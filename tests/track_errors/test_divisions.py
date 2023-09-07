import networkx as nx
import numpy as np
import pytest
from traccuracy import NodeAttr, TrackingGraph
from traccuracy.track_errors.divisions import (
    _classify_divisions,
    _correct_shifted_divisions,
    _evaluate_division_events,
    _get_pred_by_t,
    _get_succ_by_t,
)

from ..test_utils import get_division_graphs


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
    G_gt = TrackingGraph(G.copy())
    G_pred = TrackingGraph(G.copy())

    # Test true positive
    _classify_divisions(G_gt, G_pred, mapper)

    assert len(G_gt.get_nodes_with_attribute(NodeAttr.FN_DIV, lambda x: x is True)) == 0
    assert (
        len(G_pred.get_nodes_with_attribute(NodeAttr.FP_DIV, lambda x: x is True)) == 0
    )
    assert NodeAttr.TP_DIV in G_gt.nodes()["2_2"]
    assert NodeAttr.TP_DIV in G_pred.nodes()["2_2"]

    # Check division flag
    assert G_gt.division_annotations
    assert G_pred.division_annotations


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

    G_gt = TrackingGraph(G)
    G_pred = TrackingGraph(H)

    _classify_divisions(G_gt, G_pred, mapper)

    assert len(G_gt.get_nodes_with_attribute(NodeAttr.FN_DIV, lambda x: x is True)) == 0
    assert NodeAttr.FP_DIV in G_pred.nodes()["1_2"]
    assert NodeAttr.TP_DIV in G_gt.nodes()["2_2"]
    assert NodeAttr.TP_DIV in G_pred.nodes()["2_2"]


def test_classify_divisions_fn(G):
    """
    1_0 -- 1_1 -- 1_2 -- 1_3
    2_0 -- 2_1 -- 2_2
    """
    # Remove daughters to create false negative
    H = G.copy()
    H.remove_nodes_from(["3_3", "4_3"])
    mapper = [(n, n) for n in H.nodes]

    G_gt = TrackingGraph(G)
    G_pred = TrackingGraph(H)

    _classify_divisions(G_gt, G_pred, mapper)

    assert (
        len(G_pred.get_nodes_with_attribute(NodeAttr.FP_DIV, lambda x: x is True)) == 0
    )
    assert len(G_gt.get_nodes_with_attribute(NodeAttr.TP_DIV, lambda x: x is True)) == 0
    assert NodeAttr.FN_DIV in G_gt.nodes()["2_2"]


@pytest.fixture
def straight_graph():
    G = nx.DiGraph()
    for t in range(2, 10):
        G.add_edge(f"1_{t}", f"1_{t+1}")

    # Set node attributes
    attrs = {}
    for node in G.nodes:
        attrs[node] = {"t": int(node[-1:]), "x": 0, "y": 0}
    nx.set_node_attributes(G, attrs)

    return G


def test__get_pred_by_t(straight_graph):
    # Linear graph with node id 1 from frame 2-10
    G = TrackingGraph(straight_graph)

    # Predecessor available
    start_frame = 10
    target_frame = 5
    node = _get_pred_by_t(G, f"1_{start_frame}", start_frame - target_frame)
    assert node == f"1_{target_frame}"

    # Predecessor does not exist
    start_frame = 10
    target_frame = 1
    node = _get_pred_by_t(G, f"1_{start_frame}", start_frame - target_frame)
    assert node is None


def test__get_succ_by_t():
    _, G2, _ = get_division_graphs()
    G2 = TrackingGraph(G2)

    # Find 2 frames forward correctly
    start_node = "2_2"
    delta_t = 2
    end_node = "2_4"
    node = _get_succ_by_t(G2, start_node, delta_t)
    assert node == end_node

    # 3 frames forward returns None
    start_node = "2_2"
    delta_t = 3
    end_node = None
    node = _get_succ_by_t(G2, start_node, delta_t)
    assert node == end_node


class Test_correct_shifted_divisions:
    def test_no_change(self):
        # Early division in gt
        G_pred, G_gt, mapper = get_division_graphs()
        G_gt.nodes["1_1"][NodeAttr.FN_DIV] = True
        G_pred.nodes["1_3"][NodeAttr.FP_DIV] = True

        # buffer of 1, no change
        nG_gt, nG_pred = _correct_shifted_divisions(
            TrackingGraph(G_gt), TrackingGraph(G_pred), mapper, n_frames=1
        )

        assert nG_pred.nodes()["1_3"][NodeAttr.FP_DIV] is True
        assert nG_gt.nodes()["1_1"][NodeAttr.FN_DIV] is True
        assert (
            len(nG_gt.get_nodes_with_attribute(NodeAttr.TP_DIV, lambda x: x is True))
            == 0
        )

    def test_fn_early(self):
        # Early division in gt
        G_pred, G_gt, mapper = get_division_graphs()
        G_gt.nodes["1_1"][NodeAttr.FN_DIV] = True
        G_pred.nodes["1_3"][NodeAttr.FP_DIV] = True

        # buffer of 3, corrections
        nG_gt, nG_pred = _correct_shifted_divisions(
            TrackingGraph(G_gt), TrackingGraph(G_pred), mapper, n_frames=3
        )

        assert nG_pred.nodes()["1_3"][NodeAttr.FP_DIV] is False
        assert nG_gt.nodes()["1_1"][NodeAttr.FN_DIV] is False
        assert nG_pred.nodes()["1_3"][NodeAttr.TP_DIV] is True
        assert nG_gt.nodes()["1_1"][NodeAttr.TP_DIV] is True

    def test_fp_early(self):
        # Early division in pred
        G_gt, G_pred, mapper = get_division_graphs()
        G_pred.nodes["1_1"][NodeAttr.FP_DIV] = True
        G_gt.nodes["1_3"][NodeAttr.FN_DIV] = True

        # buffer of 3, corrections
        nG_gt, nG_pred = _correct_shifted_divisions(
            TrackingGraph(G_gt), TrackingGraph(G_pred), mapper, n_frames=3
        )

        assert nG_pred.nodes()["1_1"][NodeAttr.FP_DIV] is False
        assert nG_gt.nodes()["1_3"][NodeAttr.FN_DIV] is False
        assert nG_pred.nodes()["1_1"][NodeAttr.TP_DIV] is True
        assert nG_gt.nodes()["1_3"][NodeAttr.TP_DIV] is True


def test_evaluate_division_events():
    G_gt, G_pred, mapper = get_division_graphs()
    frame_buffer = (0, 1, 2)

    results = _evaluate_division_events(
        TrackingGraph(G_gt), TrackingGraph(G_pred), mapper, frame_buffer=frame_buffer
    )

    assert np.all([isinstance(k, int) for k in results.keys()])
