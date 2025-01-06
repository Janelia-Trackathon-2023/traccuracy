import networkx as nx
import numpy as np
import pytest

import tests.examples.graphs as ex_graphs
from traccuracy._tracking_graph import EdgeFlag, NodeFlag, TrackingGraph
from traccuracy.matchers import Matched
from traccuracy.track_errors._ctc import get_edge_errors, get_vertex_errors


class TestStandardNode:
    def test_no_gt(self):
        matched = ex_graphs.empty_gt()
        # all pred nodes are false positives
        get_vertex_errors(matched)
        for attrs in matched.pred_graph.nodes.values():
            assert attrs.get(NodeFlag.CTC_TRUE_POS) is False
            assert attrs.get(NodeFlag.CTC_FALSE_POS) is True
            assert attrs.get(NodeFlag.NON_SPLIT) is False

    def test_no_pred(self):
        matched = ex_graphs.empty_pred()
        # All gt nodes are false negatives
        get_vertex_errors(matched)
        for attrs in matched.gt_graph.nodes.values():
            assert attrs.get(NodeFlag.CTC_TRUE_POS) is False
            assert attrs.get(NodeFlag.CTC_FALSE_NEG) is True

    def test_good_matched(self):
        matched = ex_graphs.good_matched()
        # all nodes gt/pred are true pos
        get_vertex_errors(matched)
        for attrs in matched.gt_graph.nodes.values():
            assert attrs.get(NodeFlag.CTC_TRUE_POS) is True
            assert attrs.get(NodeFlag.CTC_FALSE_NEG) is False
        for attrs in matched.pred_graph.nodes.values():
            assert attrs.get(NodeFlag.CTC_TRUE_POS) is True
            assert attrs.get(NodeFlag.CTC_FALSE_POS) is False
            assert attrs.get(NodeFlag.NON_SPLIT) is False

    @pytest.mark.parametrize("t", [0, 1, 2])
    def test_fn_node(self, t):
        wrong_node = [1, 2, 3][t]
        matched = ex_graphs.fn_node_matched(t)
        # Missing pred node = false neg in gt
        get_vertex_errors(matched)

        # Check gt graph
        for node, attrs in matched.gt_graph.nodes.items():
            if node == wrong_node:
                assert attrs[NodeFlag.CTC_TRUE_POS] is False
                assert attrs[NodeFlag.CTC_FALSE_NEG] is True
            else:
                assert attrs[NodeFlag.CTC_TRUE_POS] is True
                assert attrs[NodeFlag.CTC_FALSE_NEG] is False

        # Check pred graph -- all correct
        for attrs in matched.pred_graph.nodes.values():
            assert attrs.get(NodeFlag.CTC_TRUE_POS) is True
            assert attrs.get(NodeFlag.CTC_FALSE_POS) is False
            assert attrs.get(NodeFlag.NON_SPLIT) is False

    @pytest.mark.parametrize("t", [0, 1, 2])
    def test_fp_node(self, t):
        matched = ex_graphs.fp_node_matched(t)
        # Pred has a false pos node in t
        get_vertex_errors(matched)

        # GT all correct
        for attrs in matched.gt_graph.nodes.values():
            assert attrs[NodeFlag.CTC_TRUE_POS] is True
            assert attrs[NodeFlag.CTC_FALSE_NEG] is False

        # Check pred
        for node, attrs in matched.pred_graph.nodes.items():
            if node == 7:
                assert attrs.get(NodeFlag.CTC_TRUE_POS) is False
                assert attrs.get(NodeFlag.CTC_FALSE_POS) is True
                assert attrs.get(NodeFlag.NON_SPLIT) is False
            else:
                assert attrs.get(NodeFlag.CTC_TRUE_POS) is True
                assert attrs.get(NodeFlag.CTC_FALSE_POS) is False
                assert attrs.get(NodeFlag.NON_SPLIT) is False

    @pytest.mark.parametrize("edge_er", [0, 1])
    def test_fp_edge(self, edge_er):
        matched = ex_graphs.fp_edge_matched(edge_er)
        # Introduces two fp nodes 7 and 8
        get_vertex_errors(matched)

        # GT all correct
        # GT all correct
        for attrs in matched.gt_graph.nodes.values():
            assert attrs[NodeFlag.CTC_TRUE_POS] is True
            assert attrs[NodeFlag.CTC_FALSE_NEG] is False

        # Check pred
        for node, attrs in matched.pred_graph.nodes.items():
            if node in {7, 8}:
                assert attrs.get(NodeFlag.CTC_TRUE_POS) is False
                assert attrs.get(NodeFlag.CTC_FALSE_POS) is True
                assert attrs.get(NodeFlag.NON_SPLIT) is False
            else:
                assert attrs.get(NodeFlag.CTC_TRUE_POS) is True
                assert attrs.get(NodeFlag.CTC_FALSE_POS) is False
                assert attrs.get(NodeFlag.NON_SPLIT) is False

    # Not testing ex_graphs.one_to two b/c not supported by ctc matcher

    @pytest.mark.parametrize("t", [0, 1, 2])
    def test_nonsplit(self, t):
        matched = ex_graphs.node_two_to_one(t)
        get_vertex_errors(matched)

        # false neg in gt
        fn_nodes = {7, [1, 2, 3][t]}
        for node, attrs in matched.gt_graph.nodes.items():
            if node in fn_nodes:
                assert attrs[NodeFlag.CTC_TRUE_POS] is False
                assert attrs[NodeFlag.CTC_FALSE_NEG] is False
            else:
                assert attrs[NodeFlag.CTC_TRUE_POS] is True
                assert attrs[NodeFlag.CTC_FALSE_NEG] is False

        # nonsplit node in prediction
        ns_node = [4, 5, 6][t]
        for node, attrs in matched.pred_graph.nodes.items():
            if node == ns_node:
                assert attrs.get(NodeFlag.CTC_TRUE_POS) is False
                assert attrs.get(NodeFlag.CTC_FALSE_POS) is False
                assert attrs.get(NodeFlag.NON_SPLIT) is True
            else:
                assert attrs.get(NodeFlag.CTC_TRUE_POS) is True
                assert attrs.get(NodeFlag.CTC_FALSE_POS) is False
                assert attrs.get(NodeFlag.NON_SPLIT) is False


