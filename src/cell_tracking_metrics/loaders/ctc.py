import glob
import os

import networkx as nx
import numpy as np
import pandas as pd
from skimage.measure import regionprops_table
from tifffile import imread

from cell_tracking_metrics._tracking_graph import TrackingGraph
from cell_tracking_metrics.tracking_data import TrackingData


def load_tiffs(data_dir):
    """Load a directory of individual frames into a stack.

    Args:
        data_dir (Path): Path to directory of tiff files

    Raises:
        FileNotFoundError: No tif files found in data_dir

    Returns:
        np.array: 4D array with dims TYXC
    """
    files = np.sort(glob.glob(f"{data_dir}/*.tif*"))
    if len(files) == 0:
        raise FileNotFoundError(f"No tif files were found in {data_dir}")

    ims = []
    for f in files:
        ims.append(imread(f))

    mov = np.stack(ims)
    return mov


def _detections_from_image(stack, idx):
    """Return the unique track label, centroid and time for each track vertex.

    Args:
        stack (np.ndarray): Stack of masks
        idx (int): Index of the image to calculate the centroids and track labels

    Returns:
        pd.DataFrame: The dataframe of track data for one time step (specified by idx)
    """
    props = regionprops_table(
        np.asarray(stack[idx, ...]), properties=("label", "centroid")
    )
    props["t"] = np.full(props["label"].shape, idx)
    return pd.DataFrame(props)


def get_node_attributes(masks):
    """Calculates x,y,z,t,label for each detection in a movie.

    Args:
        masks (np.ndarray): Set of masks with time in the first axis

    Returns:
        pd.DataFrame: Dataframe with one detection per row. Columns
            segmentation_id, x, y, z, t
    """
    data_df = pd.concat(
        [_detections_from_image(masks, idx) for idx in range(masks.shape[0])]
    ).reset_index(drop=True)
    data_df = data_df.rename(
        columns={
            "label": "segmentation_id",
            "centroid-2": "z",
            "centroid-1": "y",
            "centroid-0": "x",
        }
    )
    return data_df


def ctc_to_graph(df, detections):
    """Create a Graph from DataFrame of CTC info with node attributes.

    Args:
        data (pd.DataFrame): DataFrame of CTC-style info
        detections (pd.DataFrame): Dataframe from get_node_attributes with position
            and segmentation label for each cell detection

    Returns:
        networkx.Graph: Graph representation of the CTC data.

    Raises:
        ValueError: If the Parent_ID is not in any previous frames.
    """
    edges = []

    all_ids = set()
    single_nodes = set()

    # Add each continuous cell lineage as a set of edges to df
    for _, row in df.iterrows():
        tpoints = np.arange(row["Start"], row["End"] + 1)

        cellids = ["{}_{}".format(row["Cell_ID"], t) for t in tpoints]

        if len(cellids) == 1:
            single_nodes.add(cellids[0])

        all_ids.update(cellids)

        edges.append(
            pd.DataFrame(
                {
                    "source": cellids[0:-1],
                    "target": cellids[1:],
                }
            )
        )

    # Add parent-daughter connections
    for _, row in df[df["Parent_ID"] != 0].iterrows():
        # Assume the parent is in the previous frame.
        parent_frame = row["Start"] - 1
        source = "{}_{}".format(row["Parent_ID"], parent_frame)

        if source not in all_ids:  # parents should be in the previous frame.
            # parent_frame = df[df['Cell_ID'] == row['Parent_id']]['End']
            # source = '{}_{}'.format(row['Parent_ID'], parent_frame)
            print("skipped parent {} to daughter {}".format(source, row["Cell_ID"]))
            continue

        target = "{}_{}".format(row["Cell_ID"], row["Start"])

        edges.append(pd.DataFrame({"source": [source], "target": [target]}))

    # Store position attributes on nodes
    detections["node_id"] = (
        detections["segmentation_id"].astype("str")
        + "_"
        + detections["t"].astype("str")
    )
    detections = detections.set_index("node_id")

    attributes = {}
    for i, row in detections.iterrows():
        attributes[i] = row

    # Create graph
    edges = pd.concat(edges)
    G = nx.from_pandas_edgelist(
        edges, source="source", target="target", create_using=nx.DiGraph
    )

    # Add all isolates to graph
    for cell_id in single_nodes:
        G.add_node(cell_id)

    nx.set_node_attributes(G, attributes)

    return G


def load_ctc_data(data_dir, track_path):
    """Read the CTC track file and create a Graph.

    Args:
        path (str): Path to the CTC text file.

    Returns:
        networkx.Graph: Graph representation of the ISBI data.

    Raises:
        ValueError: If the Parent_ID is not in any previous frames.
    """
    names = ["Cell_ID", "Start", "End", "Parent_ID"]
    tracks = pd.read_csv(
        os.path.join(data_dir, track_path), header=None, sep=" ", names=names
    )

    masks = load_tiffs(data_dir)
    detections = get_node_attributes(masks)

    G = ctc_to_graph(tracks, detections)

    data = TrackingData(TrackingGraph(G), segmentation=masks)

    return data
