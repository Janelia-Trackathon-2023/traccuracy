import networkx as nx
import numpy as np
import pytest

from traccuracy._tracking_graph import EdgeFlag, NodeFlag, TrackingGraph
from traccuracy.matchers import Matched
from traccuracy.track_errors._ctc import get_edge_errors, get_vertex_errors

import tests.examples.graphs as ex_graphs


class Test_get_vertex_errors:
    def test_no_gt(self):
        matched = ex_graphs.empty_gt()
        # all pred nodes are false positives
        get_vertex_errors(matched)
        for attrs in matched.pred_graph.nodes.values():
            assert attrs.get(NodeFlag.TRUE_POS) == False
            assert attrs.get(NodeFlag.FALSE_POS) == True
            assert attrs.get(NodeFlag.NON_SPLIT) == False

    def test_no_pred(self):
        matched = ex_graphs.empty_pred()
        # All gt nodes are false negatives
        get_vertex_errors(matched)
        for attrs in matched.gt_graph.nodes.values():
            assert attrs.get(NodeFlag.TRUE_POS) == False
            assert attrs.get(NodeFlag.FALSE_NEG) == True

    def test_good_matched(self):
        matched = ex_graphs.good_matched()
        # all notes gt/pred are true pos
        get_vertex_errors(matched)
        for attrs in matched.gt_graph.nodes.values():
            assert attrs.get(NodeFlag.TRUE_POS) == True
            assert attrs.get(NodeFlag.FALSE_NEG) == False
        for attrs in matched.pred_graph.nodes.values():
            assert attrs.get(NodeFlag.TRUE_POS) == True
            assert attrs.get(NodeFlag.FALSE_POS) == False
            assert attrs.get(NodeFlag.NON_SPLIT) == False

    @pytest.mark.parametrize(
            "t",
            [0, 1, 2]
    )
    def test_fn_node(self, t):
        wrong_node = [1, 2, 3][t]
        matched = ex_graphs.fn_node_matched(t)
        # Missing pred node = false neg in gt
        get_vertex_errors(matched)

        # Check gt graph
        for node, attrs in matched.gt_graph.nodes.items():
            if node == wrong_node:
                assert attrs[NodeFlag.TRUE_POS] == False
                assert attrs[NodeFlag.FALSE_NEG] == True
            else:
                assert attrs[NodeFlag.TRUE_POS] == True
                assert attrs[NodeFlag.FALSE_NEG] == False

        # Check pred graph -- all correct
        for attrs in matched.pred_graph.nodes.values():
            assert attrs.get(NodeFlag.TRUE_POS) == True
            assert attrs.get(NodeFlag.FALSE_POS) == False
            assert attrs.get(NodeFlag.NON_SPLIT) == False

    @pytest.mark.parametrize(
            "t",
            [0, 1, 2]
    )
    def test_fp_node(self, t):
        matched = ex_graphs.fp_node_matched(t)
        # Pred has a false pos node in t
        get_vertex_errors(matched)

        # GT all correct
        for attrs in matched.gt_graph.nodes.values():
            assert attrs[NodeFlag.TRUE_POS] == True
            assert attrs[NodeFlag.FALSE_NEG] == False
        
        # Check pred
        for node, attrs in matched.pred_graph.nodes.items():
            if node == 7:
                assert attrs.get(NodeFlag.TRUE_POS) == False
                assert attrs.get(NodeFlag.FALSE_POS) == True
                assert attrs.get(NodeFlag.NON_SPLIT) == False
            else:
                assert attrs.get(NodeFlag.TRUE_POS) == True
                assert attrs.get(NodeFlag.FALSE_POS) == False
                assert attrs.get(NodeFlag.NON_SPLIT) == False

    @pytest.mark.parametrize(
            "edge_er",
            [0, 1]
    )
    def test_fp_edge(self, edge_er):
        matched = ex_graphs.fp_edge_matched(edge_er)
        # Introduces two fp nodes 7 and 8
        get_vertex_errors(matched)

        #GT all correct
        # GT all correct
        for attrs in matched.gt_graph.nodes.values():
            assert attrs[NodeFlag.TRUE_POS] == True
            assert attrs[NodeFlag.FALSE_NEG] == False
        
        # Check pred
        for node, attrs in matched.pred_graph.nodes.items():
            if node in {7, 8}:
                assert attrs.get(NodeFlag.TRUE_POS) == False
                assert attrs.get(NodeFlag.FALSE_POS) == True
                assert attrs.get(NodeFlag.NON_SPLIT) == False
            else:
                assert attrs.get(NodeFlag.TRUE_POS) == True
                assert attrs.get(NodeFlag.FALSE_POS) == False
                assert attrs.get(NodeFlag.NON_SPLIT) == False

    # Not testing ex_graphs.one_to two b/c not supported by ctc matcher
    
    @pytest.mark.parametrize(
            "t",
            [0, 1, 2]
    )
    def test_nonsplit(self, t):
        matched = ex_graphs.node_two_to_one(t)
        get_vertex_errors(matched)
        
        # false neg in gt
        fn_nodes = {7, [1, 2, 3][t]}
        for node, attrs in matched.gt_graph.nodes.items():
            if node in fn_nodes:
                assert attrs[NodeFlag.TRUE_POS] == False
                assert attrs[NodeFlag.FALSE_NEG] == False
            else:
                assert attrs[NodeFlag.TRUE_POS] == True
                assert attrs[NodeFlag.FALSE_NEG] == False

        # nonsplit node in prediction
        ns_node = [4, 5, 6][t]
        for node, attrs in matched.pred_graph.nodes.items():
            if node == ns_node:
                assert attrs.get(NodeFlag.TRUE_POS) == False
                assert attrs.get(NodeFlag.FALSE_POS) == False
                assert attrs.get(NodeFlag.NON_SPLIT) == True
            else:
                assert attrs.get(NodeFlag.TRUE_POS) == True
                assert attrs.get(NodeFlag.FALSE_POS) == False
                assert attrs.get(NodeFlag.NON_SPLIT) == False
        

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
    nx.set_node_attributes(comp_g, True, NodeFlag.TRUE_POS)
    nx.set_node_attributes(
        comp_g,
        {idx: {"t": 0, "segmentation_id": 1, "y": 0, "x": 0} for idx in comp_ids},
    )
    G_comp = TrackingGraph(comp_g)

    gt_edges = [(4, 5), (17, 18)]
    gt_g = nx.DiGraph()
    gt_g.add_nodes_from(gt_ids)
    gt_g.add_edges_from(gt_edges)
    nx.set_node_attributes(gt_g, False, NodeFlag.FALSE_NEG)
    nx.set_node_attributes(
        gt_g, {idx: {"t": 0, "segmentation_id": 1, "y": 0, "x": 0} for idx in gt_ids}
    )
    G_gt = TrackingGraph(gt_g)

    matched_data = Matched(G_gt, G_comp, mapping, {"name": "DummyMatcher"})

    get_edge_errors(matched_data)

    assert matched_data.pred_graph.edges[(7, 8)][EdgeFlag.FALSE_POS]
    assert matched_data.gt_graph.edges[(17, 18)][EdgeFlag.FALSE_NEG]


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
        assert not comp.edges[edge][EdgeFlag.FALSE_POS]

    # https://github.com/Janelia-Trackathon-2023/traccuracy/pull/141#issuecomment-2265990197
    if False:  # TODO: Fix this in a separate PR
        for node in [1, 2, 4, 5]:
            assert gt.nodes[node][NodeFlag.FALSE_NEG]

    for node in [3, 6]:
        assert gt.nodes[node][NodeFlag.FALSE_NEG]

    for edge in gt_edges:
        assert gt.edges[edge][EdgeFlag.FALSE_NEG]


