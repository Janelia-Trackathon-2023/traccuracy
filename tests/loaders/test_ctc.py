import pandas as pd
from cell_tracking_metrics.loaders import ctc


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
