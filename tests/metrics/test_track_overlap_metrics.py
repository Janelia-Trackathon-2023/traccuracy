from copy import deepcopy

import networkx as nx
import pytest
from traccuracy import TrackingGraph
from traccuracy.metrics._track_overlap import TrackOverlapMetrics

from tests.test_utils import DummyMatched


def add_frame(tree):
    attrs = {}
    for node in tree.nodes:
        attrs[node] = {"t": int(node.split("_")[0]), "x": 0, "y": 0}
    nx.set_node_attributes(tree, attrs)
    return tree


TEST_TREES = [
    {
        "name": "simple1",
        "gt_edges": [
            # 0 - 0 - 0 - 0 - 0 - 0
            #           |
            #           - 1 - 1 - 1
            #
            #     2 - 2 - 2 - 2
            ("0_0", "1_0"),
            ("1_0", "2_0"),
            ("2_0", "3_0"),
            ("3_0", "4_0"),
            ("4_0", "5_0"),
            ("2_0", "3_1"),
            ("3_1", "4_1"),
            ("4_1", "5_1"),
            ("1_2", "2_2"),
            ("2_2", "3_2"),
            ("3_2", "4_2"),
        ],
        "pred_edges": [
            # 0 - 0 - 0 - 0   0 - 0
            #           |
            #           - 1
            #               - 1 - 1
            #               |
            #     2 - 2 - 2 -
            ("0_0", "1_0"),
            ("1_0", "2_0"),
            ("2_0", "3_0"),
            ("4_0", "5_0"),
            ("2_0", "3_1"),
            ("1_2", "2_2"),
            ("2_2", "3_2"),
            ("3_2", "4_1"),
            ("4_1", "5_1"),
            ("4_1", "5_1"),
            ("4_1", "5_1"),
        ],
        "results_with_division_edges": {
            "track_purity": 7 / 9,
            "target_effectiveness": 6 / 11,
        },
        "results_without_division_edges": {
            "track_purity": 5 / 7,
            "target_effectiveness": 6 / 9,
        },
    },
    #    {
    #        "name" : "overlap",
    #        "gt_edges" : [
    #            ("0_0", "1_0"),
    #            ("1_0", "2_0"),
    #            ("2_0", "3_0"),
    #            ("1_0", "2_1"),
    #            ("2_1", "3_1"),
    #        ],
    #
    #    }
]

simple2 = deepcopy(TEST_TREES[0])
simple2["name"] = "simple2"
# 0 - 0 - 0 - 0   0 - 0
#           |
#           - 1
#               - 1 - 1
#               |
#     2 - 2 - 2 -
#           |
#           - 3 - 3
simple2["pred_edges"].extend(
    [
        ("2_2", "3_3"),
        ("3_3", "4_3"),
    ]
)
simple2["results_with_division_edges"] = {
    "track_purity": 7 / 11,
    "target_effectiveness": 6 / 11,
}
simple2["results_without_division_edges"] = {
    "track_purity": 5 / 9,
    "target_effectiveness": 6 / 9,
}
TEST_TREES.append(simple2)
assert TEST_TREES[0] != TEST_TREES[1]


@pytest.mark.parametrize("data", TEST_TREES)
def test_track_overlap_metrics(data) -> None:
    g_gt = add_frame(nx.from_edgelist(data["gt_edges"], create_using=nx.DiGraph))
    g_pred = add_frame(nx.from_edgelist(data["pred_edges"], create_using=nx.DiGraph))
    mapping = [(n, n) for n in g_gt.nodes]

    matched = DummyMatched(
        TrackingGraph(g_gt),
        TrackingGraph(g_pred),
        mapper=mapping,
    )

    metric = TrackOverlapMetrics(matched)
    assert metric.results

    assert (
        metric.results == data["results_with_division_edges"]
    ), f"{data['name']} failed with division edges"

    metric = TrackOverlapMetrics(matched, include_division_edges=False)
    assert metric.results

    assert (
        metric.results == data["results_without_division_edges"]
    ), f"{data['name']} failed without division edges"
