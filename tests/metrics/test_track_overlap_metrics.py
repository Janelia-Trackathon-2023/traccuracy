from copy import deepcopy

import networkx as nx
import pytest
from traccuracy import TrackingGraph
from traccuracy.matchers import Matched
from traccuracy.metrics._track_overlap import TrackOverlapMetrics, _mapping_to_dict


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
    {
        "name": "overlap",
        # 0 - 0 - 0 - 0
        #       |
        #       - 1 - 1
        "gt_edges": [
            ("0_0", "1_0"),
            ("1_0", "2_0"),
            ("2_0", "3_0"),
            ("1_0", "2_1"),
            ("2_1", "3_1"),
        ],
        # 0 - 0 - 0
        #       |
        #       - 1 - 1
        #     2 - 2 - 2
        # (2 and 1 overlap)
        "pred_edges": [
            ("0_0", "1_0"),
            ("1_0", "2_0"),
            ("1_0", "2_1"),
            ("2_1", "3_1"),
            ("1_2", "2_2"),
            ("2_2", "3_2"),
        ],
        "mapping": [  # GT to pred mapping
            ("0_0", "0_0"),
            ("1_0", "1_0"),
            ("2_0", "2_0"),
            ("3_0", "3_0"),
            ("2_1", "2_1"),
            ("3_1", "3_1"),
            ("2_1", "2_2"),
            ("3_1", "3_2"),
        ],
        "results_with_division_edges": {
            "track_purity": 5 / 6,
            "target_effectiveness": 4 / 5,
        },
        "results_without_division_edges": {
            "track_purity": 3 / 4,
            "target_effectiveness": 2 / 3,
        },
    },
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
    "target_effectiveness": 5 / 11,
}
simple2["results_without_division_edges"] = {
    "track_purity": 5 / 7,
    "target_effectiveness": 5 / 9,
}
TEST_TREES.append(simple2)
assert TEST_TREES[0] != TEST_TREES[1]


@pytest.mark.parametrize("data", TEST_TREES)
@pytest.mark.parametrize("inverse", [False, True])
def test_track_overlap_metrics(data, inverse) -> None:
    g_gt = add_frame(nx.from_edgelist(data["gt_edges"], create_using=nx.DiGraph))
    g_pred = add_frame(nx.from_edgelist(data["pred_edges"], create_using=nx.DiGraph))
    if "mapping" in data:
        mapping = data["mapping"]
    else:
        mapping = [(n, n) for n in g_gt.nodes]

    if inverse:
        g_gt, g_pred = g_pred, g_gt
        mapping = [(b, a) for a, b in mapping]

    matched = Matched(
        TrackingGraph(g_gt),
        TrackingGraph(g_pred),
        mapping,
    )

    metric = TrackOverlapMetrics()
    results = metric._compute(matched)
    assert results

    expected = data["results_with_division_edges"]
    if inverse:
        expected = {
            "track_purity": expected["target_effectiveness"],
            "target_effectiveness": expected["track_purity"],
        }
    assert results == expected, f"{data['name']} failed with division edges"

    metric = TrackOverlapMetrics(include_division_edges=False)
    results = metric._compute(matched)
    assert results

    expected = data["results_without_division_edges"]
    if inverse:
        expected = {
            "track_purity": expected["target_effectiveness"],
            "target_effectiveness": expected["track_purity"],
        }
    assert results == expected, f"{data['name']} failed without division edges"


def test_mapping_to_dict():
    mapping = [("1", "2"), ("2", "3"), ("1", "3"), ("2", "3")]
    mapping_dict = _mapping_to_dict(mapping)
    assert mapping_dict == {"1": ["2", "3"], "2": ["3", "3"]}
