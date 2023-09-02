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


from traccuracy.track_errors.divisions import _evaluate_division_events

from ._base import Metric


def _calculate_metrics(G_gt, G_pred):
    if not (G_gt.division_annotations and G_pred.division_annotations):
        raise ValueError(
            "Both input TrackingGraphs must have division_annotations calculated"
        )

    tp_division_count = len(
        G_gt.get_nodes_with_attribute("is_tp_division", lambda x: x)
    )
    fn_division_count = len(
        G_gt.get_nodes_with_attribute("is_fn_division", lambda x: x)
    )
    fp_division_count = len(
        G_pred.get_nodes_with_attribute("is_fp_division", lambda x: x)
    )

    try:
        recall = tp_division_count / (tp_division_count + fn_division_count)
    except ZeroDivisionError:
        recall = 0

    try:
        precision = tp_division_count / (tp_division_count + fp_division_count)
    except ZeroDivisionError:
        precision = 0

    try:
        f1 = 2 * (recall * precision) / (recall + precision)
    except ZeroDivisionError:
        f1 = 0

    try:
        mbc = tp_division_count / (
            tp_division_count + fn_division_count + fp_division_count
        )
    except ZeroDivisionError:
        mbc = 0

    return {
        "Division Recall": recall,
        "Division Precision": precision,
        "Division F1": f1,
        "Mitotic Branching Correctness": mbc,
        "True Positive Divisions": tp_division_count,
        "False Positive Divisions": fp_division_count,
        "False Negative Divisions": fn_division_count,
    }


class DivisionMetrics(Metric):
    needs_one_to_one = True

    def __init__(self, matched_data, frame_buffer=(0,)):
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
        div_annotations = _evaluate_division_events(
            self.data.gt_data.tracking_graph,
            self.data.pred_data.tracking_graph,
            self.data.mapping,
            frame_buffer=self.frame_buffer,
        )

        return {
            f"Frame Buffer {fb}": _calculate_metrics(G_gt, G_pred)
            for fb, (G_gt, G_pred) in div_annotations.items()
        }
