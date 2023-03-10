import networkx as nx
import pytest
from cell_tracking_metrics.track_errors.divisions import classify_divisions
from cell_tracking_metrics.tracking_graph import TrackingGraph


@pytest.fixture
def G():
    """
    1_0 -- 1_1 -- 1_2 -- 1_3
                         3_3
    2_0 -- 2_1 -- 2_2 -<
                         4_3
    """
    G = nx.DiGraph()
    G.add_edge("1_0", "1_1")
    G.add_edge("1_1", "1_2")
    G.add_edge("1_2", "1_3")

    G.add_edge("2_0", "2_1")
    G.add_edge("2_1", "2_2")

    # node 2 divides into 3 and 4 in frame 3
    G.add_edge("2_2", "3_3")
    G.add_edge("2_2", "4_3")

    # Set node attributes
    attrs = {}
    for node in G.nodes:
        attrs[node] = {"t": int(node[-1:]), "x": 0, "y": 0}
    nx.set_node_attributes(G, attrs)

    return G


def test_classify_divisions_tp(G):
    # Define mapper assuming all nodes match
    mapper = [(n, n) for n in G.nodes]

    # Test true positive
    counts, G_gt, G_pred = classify_divisions(
        TrackingGraph(G), TrackingGraph(G), mapper
    )
    assert counts.tp_divisions == 1
    assert counts.fn_divisions == 0
    assert counts.fp_divisions == 0
    assert "is_tp_division" in G_gt.nodes()["2_2"]
    assert "is_tp_division" in G_pred.nodes()["2_2"]


def test_classify_divisions_fp(G):
    """
                         5_3
    1_0 -- 1_1 -- 1_2 -<
                         1_3
                         3_3
    2_0 -- 2_1 -- 2_2 -<
                         4_3
    """
    H = G.copy()
    # Add false positive division edge
    H.add_edge("1_2", "5_3")
    nx.set_node_attributes(H, {"5_3": {"t": 3, "x": 0, "y": 0}})
    mapper = [(n, n) for n in H.nodes]

    counts, G_gt, G_pred = classify_divisions(
        TrackingGraph(G), TrackingGraph(H), mapper
    )
    assert counts.fp_divisions == 1
    assert counts.tp_divisions == 1
    assert counts.fn_divisions == 0
    assert "is_fp_division" in G_pred.nodes()["1_2"]


def test_classify_divisions_fn(G):
    """
    1_0 -- 1_1 -- 1_2 -- 1_3
    2_0 -- 2_1 -- 2_2
    """
    # Remove daughters to create false negative
    H = G.copy()
    H.remove_nodes_from(["3_3", "4_3"])
    mapper = [(n, n) for n in H.nodes]

    counts, G_gt, G_pred = classify_divisions(
        TrackingGraph(G), TrackingGraph(H), mapper
    )
    assert counts.fp_divisions == 0
    assert counts.tp_divisions == 0
    assert counts.fn_divisions == 1
    assert "is_fn_division" in G_gt.nodes()["2_2"]
