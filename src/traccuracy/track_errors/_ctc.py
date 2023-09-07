from collections import defaultdict
from typing import TYPE_CHECKING

import numpy as np
from tqdm import tqdm

if TYPE_CHECKING:
    from traccuracy.matchers._matched import Matched


def evaluate_ctc_events(matched_data: "Matched"):
    """Annotates ground truth and predicted graph with node and edge error types

    Annotations are made in place
    """
    get_vertex_errors(matched_data)
    get_edge_errors(matched_data)


def get_vertex_errors(matched_data: "Matched"):
    """Count vertex errors and assign class to each comp/gt node.

    Parameters
    ----------
    matched_data: Matched
        Matched data object containing gt and pred graphs with their associated mapping
    """
    comp_graph = matched_data.pred_data.tracking_graph
    gt_graph = matched_data.gt_data.tracking_graph
    mapping = matched_data.mapping

    comp_graph.set_node_attribute(list(comp_graph.nodes()), "is_tp", False)
    comp_graph.set_node_attribute(list(comp_graph.nodes()), "is_ns", False)

    # will flip this when we come across the vertex in the mapping
    comp_graph.set_node_attribute(list(comp_graph.nodes()), "is_fp", True)
    gt_graph.set_node_attribute(list(gt_graph.nodes()), "is_fn", True)

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
            comp_graph.set_node_attribute(pred_id, "is_tp", True)
            comp_graph.set_node_attribute(pred_id, "is_fp", False)
            gt_graph.set_node_attribute(gid, "is_fn", False)
        elif len(gt_ids) > 1:
            comp_graph.set_node_attribute(pred_id, "is_ns", True)
            comp_graph.set_node_attribute(pred_id, "is_fp", False)
            # number of split operations that would be required to correct the vertices
            ns_count += len(gt_ids) - 1
            gt_graph.set_node_attribute(gt_ids, "is_fn", False)

    # Record presence of annotations on the TrackingGraph
    comp_graph.node_errors = True
    gt_graph.node_errors = True


def get_edge_errors(matched_data: "Matched"):
    comp_graph = matched_data.pred_data.tracking_graph
    gt_graph = matched_data.gt_data.tracking_graph
    node_mapping = matched_data.mapping

    induced_graph = comp_graph.get_subgraph(
        comp_graph.get_nodes_with_attribute("is_tp", criterion=lambda x: x)
    ).graph

    comp_graph.set_edge_attribute(list(comp_graph.edges()), "is_fp", False)
    comp_graph.set_edge_attribute(list(comp_graph.edges()), "is_tp", False)
    comp_graph.set_edge_attribute(list(comp_graph.edges()), "is_wrong_semantic", False)
    gt_graph.set_edge_attribute(list(gt_graph.edges()), "is_fn", False)

    node_mapping_first = np.array([mp[0] for mp in node_mapping])
    node_mapping_second = np.array([mp[1] for mp in node_mapping])

    # fp edges - edges in induced_graph that aren't in gt_graph
    for edge in tqdm(induced_graph.edges, "Evaluating FP edges"):
        source, target = edge[0], edge[1]

        source_gt_id = node_mapping[np.where(node_mapping_second == source)[0][0]][0]
        target_gt_id = node_mapping[np.where(node_mapping_second == target)[0][0]][0]

        expected_gt_edge = (source_gt_id, target_gt_id)
        if expected_gt_edge not in gt_graph.edges():
            comp_graph.set_edge_attribute(edge, "is_fp", True)
        else:
            # check if semantics are correct
            is_parent_gt = gt_graph.edges()[expected_gt_edge]["is_intertrack_edge"]
            is_parent_comp = comp_graph.edges()[edge]["is_intertrack_edge"]
            if is_parent_gt != is_parent_comp:
                comp_graph.set_edge_attribute(edge, "is_wrong_semantic", True)
            else:
                comp_graph.set_edge_attribute(edge, "is_tp", True)

    # fn edges - edges in gt_graph that aren't in induced graph
    for edge in tqdm(gt_graph.edges(), "Evaluating FN edges"):
        source, target = edge[0], edge[1]
        # this edge is adjacent to an edge we didn't detect, so it definitely is an fn
        if gt_graph.nodes()[source]["is_fn"] or gt_graph.nodes()[target]["is_fn"]:
            gt_graph.set_edge_attribute(edge, "is_fn", True)
            continue

        source_comp_id = node_mapping[np.where(node_mapping_first == source)[0][0]][1]
        target_comp_id = node_mapping[np.where(node_mapping_first == target)[0][0]][1]

        expected_comp_edge = (source_comp_id, target_comp_id)
        if expected_comp_edge not in induced_graph.edges:
            gt_graph.set_edge_attribute(edge, "is_fn", True)

    gt_graph.edge_errors = True
    comp_graph.edge_errors = True