def test_assign_edge_errors():
    comp_ids = [3, 7, 10]
    comp_ids_2 = list(np.asarray(comp_ids) + 1)
    comp_ids += comp_ids_2

    gt_ids = [4, 12, 17]
    gt_ids_2 = list(np.asarray(gt_ids) + 1)
    gt_ids += gt_ids_2

    mapping = [(4, 3), (12, 7), (17, 10), (5, 4), (18, 11), (13, 8)]

    # need a tp, fp, fn
    comp_edges = [(3, 4), (7, 8)]
    comp_g = nx.DiGraph()
    comp_g.add_nodes_from(comp_ids)
    comp_g.add_edges_from(comp_edges)
    nx.set_node_attributes(comp_g, True, NodeFlag.CTC_TRUE_POS)
    nx.set_node_attributes(
        comp_g,
        {idx: {"t": 0, "segmentation_id": 1, "y": 0, "x": 0} for idx in comp_ids},
    )
    G_comp = TrackingGraph(comp_g)

    gt_edges = [(4, 5), (17, 18)]
    gt_g = nx.DiGraph()
    gt_g.add_nodes_from(gt_ids)
    gt_g.add_edges_from(gt_edges)
    nx.set_node_attributes(gt_g, False, NodeFlag.CTC_FALSE_NEG)
    nx.set_node_attributes(
        gt_g, {idx: {"t": 0, "segmentation_id": 1, "y": 0, "x": 0} for idx in gt_ids}
    )
    G_gt = TrackingGraph(gt_g)

    matched_data = Matched(G_gt, G_comp, mapping, {"name": "DummyMatcher"})

    get_edge_errors(matched_data)

    assert matched_data.pred_graph.edges[(7, 8)][EdgeFlag.CTC_FALSE_POS]
    assert matched_data.gt_graph.edges[(17, 18)][EdgeFlag.CTC_FALSE_NEG]


