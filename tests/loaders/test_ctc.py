import pandas as pd
from cell_tracking_metrics.loaders import ctc
from cell_tracking_metrics.tracking_graph import TrackingGraph


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
