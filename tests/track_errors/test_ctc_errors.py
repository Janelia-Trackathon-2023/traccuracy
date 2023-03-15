import networkx as nx
import numpy as np
from traccuracy.track_errors._ctc import (
    get_comp_subgraph,
    get_edge_errors,
    get_vertex_errors,
)


def test_get_vertex_errors():
    comp_ids = [3, 7, 10]
    comp_ids_2 = list(np.asarray(comp_ids) + 1)
    gt_ids = [4, 12, 14, 17]
    gt_ids_2 = list(np.asarray(gt_ids) + 1)

    mtrix = np.zeros((3, 4), dtype=np.uint8)
    mtrix[0, 1] = 1
    mtrix[0, 3] = 1
    mtrix[1, 2] = 1

    mtrix2 = np.zeros((3, 4), dtype=np.uint8)
    mtrix2[1, 1] = 1
    mtrix2[2, 0] = 1
    mtrix_dict = {
        0: {"det": mtrix, "comp_ids": comp_ids, "gt_ids": gt_ids},
        1: {"det": mtrix2, "comp_ids": comp_ids_2, "gt_ids": gt_ids_2},
    }
    gt_g = nx.DiGraph()
    gt_g.add_nodes_from(gt_ids + gt_ids_2)
    comp_g = nx.DiGraph()
    comp_g.add_nodes_from(comp_ids + comp_ids_2)

    vertex_errors = get_vertex_errors(gt_g, comp_g, mtrix_dict)
    assert vertex_errors["ns"] == 1
    assert vertex_errors["tp"] == 3
    assert vertex_errors["fp"] == 2
    assert vertex_errors["fn"] == 3

    assert gt_g.nodes[15]["is_fn"]
    assert not gt_g.nodes[17]["is_fn"]

    assert comp_g.nodes[3]["is_ns"]
    assert not comp_g.nodes[7]["is_ns"]

    assert comp_g.nodes[7]["is_tp"]
    assert not comp_g.nodes[3]["is_tp"]

    assert comp_g.nodes[10]["is_fp"]
    assert not comp_g.nodes[7]["is_fp"]


def test_get_comp_subgraph():
    comp_ids = [3, 7, 10]
    comp_ids_2 = list(np.asarray(comp_ids) + 1)

    comp_g = nx.DiGraph()
    comp_g.add_nodes_from(comp_ids + comp_ids_2)
    nx.set_node_attributes(comp_g, False, "is_tp")
    comp_g.nodes[7]["is_tp"] = True
    comp_g.nodes[8]["is_tp"] = True
    comp_g.nodes[11]["is_tp"] = True
    comp_g.add_edge(3, 4)
    comp_g.add_edge(7, 11)

    induced_graph = get_comp_subgraph(comp_g)
    assert sorted(induced_graph.nodes) == [7, 8, 11]
    assert list(induced_graph.edges) == [(7, 11)]


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
    nx.set_node_attributes(comp_g, True, "is_tp")
    nx.set_edge_attributes(comp_g, 0, "is_intertrack_edge")

    gt_edges = [(4, 5), (17, 18)]
    gt_g = nx.DiGraph()
    gt_g.add_nodes_from(gt_ids)
    gt_g.add_edges_from(gt_edges)
    nx.set_edge_attributes(gt_g, 0, "is_intertrack_edge")
    nx.set_node_attributes(gt_g, False, "is_fn")
    get_edge_errors(gt_g, comp_g, mapping)

    assert comp_g.edges[(3, 4)]["is_tp"]
    assert comp_g.edges[(7, 8)]["is_fp"]
    assert gt_g.edges[(17, 18)]["is_fn"]


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
    nx.set_node_attributes(comp_g, True, "is_tp")
    nx.set_edge_attributes(comp_g, 0, "is_intertrack_edge")

    gt_edges = [(4, 5), (17, 18)]
    gt_g = nx.DiGraph()
    gt_g.add_nodes_from(gt_ids)
    gt_g.add_edges_from(gt_edges)
    nx.set_edge_attributes(gt_g, 0, "is_intertrack_edge")
    nx.set_node_attributes(gt_g, False, "is_fn")
    gt_g.edges[(4, 5)]["is_intertrack_edge"] = 1
    get_edge_errors(gt_g, comp_g, mapping)

    assert comp_g.edges[(3, 4)]["is_wrong_semantic"]
    assert not comp_g.edges[(3, 4)]["is_tp"]
