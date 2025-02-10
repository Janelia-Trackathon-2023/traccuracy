import pytest

import tests.examples.graphs as ex_graphs
from traccuracy._tracking_graph import EdgeFlag, NodeFlag
from traccuracy.track_errors.basic import _classify_edges, _classify_nodes


class TestStandardNode:

    def test_empty_gt(self):
        matched = ex_graphs.empty_gt()
        _classify_nodes(matched)

        # no gt = all false pos
        for attrs in matched.pred_graph.nodes.values():
            assert NodeFlag.FALSE_POS in attrs

    def test_empty_pred(self):
        matched = ex_graphs.empty_pred()
        _classify_nodes(matched)

        # no pred = all false neg
        for attrs in matched.gt_graph.nodes.values():
            assert NodeFlag.FALSE_NEG in attrs

    def test_good_match(self, caplog):
        matched = ex_graphs.good_matched()
        _classify_nodes(matched)

        # All TP
        for graph in [matched.gt_graph, matched.pred_graph]:
            for attrs in graph.nodes.values():
                assert NodeFlag.TRUE_POS in attrs

        # Check that it doesn't run a second time
        _classify_nodes(matched)
        assert (
            "Node errors already calculated. Skipping graph annotation" in caplog.text
        )

    @pytest.mark.parametrize("t", [0, 1, 2])
    def test_fn_node(self, t):
        wrong_node = [1, 2, 3][t]
        matched = ex_graphs.fn_node_matched(t)
        _classify_nodes(matched)

        # Missing pred node = false neg in gt
        for node, attrs in matched.gt_graph.nodes.items():
            if node == wrong_node:
                assert NodeFlag.FALSE_NEG in attrs
            else:
                assert NodeFlag.TRUE_POS in attrs

        # Pred graph all correct
        for attrs in matched.pred_graph.nodes.values():
            assert NodeFlag.TRUE_POS in attrs

    @pytest.mark.parametrize("edge_er", [0, 1])
    def test_fn_edge(self, edge_er):
        matched = ex_graphs.fn_edge_matched(edge_er)
        _classify_nodes(matched)

        # All nodes correct in both
        for graph in [matched.gt_graph, matched.pred_graph]:
            for attrs in graph.nodes.values():
                assert NodeFlag.TRUE_POS in attrs

    @pytest.mark.parametrize("t", [0, 1, 2])
    def test_fp_node(self, t):
        matched = ex_graphs.fp_node_matched(t)
        _classify_nodes(matched)

        # FP in pred, all others correct
        for node, attrs in matched.pred_graph.nodes.items():
            if node == 7:
                assert NodeFlag.FALSE_POS in attrs
            else:
                assert NodeFlag.TRUE_POS in attrs

        # All gt correct
        for attrs in matched.gt_graph.nodes.values():
            assert NodeFlag.TRUE_POS in attrs

    @pytest.mark.parametrize("edge_er", [0, 1])
    def test_fp_edge(self, edge_er):
        matched = ex_graphs.fp_edge_matched(edge_er)
        _classify_nodes(matched)

        # Two fp nodes in pred = 7 and 8
        for node, attrs in matched.pred_graph.nodes.items():
            if node in {7, 8}:
                assert NodeFlag.FALSE_POS in attrs
            else:
                assert NodeFlag.TRUE_POS in attrs

        # All gt correct
        for attrs in matched.gt_graph.nodes.values():
            assert NodeFlag.TRUE_POS in attrs

    def test_crossover(self):
        matched = ex_graphs.crossover_edge()
        _classify_nodes(matched)

        # All pred correct
        for attrs in matched.pred_graph.nodes.values():
            assert NodeFlag.TRUE_POS in attrs

        # Subset of gt are correct
        for node in [2, 3, 4]:
            assert NodeFlag.TRUE_POS in matched.gt_graph.nodes[node]
        for node in [1, 5, 6]:
            assert NodeFlag.FALSE_NEG in matched.gt_graph.nodes[node]

    # Skipping the following cases because they are not one to one
    # ex_graphs.node_two_to_one
    # ex_graphs.edge_two_to_one
    # ex_graphs.node_one_to_two
    # ex_graphs.edge_one_to_two


