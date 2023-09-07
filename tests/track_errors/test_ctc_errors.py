import networkx as nx
import numpy as np
from traccuracy._tracking_data import TrackingData
from traccuracy._tracking_graph import EdgeAttr, NodeAttr, TrackingGraph
from traccuracy.matchers._matched import Matched
from traccuracy.track_errors._ctc import (
    get_edge_errors,
    get_vertex_errors,
)


class DummyMatched(Matched):
    def compute_mapping(self):
        return []


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

    matched_data = DummyMatched(TrackingData(G_gt), TrackingData(G_comp))
    matched_data.mapping = mapping

    get_vertex_errors(matched_data)

    assert len(G_comp.get_nodes_with_attribute(NodeAttr.NON_SPLIT, lambda x: x)) == 1
    assert len(G_comp.get_nodes_with_attribute(NodeAttr.TRUE_POS, lambda x: x)) == 3
    assert len(G_comp.get_nodes_with_attribute(NodeAttr.FALSE_POS, lambda x: x)) == 2
    assert len(G_gt.get_nodes_with_attribute(NodeAttr.FALSE_NEG, lambda x: x)) == 3

    assert gt_g.nodes[15][NodeAttr.FALSE_NEG]
    assert not gt_g.nodes[17][NodeAttr.FALSE_NEG]

    assert comp_g.nodes[3][NodeAttr.NON_SPLIT]
    assert not comp_g.nodes[7][NodeAttr.NON_SPLIT]

    assert comp_g.nodes[7][NodeAttr.TRUE_POS]
    assert not comp_g.nodes[3][NodeAttr.TRUE_POS]

    assert comp_g.nodes[10][NodeAttr.FALSE_POS]
    assert not comp_g.nodes[7][NodeAttr.FALSE_POS]


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
    nx.set_node_attributes(comp_g, True, NodeAttr.TRUE_POS)
    nx.set_edge_attributes(comp_g, 0, EdgeAttr.INTERTRACK_EDGE)
    nx.set_node_attributes(
        comp_g,
        {idx: {"t": 0, "segmentation_id": 1, "y": 0, "x": 0} for idx in comp_ids},
    )
    G_comp = TrackingGraph(comp_g)

    gt_edges = [(4, 5), (17, 18)]
    gt_g = nx.DiGraph()
    gt_g.add_nodes_from(gt_ids)
    gt_g.add_edges_from(gt_edges)
    nx.set_edge_attributes(gt_g, 0, EdgeAttr.INTERTRACK_EDGE)
    nx.set_node_attributes(gt_g, False, NodeAttr.FALSE_NEG)
    nx.set_node_attributes(
        gt_g, {idx: {"t": 0, "segmentation_id": 1, "y": 0, "x": 0} for idx in gt_ids}
    )
    G_gt = TrackingGraph(gt_g)

    matched_data = DummyMatched(TrackingData(G_gt), TrackingData(G_comp))
    matched_data.mapping = mapping

    get_edge_errors(matched_data)

    assert comp_g.edges[(3, 4)][EdgeAttr.TRUE_POS]
    assert comp_g.edges[(7, 8)][EdgeAttr.FALSE_POS]
    assert gt_g.edges[(17, 18)][EdgeAttr.FALSE_NEG]


def test_assign_edge_errors_semantics():
    comp_ids = [3, 7, 10]
    comp_ids_2 = list(np.asarray(comp_ids) + 1)
    comp_ids += comp_ids_2

    gt_ids = [4, 12, 17]
    gt_ids_2 = list(np.asarray(gt_ids) + 1)
    gt_ids += gt_ids_2

    mapping = [(4, 3), (12, 7), (17, 10), (5, 4), (18, 11), (13, 8)]

    # need a tp, fp, fn
    comp_edges = [(3, 4)]
    comp_g = nx.DiGraph()
    comp_g.add_nodes_from(comp_ids)
    comp_g.add_edges_from(comp_edges)
    nx.set_node_attributes(comp_g, True, NodeAttr.TRUE_POS)
    nx.set_edge_attributes(comp_g, 0, EdgeAttr.INTERTRACK_EDGE)
    nx.set_node_attributes(
        comp_g,
        {idx: {"t": 0, "segmentation_id": 1, "y": 0, "x": 0} for idx in comp_ids},
    )
    G_comp = TrackingGraph(comp_g)

    gt_edges = [(4, 5), (17, 18)]
    gt_g = nx.DiGraph()
    gt_g.add_nodes_from(gt_ids)
    gt_g.add_edges_from(gt_edges)
    nx.set_edge_attributes(gt_g, 0, EdgeAttr.INTERTRACK_EDGE)
    nx.set_node_attributes(gt_g, False, NodeAttr.FALSE_NEG)
    gt_g.edges[(4, 5)][EdgeAttr.INTERTRACK_EDGE] = 1
    nx.set_node_attributes(
        gt_g, {idx: {"t": 0, "segmentation_id": 1, "y": 0, "x": 0} for idx in gt_ids}
    )
    G_gt = TrackingGraph(gt_g)

    matched_data = DummyMatched(TrackingData(G_gt), TrackingData(G_comp))
    matched_data.mapping = mapping

    get_edge_errors(matched_data)

    assert comp_g.edges[(3, 4)][EdgeAttr.WRONG_SEMANTIC]
    assert not comp_g.edges[(3, 4)][EdgeAttr.TRUE_POS]
