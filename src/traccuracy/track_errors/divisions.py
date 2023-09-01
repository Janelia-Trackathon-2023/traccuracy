import copy
import itertools
from collections import Counter

from traccuracy._tracking_graph import TrackingGraph
from traccuracy._utils import find_gt_node_matches, find_pred_node_matches


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

    for gt_node in div_gt:
        # Find possible matching nodes
        pred_node = _find_gt_node_matches(gt_node)
        # No matching node so division missed
        if pred_node is None:
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
                G_gt.set_node_attribute(gt_node, "is_tp_division", True)
                G_pred.set_node_attribute(pred_node, "is_tp_division", True)
            # If daughters are at all mismatched, division is false negative
            else:
                G_gt.set_node_attribute(gt_node, "is_fn_division", True)

        # Remove res division to record that we have classified it
        if pred_node in div_pred:
            div_pred.remove(pred_node)

    # Any remaining pred divisions are false positives
    G_pred.set_node_attribute(div_pred, "is_fp_division", True)

    return G_gt, G_pred


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

    Copies G_gt and G_pred before modifying node annotations and rteturns the new versions

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

    # Create copies of the graphs to modify during correction of divisions
    G_gt = copy.deepcopy(G_gt)
    G_pred = copy.deepcopy(G_pred)

    fp_divs = G_pred.get_nodes_with_attribute("is_fp_division")
    fn_divs = G_gt.get_nodes_with_attribute("is_fn_division")

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
            # Remove error annotations from pred graph
            G_pred.set_node_attribute(fp_node, "is_fp_division", False)
            G_gt.set_node_attribute(fn_node, "is_fn_division", False)

            # Add the tp divisions annotations
            G_gt.set_node_attribute(fn_node, "is_tp_division", True)
            G_pred.set_node_attribute(fp_node, "is_tp_division", True)

    return G_gt, G_pred


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

    div_annotations = {}

    # Baseline division classification
    G_gt, G_pred = _classify_divisions(G_gt, G_pred, mapper)
    div_annotations[0] = (G_gt, G_pred)

    # Correct shifted divisions for each nonzero value in frame_buffer
    for delta in frame_buffer:
        # Skip 0 because we used that in baseline classification
        if delta == 0:
            continue

        gg, gp = _correct_shifted_divisions(G_gt, G_pred, mapper, n_frames=delta)
        div_annotations[delta] = (gg, gp)

    return div_annotations
