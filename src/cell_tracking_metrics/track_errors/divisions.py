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

    counts = DivisionEvents(
        **{
            "gt_divisions": len(div_gt),
            "tp_divisions": 0,
            "fp_divisions": 0,
            "fn_divisions": 0,
        }
    )

    for gt_node in div_gt:
        # Find possible matching nodes
        pred_node = _find_gt_node_matches(gt_node)
        # No matching node so division missed
        if pred_node is None:
            counts.fn_divisions += 1
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
                counts.tp_divisions += 1
                G_gt.set_node_attribute(gt_node, "is_tp_division", True)
                G_pred.set_node_attribute(pred_node, "is_tp_division", True)
            # If daughters are at all mismatched, division is false negative
            else:
                counts.fn_divisions += 1
                G_gt.set_node_attribute(gt_node, "is_fn_division", True)

        # Remove res division to record that we have classified it
        if pred_node in div_pred:
            div_pred.remove(pred_node)

    # Any remaining pred divisions are false positives
    counts.fp_divisions += len(div_pred)
    G_pred.set_node_attribute(div_pred, "is_fp_division", True)

    return counts, G_gt, G_pred