def test_assign_edge_errors_semantics():
    """
    gt:
    1_0 -- 1_1 -- 1_2 -- 1_3

    comp:
                         1_3
    1_0 -- 1_1 -- 1_2 -<
                         2_3
    """

    gt = nx.DiGraph()
    gt.add_edge("1_0", "1_1")
    gt.add_edge("1_1", "1_2")
    gt.add_edge("1_2", "1_3")
    # Set node attrs
    attrs = {}
    for node in gt.nodes:
        attrs[node] = {"t": int(node[-1:]), "x": 0, "y": 0}
    nx.set_node_attributes(gt, attrs)

    comp = gt.copy()
    comp.add_edge("1_2", "2_3")
    # Set node attrs
    attrs = {}
    for node in comp.nodes:
        attrs[node] = {"t": int(node[-1:]), "x": 0, "y": 0}
    nx.set_node_attributes(comp, attrs)

    # Define mapping with all nodes matching except for 2_3 in comp
    mapping = [(n, n) for n in gt.nodes]

    matched_data = Matched(
        TrackingGraph(gt), TrackingGraph(comp), mapping, {"name": "DummyMatcher"}
    )

    get_edge_errors(matched_data)

    assert matched_data.pred_graph.edges[("1_2", "1_3")][EdgeFlag.WRONG_SEMANTIC]


def test_ns_vertex_fn_edge():
    """Minimal Example of testing for FN edges with a NS Vertex
    gt      1 - 2 - 3
            4 - 5 - 6

    comp    1 - 2

    matching [ (1, 1), (4, 1), (2, 2), (5, 2) ]
    """

    gt_nodes = [
        (1, {"t": 0, "x": 1, "y": 1}),
        (2, {"t": 1, "x": 1, "y": 1}),
        (3, {"t": 2, "x": 1, "y": 1}),
        (4, {"t": 0, "x": 0, "y": 1}),
        (5, {"t": 1, "x": 0, "y": 1}),
        (6, {"t": 2, "x": 0, "y": 1}),
    ]
    gt_edges = [
        (1, 2),
        (2, 3),
        (4, 5),
        (5, 6),
    ]
    gt = nx.DiGraph()
    gt.add_nodes_from(gt_nodes)
    gt.add_edges_from(gt_edges)

    comp_nodes = [
        (1, {"t": 0, "x": 0.5, "y": 1}),
        (2, {"t": 1, "x": 0.5, "y": 1}),
    ]
    comp_edges = [
        (1, 2),
    ]
    comp = nx.DiGraph()
    comp.add_nodes_from(comp_nodes)
    comp.add_edges_from(comp_edges)

    mapping = [
        (1, 1),
        (5, 1),
        (2, 2),
        (5, 2),
    ]

    matched_data = Matched(
        TrackingGraph(gt), TrackingGraph(comp), mapping, {"name": "DummyMatcher"}
    )
    get_vertex_errors(matched_data)
    get_edge_errors(matched_data)

    for node in comp.nodes:
        assert comp.nodes[node][NodeFlag.NON_SPLIT]
    for edge in comp_edges:
        assert not comp.edges[edge][EdgeFlag.CTC_FALSE_POS]

    # https://github.com/Janelia-Trackathon-2023/traccuracy/pull/141#issuecomment-2265990197
    if False:  # TODO: Fix this in a separate PR
        for node in [1, 2, 4, 5]:
            assert gt.nodes[node][NodeFlag.CTC_FALSE_NEG]

    for node in [3, 6]:
        assert gt.nodes[node][NodeFlag.CTC_FALSE_NEG]

    for edge in gt_edges:
        assert gt.edges[edge][EdgeFlag.CTC_FALSE_NEG]


