import networkx as nx
import pytest
from cell_tracking_metrics.track_errors.divisions import (
    _get_pred_by_t,
    _get_succ_by_t,
    classify_divisions,
    correct_shifted_divisions,
    evaluate_division_events,
)
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
    assert len(counts.tp_divisions) == 1
    assert len(counts.fn_divisions) == 0
    assert len(counts.fp_divisions) == 0
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
    assert len(counts.fp_divisions) == 1
    assert len(counts.tp_divisions) == 1
    assert len(counts.fn_divisions) == 0
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
    assert len(counts.fp_divisions) == 0
    assert len(counts.tp_divisions) == 0
    assert len(counts.fn_divisions) == 1
    assert "is_fn_division" in G_gt.nodes()["2_2"]


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


def get_division_graphs():
    """
    G1
                                2_4
    1_0 -- 1_1 -- 1_2 -- 1_3 -<
                                3_4
    G2
                  2_2 -- 2_3 -- 2_4
    1_0 -- 1_1 -<
                  3_2 -- 3_3 -- 3_4
    """

    G1 = nx.DiGraph()
    G1.add_edge("1_0", "1_1")
    G1.add_edge("1_1", "1_2")
    G1.add_edge("1_2", "1_3")
    G1.add_edge("1_3", "2_4")
    G1.add_edge("1_3", "3_4")

    attrs = {}
    for node in G1.nodes:
        attrs[node] = {"t": int(node[-1:]), "x": 0, "y": 0}
    nx.set_node_attributes(G1, attrs)

    G2 = nx.DiGraph()
    G2.add_edge("1_0", "1_1")
    # Divide to generate 2 lineage
    G2.add_edge("1_1", "2_2")
    G2.add_edge("2_2", "2_3")
    G2.add_edge("2_3", "2_4")
    # Divide to generate 3 lineage
    G2.add_edge("1_1", "3_2")
    G2.add_edge("3_2", "3_3")
    G2.add_edge("3_3", "3_4")

    attrs = {}
    for node in G2.nodes:
        attrs[node] = {"t": int(node[-1:]), "x": 0, "y": 0}
    nx.set_node_attributes(G2, attrs)

    mapper = [("1_0", "1_0"), ("1_1", "1_1"), ("2_4", "2_4"), ("3_4", "3_4")]

    return G1, G2, mapper


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
        G_gt.nodes["1_1"]["is_fn_division"] = True
        G_pred.nodes["1_3"]["is_fp_division"] = True

        # buffer of 1, no change
        counts = correct_shifted_divisions(
            TrackingGraph(G_gt), TrackingGraph(G_pred), mapper, n_frames=1
        )
        assert len(counts.fp_divisions) == 1
        assert len(counts.fn_divisions) == 1
        assert len(counts.tp_divisions) == 0

    def test_fn_early(self):
        # Early division in gt
        G_pred, G_gt, mapper = get_division_graphs()
        G_gt.nodes["1_1"]["is_fn_division"] = True
        G_pred.nodes["1_3"]["is_fp_division"] = True

        # buffer of 3, corrections
        counts = correct_shifted_divisions(
            TrackingGraph(G_gt), TrackingGraph(G_pred), mapper, n_frames=3
        )
        assert len(counts.tp_divisions) == 1
        assert len(counts.fp_divisions) == 0
        assert len(counts.fn_divisions) == 0

    def test_fp_early(self):
        # Early division in pred
        G_gt, G_pred, mapper = get_division_graphs()
        G_pred.nodes["1_1"]["is_fp_division"] = True
        G_gt.nodes["1_3"]["is_fn_division"] = True

        # buffer of 3, corrections
        counts = correct_shifted_divisions(
            TrackingGraph(G_gt), TrackingGraph(G_pred), mapper, n_frames=3
        )
        assert len(counts.tp_divisions) == 1
        assert len(counts.fp_divisions) == 0
        assert len(counts.fn_divisions) == 0


def test_evaluate_division_events():
    G_gt, G_pred, mapper = get_division_graphs()
    frame_buffer = (0, 1, 2)

    events = evaluate_division_events(
        TrackingGraph(G_gt), TrackingGraph(G_pred), mapper, frame_buffer=frame_buffer
    )

    for e in events:
        assert e.frame_buffer in frame_buffer
        if e.frame_buffer in (0, 1):
            # No corrections
            assert len(e.tp_divisions) == 0
            assert len(e.fp_divisions) == 1
            assert len(e.fn_divisions) == 1
        else:
            # Correction
            assert len(e.tp_divisions) == 1
            assert len(e.fp_divisions) == 0
            assert len(e.fn_divisions) == 0
