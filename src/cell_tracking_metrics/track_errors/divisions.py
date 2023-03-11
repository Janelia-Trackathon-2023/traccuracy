import itertools
from collections import Counter

from cell_tracking_metrics.track_errors.division_events import DivisionEvents
from cell_tracking_metrics.tracking_graph import TrackingGraph
from cell_tracking_metrics.utils import find_gt_node_matches, find_pred_node_matches


def classify_divisions(G_gt, G_pred, mapper):
    """Identify each division as a true positive, false positive or false negative

    This function only works on node mappers that are one-to-one

    Args:
        G_gt (TrackingGraph): TrackingGraph of GT data
        G_pred (TrackingGraph): TrackingGraph of pred data
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
            counts.fn_division.append(gt_node)
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


def get_pred_by_t(G, node, delta_frames):
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


def get_succ_by_t(G, node, delta_frames):
    """For a given node, find the successors after delta frames

    If a division event is discovered, returns None

    Args:
        G (TrackingGraph): TrackingGraph to search on
        node (hashable): Key of starting node
        target_frame (int): Frame of the successor target node

    Returns:
        hashable: Node id of successor
    """
    print("start node", node)
    for _ in range(delta_frames):
        nodes = G.get_succs(node)
        # Exit if there are no successors another division
        if len(nodes) == 0 or len(nodes) >= 2:
            return None
        node = nodes[0]

    return node


def correct_shifted_divisions(G_gt, G_pred, mapper, n_frames=1, frame_key="t"):
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
        DivisionEvents: Corrected counts of gt_divisions, tp_divisions, fp_divisions and fn_divisions
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
    )

    # Compare all pairs of fp and fn
    for fp_node, fn_node in itertools.product(fp_divs, fn_divs):
        print(fp_node, fn_node)
        correct = False
        t_fp = G_pred.graph.nodes[fp_node][frame_key]
        t_fn = G_gt.graph.nodes[fn_node][frame_key]

        # Move on if nodes are not within frame buffer or within same frame
        if abs(t_fp - t_fn) > n_frames or t_fp == t_fn:
            print("not in buffer")
            continue

        # False positive in pred occurs before false negative in gt
        if t_fp < t_fn:
            print("fp before fn")
            # Check if fp node matches prececessor of fn
            fn_pred = get_pred_by_t(G_gt, fn_node, t_fn - t_fp, frame_key=frame_key)
            print("fn_pred", fn_pred)
            # Check if the match exists
            if (fn_pred, fp_node) not in mapper:
                # Match does not exist so divisions cannot match
                continue

            # Check if daughters match
            fp_succ = [
                get_succ_by_t(G_pred, node, 1 + t_fn - t_fp, frame_key=frame_key)
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
            print("fn before fp")
            # Check if fp node matches fn predecessor
            fp_pred = get_pred_by_t(
                G_pred, fp_node, 1 + t_fp - t_fn, frame_key=frame_key
            )
            print("fp pred", fp_pred)
            # Check if match exists
            if (fn_node, fp_pred) not in mapper:
                print("not in mapper")
                # Match does not exist so divisions cannot match
                continue

            # Check if daughters match
            fn_succ = [
                get_succ_by_t(G_gt, node, t_fp - t_fn, frame_key=frame_key)
                for node in G_gt.get_succs(fn_node)
            ]
            fp_succ = G_pred.get_succs(fp_node)
            print("fp_succ", fp_succ)
            print("fn succ", fn_succ)
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
