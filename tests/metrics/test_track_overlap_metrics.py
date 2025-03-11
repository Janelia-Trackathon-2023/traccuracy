from copy import deepcopy

import networkx as nx
import pytest

from traccuracy import TrackingGraph
from traccuracy.matchers import Matched
from traccuracy.metrics._track_overlap import TrackOverlapMetrics
import tests.examples.graphs as ex_graphs
import numpy as np

class TestStandardOverlapMetrics:
    tp = "track_purity"
    te = "target_effectiveness"

    @pytest.mark.parametrize("incl_div_edges", [True, False])
    def test_empty_gt(self, incl_div_edges):
        matched = ex_graphs.empty_gt()
        metric = TrackOverlapMetrics(include_division_edges=incl_div_edges)
        results = metric._compute(matched)
        assert results[self.tp] == 0
        assert np.isnan(results[self.te])

    @pytest.mark.parametrize("incl_div_edges", [True, False])
    def test_empty_pred(self, incl_div_edges):
        matched = ex_graphs.empty_pred()
        metric = TrackOverlapMetrics(include_division_edges=incl_div_edges)
        results = metric._compute(matched)
        assert np.isnan(results[self.tp])
        assert results[self.te] == 0

    @pytest.mark.parametrize("incl_div_edges", [True, False])
    def test_good_match(self, incl_div_edges):
        matched = ex_graphs.good_matched()
        metric = TrackOverlapMetrics(include_division_edges=incl_div_edges)
        results = metric._compute(matched)
        assert results[self.tp] == 1
        assert results[self.te] == 1

    @pytest.mark.parametrize(
        ("t", "incl_div_edges", "tp", "te"), 
        [(0, True, 1, 0.5), (0, False, 1, 0.5),
         (1, True, 0, 0), (1, False, 0, 0),
         (2, True, 1, 0.5), (2, False, 1, 0.5)
        ]
    )
    def test_fn_node(self, t, incl_div_edges, tp, te):
        matched = ex_graphs.fn_node_matched(t)
        metric = TrackOverlapMetrics(include_division_edges=incl_div_edges)
        results = metric._compute(matched)

        assert results[self.tp] == tp
        assert results[self.te] == te
    
    @pytest.mark.parametrize(
        ("edge_er", "incl_div_edges", "tp", "te"), 
        [(0, True, 1, 0.5), (0, False, 1, 0.5),
         (1, True, 1, 0.5), (1, False, 1, 0.5),
        ]
    )
    def test_fn_edge(self, edge_er, incl_div_edges, tp, te):
        matched = ex_graphs.fn_edge_matched(edge_er)
        metric = TrackOverlapMetrics(include_division_edges=incl_div_edges)
        results = metric._compute(matched)
        assert results[self.tp] == tp
        assert results[self.te] == te

    @pytest.mark.parametrize(
        ("t", "incl_div_edges", "tp", "te"), 
        [(0, True, 0.75, 1), (0, False, 0.75, 1),
         (1, True, 0.75, 1), (1, False, 0.75, 1),
         (2, True, 0.75, 1), (2, False, 0.75, 1),
        ]
    )
    def test_fp_node(self, t, incl_div_edges, tp, te):
        matched = ex_graphs.fp_node_matched(t)
        metric = TrackOverlapMetrics(include_division_edges=incl_div_edges)
        results = metric._compute(matched)
        results = metric._compute(matched)
        assert results[self.tp] == tp
        assert results[self.te] == te
    
    @pytest.mark.parametrize(
        ("edge_er", "incl_div_edges", "tp", "te"), 
        [(0, True, 2/3, 1), (0, False, 2/3, 1),
         (1, True, 2/3, 1), (1, False, 2/3, 1),
        ]
    )
    def test_fp_edge(self, edge_er, incl_div_edges, tp, te):
        matched = ex_graphs.fp_edge_matched(edge_er)
        metric = TrackOverlapMetrics(include_division_edges=incl_div_edges)
        results = metric._compute(matched)
        results = metric._compute(matched)
        assert results[self.tp] == tp
        assert results[self.te] == te
    
    @pytest.mark.parametrize(
        ("incl_div_edges", "tp", "te"), 
        [(True, 0.5, 0.25), (False, 0.5, 0.25)]
    )
    def test_crossover(self, incl_div_edges, tp, te):
        matched = ex_graphs.crossover_edge()
        metric = TrackOverlapMetrics(include_division_edges=incl_div_edges)
        results = metric._compute(matched)
        results = metric._compute(matched)
        assert results[self.tp] == tp
        assert results[self.te] == te

    # Skipping the following cases because they are not one to one
    # ex_graphs.node_two_to_one
    # ex_graphs.edge_two_to_one
    # ex_graphs.node_one_to_two
    # ex_graphs.edge_one_to_two



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

    matched = Matched(TrackingGraph(g_gt), TrackingGraph(g_pred), mapping, {"name": "DummyMatcher"})

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
