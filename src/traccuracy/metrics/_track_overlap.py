"""This submodule implements routines for Track Purity (TP) and Target Effectiveness (TE) scores.

Definitions (Bise et al., 2011; Chen, 2021; Fukai et al., 2022):

- TE for a single ground truth track T^g_j is calculated by finding the predicted track T^p_k
  that overlaps with T^g_j in the largest number of the frames and then dividing 
  the overlap frame counts by the total frame counts for T^g_j.
  The TE for the total dataset is calculated as the mean of TEs for all ground truth tracks,
  weighted by the length of the tracks.

- TP is defined analogously, with T^g_j and T^p_j being swapped in the definition.
"""

from typing import TYPE_CHECKING, Any, List, Tuple

from traccuracy._tracking_graph import TrackingGraph

from ._base import Metric

if TYPE_CHECKING:
    from ._base import Matched


class TrackOverlapMetrics(Metric):
    supports_many_to_one = True

    def __init__(self, matched_data: "Matched"):
        super().__init__(matched_data)

    def compute(self):
        # requires tracklets that also have the splitting and merging edges
        # edgess are a list of edges, grouped by the tracks
        gt_tracklets = self.data.gt_graph.get_tracklets(include_intertrack_edges=True)
        pred_tracklets = self.data.pred_graph.get_tracklets(
            include_intertrack_edges=True
        )

        gt_pred_mapping = self.data.mapping
        pred_gt_mapping = [
            (pred_node, gt_node) for gt_node, pred_node in gt_pred_mapping
        ]

        # calculate track purity and target effectiveness
        track_purity = _calc_overlap_score(
            pred_tracklets, gt_tracklets, pred_gt_mapping
        )
        target_effectiveness = _calc_overlap_score(
            gt_tracklets, pred_tracklets, gt_pred_mapping
        )
        return {
            "track_purity": track_purity,
            "target_effectiveness": target_effectiveness,
        }


def _calc_overlap_score(
    reference_tracklets: List[TrackingGraph],
    overlap_tracklets: List[TrackingGraph],
    mapping: List[Tuple[Any, Any]],
):
    """Calculate weighted sum of the length of the longest overlap tracklet
    for each reference tracklet.

    Args:
       reference_tracklets (List[TrackingGraph]): The reference tracklets
       overlap_tracklets (List[TrackingGraph]): The tracklets that overlap
       mapping (List[Tuple[Any, Any]]): Mapping between the reference tracklet nodes
       and the overlap tracklet nodes

    """
    correct_count = 0
    total_count = 0
    # iterate over the reference tracklets
    for reference_tracklet in reference_tracklets:
        # find the overlap tracklet with the largest overlap
        reference_tracklet_nodes_mapped = [
            n_to for (n_from, n_to) in mapping if n_from in reference_tracklet.nodes()
        ]
        overlaps = [
            len(set(reference_tracklet_nodes_mapped) & set(overlap_tracklet.nodes()))
            for overlap_tracklet in overlap_tracklets
        ]
        max_overlap = max(overlaps)
        correct_count += max_overlap
        total_count += len(reference_tracklet_nodes_mapped)

    return correct_count / total_count if total_count > 0 else -1