class TestStandardEdge:

    def test_empty_gt(self):
        matched = ex_graphs.empty_gt()
        _classify_edges(matched)

        # All fp edges
        for attrs in matched.pred_graph.edges.values():
            assert EdgeFlag.FALSE_POS in attrs

    def test_empty_pred(self):
        matched = ex_graphs.empty_pred()
        _classify_edges(matched)

        # all false neg
        for attrs in matched.gt_graph.edges.values():
            assert EdgeFlag.FALSE_NEG in attrs

    def test_good_match(self, caplog):
        matched = ex_graphs.good_matched()
        _classify_edges(matched)

        for graph in [matched.gt_graph, matched.pred_graph]:
            for attrs in graph.edges.values():
                assert EdgeFlag.TRUE_POS in attrs

        # Check that it doesn't run a second time
        _classify_edges(matched)
        assert (
            "Edge errors already calculated. Skipping graph annotation" in caplog.text
        )

    def test_fn_node_end(self):
        matched = ex_graphs.fn_node_matched(0)
        _classify_edges(matched)

        # All pred edges correct
        for attrs in matched.pred_graph.edges.values():
            assert EdgeFlag.TRUE_POS in attrs

        # First gt edge is false neg
        for edge, attrs in matched.gt_graph.edges.items():
            if edge == (1, 2):
                assert EdgeFlag.FALSE_NEG in attrs
            else:
                assert EdgeFlag.TRUE_POS in attrs

    def test_fn_node_middle(self):
        matched = ex_graphs.fn_node_matched(1)
        _classify_edges(matched)

        # all gt edges false neg
        for attrs in matched.gt_graph.edges.values():
            assert EdgeFlag.FALSE_NEG in attrs

    def test_fn_edge(self):
        matched = ex_graphs.fn_edge_matched(0)
        _classify_edges(matched)

        # Only pred edge is correct
        attrs = matched.pred_graph.edges[(5, 6)]
        assert EdgeFlag.TRUE_POS in attrs

        # First gt edge is false neg
        attrs = matched.gt_graph.edges[(1, 2)]
        assert EdgeFlag.FALSE_NEG in attrs

        # Second gt edge is correct
        attrs = matched.gt_graph.edges[(2, 3)]
        assert EdgeFlag.TRUE_POS in attrs

    @pytest.mark.parametrize("t", [0, 1, 2])
    def test_fp_node(self, t):
        matched = ex_graphs.fp_node_matched(t)
        _classify_edges(matched)

        # All pred and gt edges correct
        for graph in [matched.gt_graph, matched.pred_graph]:
            for attrs in graph.edges.values():
                assert EdgeFlag.TRUE_POS in attrs

    @pytest.mark.parametrize("t", [0, 1])
    def test_fp_edge(self, t):
        matched = ex_graphs.fp_edge_matched(t)
        _classify_edges(matched)

        # All gt and pred edges correct except for fp edge
        for graph in [matched.gt_graph, matched.pred_graph]:
            for edge, attrs in graph.edges.items():
                if edge == (7, 8):
                    assert EdgeFlag.FALSE_POS in attrs
                else:
                    assert EdgeFlag.TRUE_POS in attrs

    def test_crossover_edge(self):
        matched = ex_graphs.crossover_edge()
        _classify_edges(matched)

        # One pred edge correct other fp
        attrs = matched.pred_graph.edges[(7, 8)]
        assert EdgeFlag.FALSE_POS in attrs
        attrs = matched.pred_graph.edges[(8, 9)]
        assert EdgeFlag.TRUE_POS in attrs

        # All but one gt edge correct
        for edge, attrs in matched.gt_graph.edges.items():
            if edge == (2, 3):
                assert EdgeFlag.TRUE_POS in attrs
            else:
                assert EdgeFlag.FALSE_NEG in attrs

    # Skipping the following cases because they are not one to one
    # ex_graphs.node_two_to_one
    # ex_graphs.edge_two_to_one
    # ex_graphs.node_one_to_two
    # ex_graphs.edge_one_to_two
