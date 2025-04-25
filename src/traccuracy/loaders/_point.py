from typing import Optional, cast

import networkx as nx
import pandas as pd

from traccuracy._tracking_graph import TrackingGraph


def load_point_data(
    path: str | None = None,
    df: Optional[pd.DataFrame] = None,  # noqa: UP007, bar syntax breaks docks build
    parent_column: str = "parent",
    id_column: str | None = None,
    pos_columns: tuple[str, ...] = ("z", "y", "x"),
    time_column: str = "t",
    name: str | None = None,
    sep: str | None = None,
) -> TrackingGraph:
    """Load point-based tracking data into a TrackingGraph from a csv-like file

    Assumes each row contains:
    - time
    - position, e.g. three columns 'z', 'y', 'x'
    - parent, a reference to the node in the previous time frame

    Args:
        path (str | None, optional): Path to the csv-like file to load. Defaults to None.
        df (pd.DataFrame | None, optional): A dataframe that has already been loaded.
            Defaults to None.
        parent_column (str | None, optional): A reference to the parent node in the previous
            time frame. Defaults to "parent".
        id_column (str | None, optional): Optional column used to specify node ids.
            Defaults to None and the row index is used as the id
        pos_columns (tuple[str], optional): A tuple of columns to use for position.
            Defaults to ("z", "y", "x").
        time_column (str, optional): The column to use for time. Defaults to "t".
        name (str | None, optional): Optional string to name/describe the dataset. Defaults to None.
        sep (str | None, optional): Passed to pd.read_csv to set the sep kwarg. Defaults to None.

    Raises:
        ValueError: Must provide either a path or a dataframe
        ValueError: parent_column not present in data
        ValueError: id_column not present in data
        ValueError: pos_columns not present in data
        ValueError: time_column not present in data

    Returns:
        TrackingGraph
    """
    if path is None and df is None:
        raise ValueError("Must provide either a path or a dataframe")

    if path:
        if sep is None:
            df = pd.read_csv(path)
        else:
            df = pd.read_csv(path, sep=sep)

    # At this point, df is guaranteed to be dataframe not None
    df = cast("pd.DataFrame", df)

    if parent_column not in df.columns:
        raise ValueError(f"Specified parent_column {parent_column} not present")

    if id_column and id_column not in df.columns:
        raise ValueError(f"Specified id_column {id_column} not present")

    if not all(c in df.columns for c in pos_columns):
        raise ValueError(f"Specified pos_columns {pos_columns} not present")

    if time_column not in df.columns:
        raise ValueError(f"Specified time_column {time_column} not present")

    nodes, edges = [], []
    for idx, row in df.iterrows():
        if id_column is None:
            node_id = idx
        else:
            node_id = row[id_column]

        nodes.append((node_id, row[[time_column, *pos_columns]].to_dict()))

        if row[parent_column] != -1:
            edges.append((row[parent_column], node_id))

    G: nx.DiGraph = nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    return TrackingGraph(G, frame_key=time_column, location_keys=pos_columns, name=name)
