"""This submodule classifies division erros in tracking graphs

Each division is classifed as one of the following:
- true positive
- false positive
- false negative

These functions require two `TrackingGraph` objects and a mapper between
nodes in the two graphs. Divisions are identified as correct if both the parent
and daughter nodes match between the GT and predicted graph.

Temporal tolerance for correct divisions is implemented to allow for cases in
which the exact frame that a division event occurs is somewhat arbitrary due to
a high frame rate or variable segmentation or detection. Consider the following
graphs as an example::
    G1
                                2_4
    1_0 -- 1_1 -- 1_2 -- 1_3 -<
                                3_4
    G2
                  2_2 -- 2_3 -- 2_4
    1_0 -- 1_1 -<
                  3_2 -- 3_3 -- 3_4

After classifying basic division errors, we consider all false positive and false
negative divisions. If a pair of errors occurs within the specified frame buffer,
the pair is considered a true positive division if the parent nodes and daughter
nodes match. We determine the "parent node" of the late division, e.g. node 1_3 in
graph G1, by traversing back along the graph until we find the node in the same frame
as the parent node of the early division. We repeat the process for finding daughters
of the early division, by advancing along the graph to find nodes in the same frame
as the late division daughters.
"""

import itertools
from collections import Counter

from ..track_errors.division_events import DivisionEvents
from ..tracking_graph import TrackingGraph
from ..utils import find_gt_node_matches, find_pred_node_matches
from .base import Metric


def _calculate_metrics(event: DivisionEvents):
    try:
        recall = event.tp_division_count / (
            event.tp_division_count + event.fn_division_count
        )
    except ZeroDivisionError:
        recall = 0

    try:
        precision = event.tp_division_count / (
            event.tp_division_count + event.fp_division_count
        )
    except ZeroDivisionError:
        precision = 0

    try:
        f1 = 2 * (recall * precision) / (recall + precision)
    except ZeroDivisionError:
        f1 = 0

    try:
        mbc = event.tp_division_count / (
            event.tp_division_count + event.fn_division_count + event.fp_division_count
        )
    except ZeroDivisionError:
        mbc = 0

    return {
        "Division Recall": recall,
        "Division Precision": precision,
        "Division F1": f1,
        "Mitotic Branching Correctness": mbc,
        **event.count_dict,
    }


class DivisionMetrics(Metric):
    needs_one_to_one = True

    def __init__(self, matched_data, frame_buffer=(0)):
        """Classify division events and provide summary metrics

        Args:
            matched_data (Matched): Matched object for set of GT and Pred data
                Must meet the `needs_one_to_one` critera
            frame_buffer (tuple(int), optional): Tuple of integers. Value used as n_frames
                to tolerate in correct_shifted_divisions. Defaults to (0).
        """
        self.frame_buffer = frame_buffer
        super().__init__(matched_data)

    def compute(self):
        """Runs `_evalute_division_events` and calculates summary metrics for each frame buffer

        Returns:
            dict: Returns a nested dictionary with one dictionary per frame buffer value
        """
        events = _evaluate_division_events(
            self.data.gt_data.tracking_graph,
            self.data.pred_data.tracking_graph,
            self.data.mapping,
            frame_buffer=self.frame_buffer,
        )

        return {
            f"Frame Buffer {event.frame_buffer}": _calculate_metrics(event)
            for event in events
        }


