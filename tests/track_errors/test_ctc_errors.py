import networkx as nx
import numpy as np
from traccuracy._tracking_graph import EdgeFlag, NodeFlag, TrackingGraph
from traccuracy.matchers import Matched
from traccuracy.track_errors._ctc import get_edge_errors, get_vertex_errors


def test_get_vertex_errors():
    comp_ids = [3, 7, 10]
    comp_ids_2 = list(np.asarray(comp_ids) + 1)
    gt_ids = [4, 12, 14, 17]
    gt_ids_2 = list(np.asarray(gt_ids) + 1)

    mapping = [(12, 3), (17, 3), (14, 7), (13, 8), (5, 11)]

    gt_g = nx.DiGraph()
    gt_g.add_nodes_from(gt_ids + gt_ids_2)
    nx.set_node_attributes(
        gt_g,
        {
            idx: {"t": 0, "segmentation_id": 1, "y": 0, "x": 0}
            for idx in gt_ids + gt_ids_2
        },
    )
    G_gt = TrackingGraph(gt_g)
    comp_g = nx.DiGraph()
    comp_g.add_nodes_from(comp_ids + comp_ids_2)
    nx.set_node_attributes(
        comp_g,
        {
            idx: {"t": 0, "segmentation_id": 1, "y": 0, "x": 0}
            for idx in comp_ids + comp_ids_2
        },
    )
    G_comp = TrackingGraph(comp_g)

    matched_data = Matched(G_gt, G_comp, mapping)

    get_vertex_errors(matched_data)

    assert len(matched_data.pred_graph.get_nodes_with_flag(NodeFlag.NON_SPLIT)) == 1
    assert len(matched_data.pred_graph.get_nodes_with_flag(NodeFlag.TRUE_POS)) == 3
    assert len(matched_data.pred_graph.get_nodes_with_flag(NodeFlag.FALSE_POS)) == 2
    assert len(matched_data.gt_graph.get_nodes_with_flag(NodeFlag.FALSE_NEG)) == 3

    assert matched_data.gt_graph.nodes[15][NodeFlag.FALSE_NEG]
    assert not matched_data.gt_graph.nodes[17][NodeFlag.FALSE_NEG]

    assert matched_data.pred_graph.nodes[3][NodeFlag.NON_SPLIT]
    assert not matched_data.pred_graph.nodes[7][NodeFlag.NON_SPLIT]

    assert matched_data.pred_graph.nodes[7][NodeFlag.TRUE_POS]
    assert not matched_data.pred_graph.nodes[3][NodeFlag.TRUE_POS]

    assert matched_data.pred_graph.nodes[10][NodeFlag.FALSE_POS]
    assert not matched_data.pred_graph.nodes[7][NodeFlag.FALSE_POS]


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

    matched_data = Matched(G_gt, G_comp, mapping)

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

    matched_data = Matched(TrackingGraph(gt), TrackingGraph(comp), mapping)

    get_edge_errors(matched_data)

    assert matched_data.pred_graph.edges[("1_2", "1_3")][EdgeFlag.WRONG_SEMANTIC]
