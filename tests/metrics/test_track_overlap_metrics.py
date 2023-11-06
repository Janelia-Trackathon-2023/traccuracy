import networkx as nx
import pytest
from traccuracy import TrackingGraph
from traccuracy.metrics._track_overlap import TrackOverlapMetrics

from tests.test_utils import DummyMatched


@pytest.fixture
def test_trees():
    # 0 - 1 - 2 - 3 - 4 - 5
    #           |
    #           - 3 - 4 - 5
    #
    #     1 - 2 - 3 - 4
    true_edges = [
        ((0, 0), (1, 0)),
        ((1, 0), (2, 0)),
        ((2, 0), (3, 0)),
        ((3, 0), (4, 0)),
        ((4, 0), (5, 0)),
        ((2, 0), (3, 1)),
        ((3, 1), (4, 1)),
        ((4, 1), (5, 1)),
        ((1, 2), (2, 2)),
        ((2, 2), (3, 2)),
        ((3, 2), (4, 2)),
    ]

    # 0 - 1 - 2 - 3   4 - 5
    #           |
    #           - 3
    #               - 4 - 5
    #               |
    #     1 - 2 - 3 -
    pred_edges = [
        ((0, 0), (1, 0)),
        ((1, 0), (2, 0)),
        ((2, 0), (3, 0)),
        ((4, 0), (5, 0)),
        ((2, 0), (3, 1)),
        ((1, 2), (2, 2)),
        ((2, 2), (3, 2)),
        ((3, 2), (4, 1)),
        ((4, 1), (5, 1)),
    ]

    def to_str(x):
        return "_".join([str(i) for i in x])

    def to_tree(x):
        return nx.from_edgelist(
            [(to_str(n1), to_str(n2)) for n1, n2 in x], create_using=nx.DiGraph
        )

    true_tree = to_tree(true_edges)
    pred_tree = to_tree(pred_edges)

    attrs = {}
    for node in true_tree.nodes:
        attrs[node] = {"t": int(node.split("_")[0]), "x": 0, "y": 0}
    nx.set_node_attributes(true_tree, attrs)
    attrs = {}
    for node in pred_tree.nodes:
        attrs[node] = {"t": int(node.split("_")[0]), "x": 0, "y": 0}
    nx.set_node_attributes(pred_tree, attrs)

    mapping = [(n, n) for n in true_tree.nodes]
    return true_tree, pred_tree, mapping


def test_track_overlap_metrics(test_trees) -> None:
    g_gt, g_pred, mapping = test_trees
    matched = DummyMatched(
        TrackingGraph(g_gt),
        TrackingGraph(g_pred),
        mapper=mapping,
    )

    metric = TrackOverlapMetrics(matched)
    assert metric.results

    assert metric.results == {
        "track_purity": 7 / 9,
        "target_effectiveness": 6 / 11,
    }

    metric = TrackOverlapMetrics(matched, include_division_edges=False)
    assert metric.results

    assert metric.results == {
        "track_purity": 5 / 7,
        "target_effectiveness": 6 / 9,
    }