class TestStandardEdge:
    """Notes
    CTC does not annotate true positive edges
    """

    def prep_matched(self, matched):
        get_vertex_errors(matched)
        get_edge_errors(matched)
        return matched

    def test_no_gt(self):
        matched = self.prep_matched(ex_graphs.empty_gt())
        for attrs in matched.pred_graph.edges.values():
            # Edges on FP nodes are not additionally penalized as FP edge
            # https://github.com/Janelia-Trackathon-2023/traccuracy/pull/176#issuecomment-2552537116
            assert attrs.get(EdgeFlag.CTC_FALSE_POS) is False
            assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is False
            assert attrs.get(EdgeFlag.WRONG_SEMANTIC) is False

    def test_no_pred(self):
        matched = self.prep_matched(ex_graphs.empty_pred())
        for attrs in matched.gt_graph.edges.values():
            assert attrs.get(EdgeFlag.CTC_FALSE_NEG) is True
            assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is False

    def test_good_matched(self):
        matched = self.prep_matched(ex_graphs.good_matched())
        for attrs in matched.gt_graph.edges.values():
            assert attrs.get(EdgeFlag.CTC_FALSE_NEG) is False
            assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is False

        for attrs in matched.pred_graph.edges.values():
            assert attrs.get(EdgeFlag.CTC_FALSE_POS) is False
            assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is False
            assert attrs.get(EdgeFlag.WRONG_SEMANTIC) is False

    def test_fn_node_end(self):
        matched = self.prep_matched(ex_graphs.fn_node_matched(0))

        # All pred edges correct
        for attrs in matched.pred_graph.edges.values():
            assert attrs.get(EdgeFlag.CTC_FALSE_POS) is False
            assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is False
            assert attrs.get(EdgeFlag.WRONG_SEMANTIC) is False

        # First gt edge is false neg
        attrs = matched.gt_graph.edges[(1, 2)]
        assert attrs.get(EdgeFlag.CTC_FALSE_NEG) is True
        assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is False

    def test_fn_node_middle(self):
        matched = self.prep_matched(ex_graphs.fn_node_matched(1))

        # No pred edges to test, both removed by induced graph

        # All gt edges false neg
        for attrs in matched.gt_graph.edges.values():
            assert attrs.get(EdgeFlag.CTC_FALSE_NEG) is True
            assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is False

    def test_fn_edge(self):
        matched = self.prep_matched(ex_graphs.fn_edge_matched(0))

        # Only pred edge is correct
        attrs = matched.pred_graph.edges[(5, 6)]
        assert attrs.get(EdgeFlag.CTC_FALSE_POS) is False
        assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is False

        # First gt edge is false neg
        attrs = matched.gt_graph.edges[(1, 2)]
        assert attrs.get(EdgeFlag.CTC_FALSE_NEG) is True
        assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is False

        # Second gt edge is correct
        attrs = matched.gt_graph.edges[(2, 3)]
        assert attrs.get(EdgeFlag.CTC_FALSE_NEG) is False
        assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is False

    @pytest.mark.parametrize("t", [0, 1, 2])
    def test_fp_node(self, t):
        matched = self.prep_matched(ex_graphs.fp_node_matched(t))

        # All pred edges correct
        for attrs in matched.pred_graph.edges.values():
            assert attrs.get(EdgeFlag.CTC_FALSE_POS) is False
            assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is False
            assert attrs.get(EdgeFlag.WRONG_SEMANTIC) is False

        # All gt edges correct
        for attrs in matched.gt_graph.edges.values():
            assert attrs.get(EdgeFlag.CTC_FALSE_NEG) is False
            assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is False

    @pytest.mark.parametrize("t", [0, 1])
    def test_fp_edge(self, t):
        matched = self.prep_matched(ex_graphs.fp_edge_matched(t))

        # All but one pred edges correct
        for edge, attrs in matched.pred_graph.edges.items():
            # false positive edge
            if edge == (7, 8):
                # Not FP b/c not matched to any gt nodes
                assert attrs.get(EdgeFlag.CTC_FALSE_POS) is False
                assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is False
                assert attrs.get(EdgeFlag.WRONG_SEMANTIC) is False
            else:
                assert attrs.get(EdgeFlag.CTC_FALSE_POS) is False
                assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is False
                assert attrs.get(EdgeFlag.WRONG_SEMANTIC) is False

    def test_crossover_edge(self):
        matched = self.prep_matched(ex_graphs.crossover_edge())

        # All but one gt edge are FN
        for edge, attrs in matched.gt_graph.edges.items():
            if edge == (2, 3):
                assert attrs.get(EdgeFlag.CTC_FALSE_NEG) is False
                assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is False
            else:
                assert attrs.get(EdgeFlag.CTC_FALSE_NEG) is True
                assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is False

        # First pred edge is crossover so FP
        attrs = matched.pred_graph.edges[(7, 8)]
        assert attrs.get(EdgeFlag.CTC_FALSE_POS) is True
        assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is False
        assert attrs.get(EdgeFlag.WRONG_SEMANTIC) is False

        # Second pred edge is correct
        attrs = matched.pred_graph.edges[(8, 9)]
        assert attrs.get(EdgeFlag.CTC_FALSE_POS) is False
        assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is False
        assert attrs.get(EdgeFlag.WRONG_SEMANTIC) is False

    def test_node_two_to_one_end(self):
        """See comment thread for discussion of edge errors with NS nodes
        https://github.com/Janelia-Trackathon-2023/traccuracy/pull/176#issuecomment-2552537116
        """
        matched = self.prep_matched(ex_graphs.node_two_to_one(0))

        # All pred edges correct
        for attrs in matched.pred_graph.edges.values():
            assert attrs.get(EdgeFlag.CTC_FALSE_POS) is False
            assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is False
            assert attrs.get(EdgeFlag.WRONG_SEMANTIC) is False

        # First edge false neg as it was removed from induced graph
        attrs = matched.gt_graph.edges[(1, 2)]
        assert attrs.get(EdgeFlag.CTC_FALSE_NEG) is True
        assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is False

        # Second edge correct
        attrs = matched.gt_graph.edges[(2, 3)]
        assert attrs.get(EdgeFlag.CTC_FALSE_NEG) is False
        assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is False

    def test_node_two_to_one_mid(self):
        matched = self.prep_matched(ex_graphs.node_two_to_one(1))

        # gt edges are fn
        for attrs in matched.gt_graph.edges.values():
            assert attrs.get(EdgeFlag.CTC_FALSE_NEG) is True

        # Pred edges with NS nodes are not penalized (see comment thread above)
        for attrs in matched.pred_graph.edges.values():
            assert attrs.get(EdgeFlag.CTC_FALSE_POS) is False

    # CTCMatcher does not allow one gt to match multiple comp nodes.
    # Skipping the one_to_two example

    def test_correct_division(self):
        # Check that intertrack edges have been identified
        # No wrong semantics
        matched = self.prep_matched(ex_graphs.good_div(1))
        gt_edges = [(2, 4), (2, 3)]
        pred_edges = [(6, 7), (6, 8)]

        for edge, attrs in matched.gt_graph.edges.items():
            if edge in gt_edges:
                assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is True
            else:
                assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is False

        for edge, attrs in matched.pred_graph.edges.items():
            if edge in pred_edges:
                assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is True
            else:
                assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is False
            assert attrs.get(EdgeFlag.WRONG_SEMANTIC) is False

    def test_fp_division(self):
        # Check intertrack and for wrong semantic on fp division
        matched = self.prep_matched(ex_graphs.fp_div(1))

        # GT edge is not intertrack
        attrs = matched.gt_graph.edges[(2, 4)]
        assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is False

        # Pred edges are intertrack and wrong semantic
        attrs = matched.pred_graph.edges[(6, 8)]
        assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is True
        assert attrs.get(EdgeFlag.WRONG_SEMANTIC) is True

        attrs = matched.pred_graph.edges[(6, 7)]
        assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is True
        assert attrs.get(EdgeFlag.WRONG_SEMANTIC) is False

    def test_fn_division(self):
        # Intertrack and wrong semantic check
        matched = self.prep_matched(ex_graphs.one_child(1))

        # Pred edge
        attrs = matched.pred_graph.edges[(6, 8)]
        assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is False
        assert attrs.get(EdgeFlag.WRONG_SEMANTIC) is True

        # Gt edges are just intertrack
        attrs = matched.gt_graph.edges[(2, 4)]
        assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is True
        attrs = matched.gt_graph.edges[(2, 3)]
        assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is True

    def test_wrong_child(self):
        # Intertrack and wrong semantic check
        matched = self.prep_matched(ex_graphs.wrong_child(1))

        # One pred edge correct
        attrs = matched.pred_graph.edges[(7, 8)]
        assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is True
        assert attrs.get(EdgeFlag.WRONG_SEMANTIC) is False
        # Not wrong semantic b/c edge doesn't directly match to gt edge
        attrs = matched.pred_graph.edges[(7, 9)]
        assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is True
        assert attrs.get(EdgeFlag.WRONG_SEMANTIC) is False

        # Gt edges are just intertrack
        attrs = matched.gt_graph.edges[(2, 4)]
        assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is True
        attrs = matched.gt_graph.edges[(2, 3)]
        assert attrs.get(EdgeFlag.INTERTRACK_EDGE) is True
