import os

import pandas as pd
from traccuracy import TrackingData
from traccuracy.loaders import ctc
from traccuracy.tracking_graph import TrackingGraph


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
    G = ctc.ctc_to_graph(
        df, pd.DataFrame({"segmentation_id": [], "x": [], "y": [], "z": [], "t": []})
    )
    for d in data:
        node_ids = [
            "{}_{}".format(d["Cell_ID"], t) for t in range(d["Start"], d["End"] + 1)
        ]

        for node_id in node_ids:
            assert node_id in G

        if d["Parent_ID"]:  # should have a division
            daughter_id = "{}_{}".format(d["Cell_ID"], d["Start"])
            parent_id = "{}_{}".format(d["Parent_ID"], d["Start"] - 1)
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
    G = ctc.ctc_to_graph(df, pd.DataFrame.from_records(detections))
    # This should raise an error if there are no times for single nodes
    TrackingGraph(G)


def test_load_data():
    test_dir = os.path.abspath(__file__)
    data_dir = os.path.abspath(
        os.path.join(test_dir, "../../../examples/sample-data/Fluo-N2DL-HeLa/01_RES/")
    )
    track_path = os.path.join(data_dir, "res_track.txt")
    track_data = ctc.load_ctc_data(data_dir, track_path)
    assert isinstance(track_data, TrackingData)
    assert isinstance(track_data.tracking_graph, TrackingGraph)
    assert len(track_data.segmentation) == 92


def test_load_data_no_track_path():
    test_dir = os.path.abspath(__file__)
    data_dir = os.path.abspath(
        os.path.join(test_dir, "../../../examples/sample-data/Fluo-N2DL-HeLa/01_RES/")
    )
    track_data = ctc.load_ctc_data(data_dir)
    assert isinstance(track_data, TrackingData)
    assert isinstance(track_data.tracking_graph, TrackingGraph)
    assert len(track_data.segmentation) == 92
