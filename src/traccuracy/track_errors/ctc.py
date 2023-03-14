from typing import TYPE_CHECKING

import networkx as nx
import numpy as np
from tqdm import tqdm

from traccuracy.track_errors.track_events import TrackEvents

if TYPE_CHECKING:
    from typing import Dict

    from traccuracy.tracking_graph import TrackingGraph


def evaluate_ctc_events(
    G_gt: "TrackingGraph", G_pred: "TrackingGraph", mapper, det_matrices
):
    gt_nx_graph = G_gt.graph
    pred_nx_graph = G_pred.graph
    node_errors = get_vertex_errors(gt_nx_graph, pred_nx_graph, det_matrices)
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
    gt_graph: "nx.Graph",
    comp_graph: "nx.Graph",
    detection_matrices: "Dict",
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
    detection_matrices : Dict
        Dictionary indexed by t holding `det`, `comp_ids` and `gt_ids`
    """
    tp_count = 0
    fp_count = 0
    fn_count = 0
    ns_count = 0

    nx.set_node_attributes(comp_graph, False, "is_tp")
    nx.set_node_attributes(comp_graph, False, "is_fp")
    nx.set_node_attributes(comp_graph, False, "is_ns")
    nx.set_node_attributes(gt_graph, False, "is_fn")

    fp_nodes = []
    fn_nodes = []
    ns_nodes = []

    for t in tqdm(sorted(detection_matrices.keys()), "Evaluating nodes"):
        mtrix = detection_matrices[t]["det"]
        comp_ids = detection_matrices[t]["comp_ids"]
        gt_ids = detection_matrices[t]["gt_ids"]

        tp_rows = np.ravel(np.argwhere(np.sum(mtrix, axis=1) == 1))
        fp_rows = np.ravel(np.argwhere(np.sum(mtrix, axis=1) == 0))
        fn_cols = np.ravel(np.argwhere(np.sum(mtrix, axis=0) == 0))
        ns_rows = np.ravel(np.argwhere(np.sum(mtrix, axis=1) > 1))

        for row in tp_rows:
            node_id = comp_ids[row]
            comp_graph.nodes[node_id]["is_tp"] = True

        for row in fp_rows:
            node_id = comp_ids[row]
            comp_graph.nodes[node_id]["is_fp"] = True
            fp_nodes.append(node_id)

        for col in fn_cols:
            node_id = gt_ids[col]
            gt_graph.nodes[node_id]["is_fn"] = True
            fn_nodes.append(node_id)

        # num operations needed to fix a non split vertex is
        # num reference markers matched to computed marker - 1
        for row in ns_rows:
            node_id = comp_ids[row]
            comp_graph.nodes[node_id]["is_ns"] = True
            number_of_splits = np.sum(mtrix[row]) - 1
            ns_count += number_of_splits
            ns_nodes.append(node_id)

        tp_count += len(tp_rows)
        fp_count += len(fp_rows)
        fn_count += len(fn_cols)

    error_counts = {
        "tp": tp_count,
        "fp": fp_count,
        "fn": fn_count,
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

    # fp edges - edges in induced_graph that aren't in gt_graph
    for edge in tqdm(induced_graph.edges, "Evaluating edges"):
        source, target = edge[0], edge[1]
        source_gt_id = list(filter(lambda mp: mp[1] == source, node_mapping))[0][0]
        target_gt_id = list(filter(lambda mp: mp[1] == target, node_mapping))[0][0]
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
    for edge in gt_graph.edges:
        source, target = edge[0], edge[1]
        # this edge is adjacent to an edge we didn't detect, so it definitely is an fn
        # TODO: assumes you've already assigned vertex errors...
        if gt_graph.nodes[source]["is_fn"] or gt_graph.nodes[target]["is_fn"]:
            gt_graph.edges[edge]["is_fn"] = True
            fn_edges.append(edge)
            continue

        source_comp_id = list(filter(lambda mp: mp[0] == source, node_mapping))[0][1]
        target_comp_id = list(filter(lambda mp: mp[0] == target, node_mapping))[0][1]
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
