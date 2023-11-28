from __future__ import annotations

import logging
from collections import defaultdict
from typing import TYPE_CHECKING

from tqdm import tqdm

from traccuracy._tracking_graph import EdgeAttr, NodeAttr

if TYPE_CHECKING:
    from traccuracy.matchers import Matched

logger = logging.getLogger(__name__)


def evaluate_ctc_events(matched_data: Matched):
    """Annotates ground truth and predicted graph with node and edge error types

    Annotations are made in place
    """
    get_vertex_errors(matched_data)
    get_edge_errors(matched_data)


def get_vertex_errors(matched_data: Matched):
    """Count vertex errors and assign class to each comp/gt node.

    Parameters
    ----------
    matched_data: traccuracy.matchers.Matched
        Matched data object containing gt and pred graphs with their associated mapping
    """
    comp_graph = matched_data.pred_graph
    gt_graph = matched_data.gt_graph
    mapping = matched_data.mapping

    if comp_graph.node_errors and gt_graph.node_errors:
        logger.info("Node errors already calculated. Skipping graph annotation")
        return

    comp_graph.set_node_attribute(list(comp_graph.nodes()), NodeAttr.TRUE_POS, False)
    comp_graph.set_node_attribute(list(comp_graph.nodes()), NodeAttr.NON_SPLIT, False)

    # will flip this when we come across the vertex in the mapping
    comp_graph.set_node_attribute(list(comp_graph.nodes()), NodeAttr.FALSE_POS, True)
    gt_graph.set_node_attribute(list(gt_graph.nodes()), NodeAttr.FALSE_NEG, True)

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
            comp_graph.set_node_attribute(pred_id, NodeAttr.TRUE_POS, True)
            comp_graph.set_node_attribute(pred_id, NodeAttr.FALSE_POS, False)
            gt_graph.set_node_attribute(gid, NodeAttr.FALSE_NEG, False)
        elif len(gt_ids) > 1:
            comp_graph.set_node_attribute(pred_id, NodeAttr.NON_SPLIT, True)
            comp_graph.set_node_attribute(pred_id, NodeAttr.FALSE_POS, False)
            # number of split operations that would be required to correct the vertices
            ns_count += len(gt_ids) - 1
            gt_graph.set_node_attribute(gt_ids, NodeAttr.FALSE_NEG, False)

    # Record presence of annotations on the TrackingGraph
    comp_graph.node_errors = True
    gt_graph.node_errors = True


def get_edge_errors(matched_data: Matched):
    comp_graph = matched_data.pred_graph
    gt_graph = matched_data.gt_graph
    node_mapping = matched_data.mapping

    if comp_graph.edge_errors and gt_graph.edge_errors:
        logger.info("Edge errors already calculated. Skipping graph annotation")
        return

    # Node errors must already be annotated
    if not comp_graph.node_errors and not gt_graph.node_errors:
        logger.warning("Node errors have not been annotated. Running node annotation.")
        get_vertex_errors(matched_data)

    induced_graph = comp_graph.get_subgraph(
        comp_graph.get_nodes_with_flag(NodeAttr.TRUE_POS)
    ).graph

    comp_graph.set_edge_attribute(list(comp_graph.edges()), EdgeAttr.FALSE_POS, False)
    comp_graph.set_edge_attribute(
        list(comp_graph.edges()), EdgeAttr.WRONG_SEMANTIC, False
    )
    gt_graph.set_edge_attribute(list(gt_graph.edges()), EdgeAttr.FALSE_NEG, False)

    gt_comp_mapping = {gt: comp for gt, comp in node_mapping if comp in induced_graph}
    comp_gt_mapping = {comp: gt for gt, comp in node_mapping if comp in induced_graph}

    # intertrack edges = connection between parent and daughter
    for graph in [comp_graph, gt_graph]:
        # Set to False by default
        graph.set_edge_attribute(list(graph.edges()), EdgeAttr.INTERTRACK_EDGE, False)

        for parent in graph.get_divisions():
            for daughter in graph.get_succs(parent):
                graph.set_edge_attribute(
                    (parent, daughter), EdgeAttr.INTERTRACK_EDGE, True
                )

        for merge in graph.get_merges():
            for parent in graph.get_preds(merge):
                graph.set_edge_attribute(
                    (parent, merge), EdgeAttr.INTERTRACK_EDGE, True
                )

    # fp edges - edges in induced_graph that aren't in gt_graph
    for edge in tqdm(induced_graph.edges, "Evaluating FP edges"):
        source, target = edge[0], edge[1]

        source_gt_id = comp_gt_mapping[source]
        target_gt_id = comp_gt_mapping[target]

        expected_gt_edge = (source_gt_id, target_gt_id)
        if expected_gt_edge not in gt_graph.edges():
            comp_graph.set_edge_attribute(edge, EdgeAttr.FALSE_POS, True)
        else:
            # check if semantics are correct
            is_parent_gt = gt_graph.edges()[expected_gt_edge][EdgeAttr.INTERTRACK_EDGE]
            is_parent_comp = comp_graph.edges()[edge][EdgeAttr.INTERTRACK_EDGE]
            if is_parent_gt != is_parent_comp:
                comp_graph.set_edge_attribute(edge, EdgeAttr.WRONG_SEMANTIC, True)

    # fn edges - edges in gt_graph that aren't in induced graph
    for edge in tqdm(gt_graph.edges(), "Evaluating FN edges"):
        source, target = edge[0], edge[1]
        # this edge is adjacent to an edge we didn't detect, so it definitely is an fn
        if (
            gt_graph.nodes()[source][NodeAttr.FALSE_NEG]
            or gt_graph.nodes()[target][NodeAttr.FALSE_NEG]
        ):
            gt_graph.set_edge_attribute(edge, EdgeAttr.FALSE_NEG, True)
            continue

        source_comp_id = gt_comp_mapping[source]
        target_comp_id = gt_comp_mapping[target]

        expected_comp_edge = (source_comp_id, target_comp_id)
        if expected_comp_edge not in induced_graph.edges:
            gt_graph.set_edge_attribute(edge, EdgeAttr.FALSE_NEG, True)

    gt_graph.edge_errors = True
    comp_graph.edge_errors = True
