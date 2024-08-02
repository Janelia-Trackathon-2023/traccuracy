import os

import pandas as pd
from traccuracy._tracking_graph import TrackingGraph
from traccuracy.loaders import _ctc


def test_ctc_to_graph():
    # cell_id, start, end, parent_id
    data = [
        {"Cell_ID": 1, "Start": 0, "End": 3, "Parent_ID": 0},
        {"Cell_ID": 2, "Start": 0, "End": 2, "Parent_ID": 0},
        {"Cell_ID": 3, "Start": 3, "End": 3, "Parent_ID": 2},
        {"Cell_ID": 4, "Start": 3, "End": 3, "Parent_ID": 2},
        {"Cell_ID": 5, "Start": 3, "End": 3, "Parent_ID": 4},
    ]
    df = pd.DataFrame(data)
    G = _ctc.ctc_to_graph(
        df, pd.DataFrame({"segmentation_id": [], "x": [], "y": [], "z": [], "t": []})
    )
    for d in data:
        node_ids = [
            "{}_{}".format(d["Cell_ID"], t) for t in range(d["Start"], d["End"] + 1)
        ]

        for node_id in node_ids:
            assert node_id in G

        if d["Parent_ID"]:  # should have a division
            parent_row = df[df["Cell_ID"] == d["Parent_ID"]].iloc[
                0
            ]  # Needs to be a Series for indexing below
            daughter_id = "{}_{}".format(d["Cell_ID"], d["Start"])
            parent_id = "{}_{}".format(parent_row["Cell_ID"], parent_row["End"])
            if G.has_node(parent_id):
                assert G.has_edge(parent_id, daughter_id)
            else:
                assert not G.in_degree(daughter_id)


def test_ctc_single_nodes():
    data = [
        {"Cell_ID": 1, "Start": 0, "End": 3, "Parent_ID": 0},
        {"Cell_ID": 2, "Start": 0, "End": 2, "Parent_ID": 0},
        {"Cell_ID": 3, "Start": 3, "End": 3, "Parent_ID": 2},
        {"Cell_ID": 4, "Start": 3, "End": 3, "Parent_ID": 2},
        {"Cell_ID": 5, "Start": 3, "End": 3, "Parent_ID": 4},
    ]

    detections = [
        {"segmentation_id": 1, "x": 1, "y": 2, "z": 1, "t": 0},
        {"segmentation_id": 1, "x": 1, "y": 2, "z": 1, "t": 1},
        {"segmentation_id": 1, "x": 1, "y": 2, "z": 1, "t": 2},
        {"segmentation_id": 1, "x": 1, "y": 2, "z": 1, "t": 3},
        {"segmentation_id": 2, "x": 2, "y": 1, "z": 1, "t": 0},
        {"segmentation_id": 2, "x": 2, "y": 1, "z": 1, "t": 1},
        {"segmentation_id": 2, "x": 2, "y": 1, "z": 1, "t": 2},
        {"segmentation_id": 2, "x": 2, "y": 1, "z": 1, "t": 3},
        {"segmentation_id": 3, "x": 1, "y": 1, "z": 1, "t": 3},
        {"segmentation_id": 4, "x": 1, "y": 2, "z": 2, "t": 3},
        {"segmentation_id": 5, "x": 1, "y": 1, "z": 2, "t": 3},
    ]
    df = pd.DataFrame(data)
    G = _ctc.ctc_to_graph(df, pd.DataFrame.from_records(detections))
    # This should raise an error if there are no times for single nodes
    TrackingGraph(G)


def test_ctc_with_gap_closing():
    data = [
        {"Cell_ID": 1, "Start": 0, "End": 1, "Parent_ID": 0},
        {"Cell_ID": 2, "Start": 0, "End": 1, "Parent_ID": 0},
        # Connecting frame 1 to frame 3
        {"Cell_ID": 3, "Start": 3, "End": 5, "Parent_ID": 1},
        # Connecting frame 1 to frame 6
        {"Cell_ID": 4, "Start": 6, "End": 8, "Parent_ID": 2},
    ]
    df = pd.DataFrame(data)
    G = _ctc.ctc_to_graph(
        df, pd.DataFrame({"segmentation_id": [], "x": [], "y": [], "z": [], "t": []})
    )
    assert G.has_edge("1_1", "3_3")
    assert G.has_edge("2_1", "4_6")


def test_load_data():
    test_dir = os.path.abspath(__file__)
    data_dir = os.path.abspath(
        os.path.join(test_dir, "../../../examples/sample-data/Fluo-N2DL-HeLa/01_RES/")
    )
    track_path = os.path.join(data_dir, "res_track.txt")
    track_data = _ctc.load_ctc_data(data_dir, track_path)
    assert isinstance(track_data, TrackingGraph)
    assert len(track_data.segmentation) == 92


def test_load_data_no_track_path():
    test_dir = os.path.abspath(__file__)
    data_dir = os.path.abspath(
        os.path.join(test_dir, "../../../examples/sample-data/Fluo-N2DL-HeLa/01_RES/")
    )
    track_data = _ctc.load_ctc_data(data_dir)
    assert isinstance(track_data, TrackingGraph)
    assert len(track_data.segmentation) == 92
