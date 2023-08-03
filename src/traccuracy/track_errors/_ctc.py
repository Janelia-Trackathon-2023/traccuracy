from collections import defaultdict
from typing import TYPE_CHECKING

import numpy as np
import networkx as nx
from tqdm import tqdm

from ._track_events import TrackEvents

if TYPE_CHECKING:
    from typing import List, Tuple

    from traccuracy._tracking_graph import TrackingGraph


def evaluate_ctc_events(G_gt: "TrackingGraph", G_pred: "TrackingGraph", mapper):
    gt_nx_graph = G_gt.graph
    pred_nx_graph = G_pred.graph
    node_errors = get_vertex_errors(gt_nx_graph, pred_nx_graph, mapper)
    edge_errors = get_edge_errors(gt_nx_graph, pred_nx_graph, mapper)

    track_events = TrackEvents(
        fp_nodes=node_errors["fp_nodes"],
        fn_nodes=node_errors["fn_nodes"],
        fp_edges=edge_errors["fp_edges"],
        fn_edges=edge_errors["fn_edges"],
        nonsplit_vertices=node_errors["ns_nodes"],
        incorrect_semantics=edge_errors["ws_edges"],
    )
    return track_events


def get_vertex_errors(
    gt_graph: "nx.Graph", comp_graph: "nx.Graph", mapping: "List[Tuple[str, str]]"
):
    """Count vertex errors and assign class to each comp/gt node.

    Parameters
    ----------
    gt_graph : networkx.Graph
        Graph of ground truth tracking solution. Nodes must have label
        attribute denoting the pixel value of the marker.
    comp_graph : networkx.Graph
        Graph of computed tracking solution. Nodes must have label
        attribute denoting the pixel value of the marker.
    list[(gt_node, pred_node)]: list of tuples where each tuple contains a gt node
        and pred node
    """
    nx.set_node_attributes(comp_graph, False, "is_tp")
    nx.set_node_attributes(comp_graph, False, "is_ns")

    # will flip this when we come across the vertex in the mapping
    nx.set_node_attributes(comp_graph, True, "is_fp")
    nx.set_node_attributes(gt_graph, True, "is_fn")

    # we need to know how many computed vertices are "non-split", so we make
    # a mapping of gt vertices to their matched comp vertices
    dict_mapping = defaultdict(list)
    for gt_id, pred_id in mapping:
        dict_mapping[pred_id].append(gt_id)

    ns_count = 0
    for pred_id in tqdm(dict_mapping, desc="Evaluating nodes"):
        gt_ids = dict_mapping[pred_id]
        if len(gt_ids) == 1:
            gid = gt_ids[0]
            comp_graph.nodes[pred_id]["is_tp"] = True
            comp_graph.nodes[pred_id]["is_fp"] = False
            gt_graph.nodes[gid]["is_fn"] = False
        elif len(gt_ids) > 1:
            comp_graph.nodes[pred_id]["is_ns"] = True
            comp_graph.nodes[pred_id]["is_fp"] = False
            # number of split operations that would be required to correct the vertices
            ns_count += len(gt_ids) - 1
            for gid in gt_ids:
                gt_graph.nodes[gid]["is_fn"] = False

    tp_nodes: "List[str]" = []
    fp_nodes: "List[str]" = []
    ns_nodes: "List[str]" = []
    for nid in comp_graph.nodes:
        node = comp_graph.nodes[nid]
        if node["is_tp"]:
            tp_nodes.append(nid)
        elif node["is_fp"]:
            fp_nodes.append(nid)
        elif node["is_ns"]:
            ns_nodes.append(nid)
    fn_nodes = [node for node in gt_graph.nodes if gt_graph.nodes[node]["is_fn"]]

    error_counts = {
        "tp": len(tp_nodes),
        "fp": len(fp_nodes),
        "fn": len(fn_nodes),
        "ns": ns_count,
        "fp_nodes": fp_nodes,
        "fn_nodes": fn_nodes,
        "ns_nodes": ns_nodes,
    }
    return error_counts


def get_edge_errors(gt_graph, comp_graph, node_mapping):
    induced_graph = get_comp_subgraph(comp_graph)

    nx.set_edge_attributes(comp_graph, False, "is_fp")
    nx.set_edge_attributes(comp_graph, False, "is_tp")
    nx.set_edge_attributes(comp_graph, False, "is_wrong_semantic")
    nx.set_edge_attributes(gt_graph, False, "is_fn")

    fp_edges = []
    fn_edges = []
    ws_edges = []

    node_mapping_first = np.array([mp[0] for mp in node_mapping])
    node_mapping_second = np.array([mp[1] for mp in node_mapping])
    
    # fp edges - edges in induced_graph that aren't in gt_graph
    for edge in tqdm(induced_graph.edges, "Evaluating FP edges"):
        source, target = edge[0], edge[1]
        
        source_gt_id = node_mapping[np.where(node_mapping_second==source)[0][0]][0]
        target_gt_id = node_mapping[np.where(node_mapping_second==target)[0][0]][0]
        
        expected_gt_edge = (source_gt_id, target_gt_id)
        if expected_gt_edge not in gt_graph.edges:
            comp_graph.edges[edge]["is_fp"] = True
            fp_edges.append(edge)
        else:
            # check if semantics are correct
            is_parent_gt = gt_graph.edges[expected_gt_edge]["is_intertrack_edge"]
            is_parent_comp = comp_graph.edges[edge]["is_intertrack_edge"]
            if is_parent_gt != is_parent_comp:
                comp_graph.edges[edge]["is_wrong_semantic"] = True
                ws_edges.append(edge)
            else:
                comp_graph.edges[edge]["is_tp"] = True

    # fn edges - edges in gt_graph that aren't in induced graph
    for edge in tqdm(gt_graph.edges, "Evaluating FN edges"):
        source, target = edge[0], edge[1]
        # this edge is adjacent to an edge we didn't detect, so it definitely is an fn
        if gt_graph.nodes[source]["is_fn"] or gt_graph.nodes[target]["is_fn"]:
            gt_graph.edges[edge]["is_fn"] = True
            fn_edges.append(edge)
            continue

        source_comp_id = node_mapping[np.where(node_mapping_first==source)[0][0]][1]
        target_comp_id = node_mapping[np.where(node_mapping_first==target)[0][0]][1]
        
        expected_comp_edge = (source_comp_id, target_comp_id)
        if expected_comp_edge not in induced_graph.edges:
            gt_graph.edges[edge]["is_fn"] = True
            fn_edges.append(edge)

    return {"fp_edges": fp_edges, "fn_edges": fn_edges, "ws_edges": ws_edges}


def get_comp_subgraph(comp_graph: "nx.Graph") -> "nx.Graph":
    """Return computed graph subgraph of TP vertices and their incident edges.

    Parameters
    ----------
    comp_graph : networkx.Graph
        Graph of computed tracking solution. Nodes must have label
        attribute denoting the pixel value of the marker.

    Returns
    -------
    induced_graph : networkx.Graph
        Subgraph of comp_graph with only TP vertices and their incident edges
    """
    tp_nodes = [node for node in comp_graph.nodes if comp_graph.nodes[node]["is_tp"]]
    induced_graph = nx.DiGraph(comp_graph.subgraph(tp_nodes).copy())
    return induced_graph