def _classify_divisions(G_gt, G_pred, mapper):
    """Identify each division as a true positive, false positive or false negative

    This function only works on node mappers that are one-to-one

    Args:
        G_gt (TrackingGraph): `TrackingGraph` of GT data
        G_pred (TrackingGraph): `TrackingGraph` of pred data
        mapper ([(gt_node, pred_node)]): List of tuples with pairs of gt and pred nodes

    Raises:
        TypeError: G_gt and G_pred must be TrackingGraph objects
        ValueError: mapper must contain a one-to-one mapping of nodes

    Returns:
        DivisionEvents: Counts of gt_divisions, tp_divisions, fp_divisions and fn_divisions
        TrackingGraph: G_gt with division annotations
        TrackingGraph: G_pred with division annotations
    """
    if not isinstance(G_gt, TrackingGraph) or not isinstance(G_pred, TrackingGraph):
        raise TypeError("G_gt and G_pred must be TrackingGraph objects")

    # Check that mapper is one to one
    if len(mapper) != len({pair[0] for pair in mapper}) or len(mapper) != len(
        {pair[1] for pair in mapper}
    ):
        raise ValueError("Mapping must be one-to-one")

    def _find_gt_node_matches(gt_node):
        match = find_gt_node_matches(mapper, gt_node)
        if len(match) > 0:
            return match[0]

    def _find_pred_node_matches(pred_node):
        match = find_pred_node_matches(mapper, pred_node)
        if len(match) > 0:
            return match[0]

    # Collect list of divisions
    div_gt = G_gt.get_divisions()
    div_pred = G_pred.get_divisions()

    counts = DivisionEvents()
    counts.gt_divisions.extend(div_gt)

    for gt_node in div_gt:
        # Find possible matching nodes
        pred_node = _find_gt_node_matches(gt_node)
        # No matching node so division missed
        if pred_node is None:
            counts.fn_divisions.append(gt_node)
            G_gt.set_node_attribute(gt_node, "is_fn_division", True)
        # Check if the division has the corret daughters
        else:
            succ_gt = G_gt.get_succs(gt_node)
            # Map pred succ nodes onto gt, unmapped nodes will return as None
            succ_pred = [
                _find_pred_node_matches(n) for n in G_pred.get_succs(pred_node)
            ]

            # If daughters are same, division is correct
            if Counter(succ_gt) == Counter(succ_pred):
                counts.tp_divisions.append(gt_node)
                G_gt.set_node_attribute(gt_node, "is_tp_division", True)
                G_pred.set_node_attribute(pred_node, "is_tp_division", True)
            # If daughters are at all mismatched, division is false negative
            else:
                counts.fn_divisions.append(gt_node)
                G_gt.set_node_attribute(gt_node, "is_fn_division", True)

        # Remove res division to record that we have classified it
        if pred_node in div_pred:
            div_pred.remove(pred_node)

    # Any remaining pred divisions are false positives
    counts.fp_divisions.extend(div_pred)
    G_pred.set_node_attribute(div_pred, "is_fp_division", True)

    return counts, G_gt, G_pred


def _get_pred_by_t(G, node, delta_frames):
    """For a given graph and node, traverses back by predecessor until target_frame

    Args:
        G (TrackingGraph): TrackingGraph to search on
        node (hashable): Key of starting node
        target_frame (int): Frame of the predecessor target node

    Raises:
        ValueError: Cannot operate on graphs with merges

    Returns:
        hashable: Node key of predecessor in target frame
    """
    for _ in range(delta_frames):
        nodes = G.get_preds(node)
        # Exit if there are no predecessors
        if len(nodes) == 0:
            return None
        # Fail if finding merges
        elif len(nodes) > 1:
            raise ValueError("Cannot operate on graphs with merges")
        node = nodes[0]

    return node


def _get_succ_by_t(G, node, delta_frames):
    """For a given node, find the successors after delta frames

    If a division event is discovered, returns None

    Args:
        G (TrackingGraph): TrackingGraph to search on
        node (hashable): Key of starting node
        target_frame (int): Frame of the successor target node

    Returns:
        hashable: Node id of successor
    """
    for _ in range(delta_frames):
        nodes = G.get_succs(node)
        # Exit if there are no successors another division
        if len(nodes) == 0 or len(nodes) >= 2:
            return None
        node = nodes[0]

    return node