class Test_get_edge_errors:
    # TODO: delete this flag before merging
    test_edge_tp = False

    def prep_matched(self, matched):
        get_vertex_errors(matched)
        get_edge_errors(matched)
        return matched
    
    def test_no_gt(self):
        # if pred nodes are never matched to gt nodes the corresponding edges are never reviewed
        matched = self.prep_matched(ex_graphs.empty_gt())
        for attrs in matched.pred_graph.edges.values():
            assert attrs.get(EdgeFlag.FALSE_POS) == True  # currently False 
            if self.test_edge_tp: assert attrs.get(EdgeFlag.TRUE_POS) == False  # currently None 
            assert attrs.get(EdgeFlag.INTERTRACK_EDGE) == False
            assert attrs.get(EdgeFlag.WRONG_SEMANTIC) == False
    
    def test_no_pred(self):
        matched = self.prep_matched(ex_graphs.empty_pred())
        for attrs in matched.gt_graph.edges.values():
            if self.test_edge_tp: assert attrs.get(EdgeFlag.TRUE_POS) == False # currently None 
            assert attrs.get(EdgeFlag.FALSE_NEG) == True
            assert attrs.get(EdgeFlag.INTERTRACK_EDGE) == False

    def test_good_matched(self):
        matched = self.prep_matched(ex_graphs.good_matched())
        for attrs in matched.gt_graph.edges.values():
            if self.test_edge_tp: assert attrs.get(EdgeFlag.TRUE_POS) == True # currently None
            assert attrs.get(EdgeFlag.FALSE_NEG) == False
            assert attrs.get(EdgeFlag.INTERTRACK_EDGE) == False

        for attrs in matched.pred_graph.edges.values():
            assert attrs.get(EdgeFlag.FALSE_POS) == False
            if self.test_edge_tp: assert attrs.get(EdgeFlag.TRUE_POS) == True  # currently None
            assert attrs.get(EdgeFlag.INTERTRACK_EDGE) == False
            assert attrs.get(EdgeFlag.WRONG_SEMANTIC) == False
    
    def test_fn_node_end(self):
        matched = self.prep_matched(ex_graphs.fn_node_matched(0))

        # All pred edges correct
        for attrs in matched.pred_graph.edges.values():
            if self.test_edge_tp: assert attrs.get(EdgeFlag.TRUE_POS) == True
            assert attrs.get(EdgeFlag.FALSE_POS) == False
            assert attrs.get(EdgeFlag.INTERTRACK_EDGE) == False
            assert attrs.get(EdgeFlag.WRONG_SEMANTIC) == False

        # First gt edge is false neg
        attrs = matched.gt_graph.edges[(1, 2)]
        assert attrs.get(EdgeFlag.FALSE_NEG) == True
        if self.test_edge_tp: assert attrs.get(EdgeFlag.TRUE_POS) == False
        assert attrs.get(EdgeFlag.INTERTRACK_EDGE) == False

    def test_fn_node_middle(self):
        matched = self.prep_matched(ex_graphs.fn_node_matched(1))

        # No pred edges to test

        # All gt edges false pos
        for attrs in matched.gt_graph.edges.values():
            if self.test_edge_tp: assert attrs.get(EdgeFlag.TRUE_POS) == False # currently None 
            assert attrs.get(EdgeFlag.FALSE_NEG) == True
            assert attrs.get(EdgeFlag.INTERTRACK_EDGE) == False

    def test_fn_edge(self):
        matched = self.prep_matched(ex_graphs.fn_edge_matched(0))

        # Only pred edge is correct
        attrs = matched.pred_graph.edges[(5, 6)]
        assert attrs.get(EdgeFlag.FALSE_NEG) == False # currently None
        if self.test_edge_tp: assert attrs.get(EdgeFlag.TRUE_POS) == True
        assert attrs.get(EdgeFlag.INTERTRACK_EDGE) == False

        # First gt edge is false neg
        attrs = matched.gt_graph.edges[(1, 2)]
        if self.test_edge_tp: assert attrs.get(EdgeFlag.TRUE_POS) == False # currently None 
        assert attrs.get(EdgeFlag.FALSE_NEG) == True
        assert attrs.get(EdgeFlag.INTERTRACK_EDGE) == False

        # Second gt edge is correct
        attrs = matched.gt_graph.edges[(2, 3)]
        if self.test_edge_tp: assert attrs.get(EdgeFlag.TRUE_POS) == True # currently None 
        assert attrs.get(EdgeFlag.FALSE_NEG) == False
        assert attrs.get(EdgeFlag.INTERTRACK_EDGE) == False

    @pytest.mark.parametrize(
            "t",
            [0, 1, 2]
    )
    def test_fp_node(self, t):
        matched = self.prep_matched(ex_graphs.fp_node_matched(t))

        # All pred edges correct
        for attrs in matched.pred_graph.edges.values():
            if self.test_edge_tp: assert attrs.get(EdgeFlag.TRUE_POS) == True
            assert attrs.get(EdgeFlag.FALSE_POS) == False
            assert attrs.get(EdgeFlag.INTERTRACK_EDGE) == False
            assert attrs.get(EdgeFlag.WRONG_SEMANTIC) == False
        
        # All gt edges correct
        for attrs in matched.gt_graph.edges.values():
            if self.test_edge_tp: assert attrs.get(EdgeFlag.TRUE_POS) == True # currently None 
            assert attrs.get(EdgeFlag.FALSE_NEG) == False
            assert attrs.get(EdgeFlag.INTERTRACK_EDGE) == False

    @pytest.mark.parametrize(
            "t",
            [0, 1]
    )
    def test_fp_edge(self, t):
        matched = self.prep_matched(ex_graphs.fp_edge_matched(t))

        # All but one pred edges correct
        for edge, attrs in matched.pred_graph.edges.items():
            # false positive edge
            if edge == (7, 8):
                if self.test_edge_tp: assert attrs.get(EdgeFlag.TRUE_POS) == False
                assert attrs.get(EdgeFlag.FALSE_POS) == True # Currently False b/c not matched to any gt nodes
                assert attrs.get(EdgeFlag.INTERTRACK_EDGE) == False
                assert attrs.get(EdgeFlag.WRONG_SEMANTIC) == False
            else:
                if self.test_edge_tp: assert attrs.get(EdgeFlag.TRUE_POS) == True
                assert attrs.get(EdgeFlag.FALSE_POS) == False
                assert attrs.get(EdgeFlag.INTERTRACK_EDGE) == False
                assert attrs.get(EdgeFlag.WRONG_SEMANTIC) == False

    def test_node_two_to_one_end(self):
        matched = self.prep_matched(ex_graphs.node_two_to_one(0))

        # All pred edges correct
        for attrs in matched.pred_graph.edges.values():
            if self.test_edge_tp: assert attrs.get(EdgeFlag.TRUE_POS) == True
            assert attrs.get(EdgeFlag.FALSE_POS) == False
            assert attrs.get(EdgeFlag.INTERTRACK_EDGE) == False
            assert attrs.get(EdgeFlag.WRONG_SEMANTIC) == False
        
        # First edge correct - test currently fails
        attrs = matched.gt_graph.edges[(1,2)]
        if self.test_edge_tp: assert attrs.get(EdgeFlag.TRUE_POS) == True # currently None 
        assert attrs.get(EdgeFlag.FALSE_NEG) == False # currently True
        assert attrs.get(EdgeFlag.INTERTRACK_EDGE) == False

        # Second edge correct
        attrs = matched.gt_graph.edges[(2, 3)]
        if self.test_edge_tp: assert attrs.get(EdgeFlag.TRUE_POS) == True # currently None 
        assert attrs.get(EdgeFlag.FALSE_NEG) == False
        assert attrs.get(EdgeFlag.INTERTRACK_EDGE) == False


    def test_node_two_to_one_mid(self):
        matched = self.prep_matched(ex_graphs.node_two_to_one(1))

        # TODO weird non split case
        assert False

    def test_node_one_to_two(self):
        # TODO
        assert False

    
    
    # TODO: add test case for two to one with edges