def _correct_shifted_divisions(G_gt, G_pred, mapper, n_frames=1):
    """Allows for divisions to occur within a frame buffer and still be correct

    This implementation asserts that the parent lineages and daughter lineages must match.
    Matching is determined based on the provided mapper
    Does not support merges

    Args:
        G_gt (TrackingGraph): GT tracking graph with FN division annotations
        G_pred (TrackningGraph): Pred tracking graph with FP division annotations
        mapper ([(gt_node, pred_node)]): List of tuples with pairs of gt and pred nodes
            Must be a one-to-one mapping
        n_frames (int): Number of frames to include in the frame buffer

    Returns:
        DivisionEvents: Corrected counts of gt_divisions, tp_divisions, fp_divisions
            and fn_divisions
    """

    if not isinstance(G_gt, TrackingGraph) or not isinstance(G_pred, TrackingGraph):
        raise TypeError("G_gt and G_pred must be TrackingGraph objects")

    # Check that mapper is one to one
    if len(mapper) != len({pair[0] for pair in mapper}) or len(mapper) != len(
        {pair[1] for pair in mapper}
    ):
        raise ValueError("Mapping must be one-to-one")

    fp_divs = G_pred.get_nodes_with_attribute("is_fp_division")
    fn_divs = G_gt.get_nodes_with_attribute("is_fn_division")

    # Create counts object for collecting error classifications
    counts = DivisionEvents(
        gt_divisions=G_gt.get_divisions(),
        fp_divisions=fp_divs,
        fn_divisions=fn_divs,
        tp_divisions=G_gt.get_nodes_with_attribute("is_tp_division"),
        frame_buffer=n_frames,
    )

    # Compare all pairs of fp and fn
    for fp_node, fn_node in itertools.product(fp_divs, fn_divs):
        correct = False
        t_fp = G_pred.graph.nodes[fp_node][G_pred.frame_key]
        t_fn = G_gt.graph.nodes[fn_node][G_gt.frame_key]

        # Move on if nodes are not within frame buffer or within same frame
        if abs(t_fp - t_fn) > n_frames or t_fp == t_fn:
            continue

        # False positive in pred occurs before false negative in gt
        if t_fp < t_fn:
            # Check if fp node matches prececessor of fn
            fn_pred = _get_pred_by_t(G_gt, fn_node, t_fn - t_fp)
            # Check if the match exists
            if (fn_pred, fp_node) not in mapper:
                # Match does not exist so divisions cannot match
                continue

            # Check if daughters match
            fp_succ = [
                _get_succ_by_t(G_pred, node, t_fn - t_fp)
                for node in G_pred.get_succs(fp_node)
            ]
            fn_succ = G_gt.get_succs(fn_node)
            if Counter(fp_succ) != Counter(fn_succ):
                # Daughters don't match so division cannot match
                continue

            # At this point daughters and parents match so division is correct
            correct = True
        # False negative in gt occurs before false positive in pred
        else:
            # Check if fp node matches fn predecessor
            fp_pred = _get_pred_by_t(G_pred, fp_node, t_fp - t_fn)
            # Check if match exists
            if (fn_node, fp_pred) not in mapper:
                # Match does not exist so divisions cannot match
                continue

            # Check if daughters match
            fn_succ = [
                _get_succ_by_t(G_gt, node, t_fp - t_fn)
                for node in G_gt.get_succs(fn_node)
            ]
            fp_succ = G_pred.get_succs(fp_node)
            if Counter(fp_succ) != Counter(fn_succ):
                # Daughters don't match so division cannot match
                continue

            # At this point daughters and parents match so division is correct
            correct = True

        if correct:
            # Remove node from error lists
            counts.fp_divisions.remove(fp_node)
            counts.fn_divisions.remove(fn_node)

            # Add gt node to tp list
            counts.tp_divisions.append(fn_node)

    return counts


def _evaluate_division_events(G_gt, G_pred, mapper, frame_buffer=(0)):
    """Classify division errors and correct shifted divisions according to frame_buffer
    One DivisionEvent object will be returned for each value in frame_buffer

    Args:
        G_gt (TrackingGraph): TrackingGraph of GT data
        G_pred (TrackingGraph): TrackingGraph of pred data
        mapper ([(gt_node, pred_node)]): List of tuples with pairs of gt and pred nodes
        frame_buffer (tuple, optional): Tuple of integers. Value used as n_frames
            to tolerate in correct_shifted_divisions. Defaults to (0).

    Returns:
        list[DivisionEvents]: List of one DivisionEvent object per value in frame_buffer
    """

    events = []

    # Baseline division classification
    event, G_gt, G_pred = _classify_divisions(G_gt, G_pred, mapper)
    events.append(event)

    # Correct shifted divisions for each nonzero value in frame_buffer
    for delta in frame_buffer:
        # Skip 0 because we used that in baseline classification
        if delta == 0:
            continue

        event = _correct_shifted_divisions(G_gt, G_pred, mapper, n_frames=delta)
        events.append(event)

    return events
