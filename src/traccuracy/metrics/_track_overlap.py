"""This submodule implements routines for Track Purity (TP) and Target Effectiveness (TE) scores.

Definitions (Bise et al., 2011; Chen, 2021; Fukai et al., 2022):

- TE for a single ground truth track T^g_j is calculated by finding the predicted track T^p_k
  that overlaps with T^g_j in the largest number of the frames and then dividing
  the overlap frame counts by the total frame counts for T^g_j.
  The TE for the total dataset is calculated as the mean of TEs for all ground truth tracks,
  weighted by the length of the tracks.

- TP is defined analogously, with T^g_j and T^p_j being swapped in the definition.
"""
from __future__ import annotations

from itertools import groupby, product
from typing import TYPE_CHECKING, Any

from ._base import Metric

if TYPE_CHECKING:
    from traccuracy._tracking_graph import TrackingGraph
    from traccuracy.matchers import Matched


def _mapping_to_dict(mapping: list[tuple[Any, Any]]) -> dict[Any, list[Any]]:
    """Convert mapping list of tuples to dictionary.

    Args:
        mapping (List[Tuple[Any, Any]]): Mapping list of tuples

    Returns:
        Dict[Any, List[Any]]: Mapping dictionary

    """

    def get_from_val(x):
        return x[0]

    return {
        k: [v[1] for v in vs]
        for k, vs in groupby(sorted(mapping, key=get_from_val), key=get_from_val)
    }


class TrackOverlapMetrics(Metric):
    """Calculate metrics for longest track overlaps.

    - Target Effectiveness: fraction of longest overlapping prediction
                            tracklets on each GT tracklet
    - Track Purity : fraction of longest overlapping GT
                     tracklets on each prediction tracklet

    Args:
        matched_data (traccuracy.matchers.Matched): Matched object for set of GT and Pred data
        include_division_edges (bool, optional): If True, include edges at division.

    """

    supports_many_to_one = True

    def __init__(self, include_division_edges: bool = True):
        self.include_division_edges = include_division_edges

    def compute(self, matched: Matched) -> dict:
        gt_tracklets = matched.gt_graph.get_tracklets(
            include_division_edges=self.include_division_edges
        )
        pred_tracklets = matched.pred_graph.get_tracklets(
            include_division_edges=self.include_division_edges
        )

        gt_pred_mapping = _mapping_to_dict(matched.mapping)
        pred_gt_mapping = _mapping_to_dict(
            [(pred_node, gt_node) for gt_node, pred_node in matched.mapping]
        )

        # calculate track purity and target effectiveness
        track_purity = _calc_overlap_score(
            pred_tracklets, gt_tracklets, gt_pred_mapping
        )
        target_effectiveness = _calc_overlap_score(
            gt_tracklets, pred_tracklets, pred_gt_mapping
        )
        return {
            "track_purity": track_purity,
            "target_effectiveness": target_effectiveness,
        }


def _calc_overlap_score(
    reference_tracklets: list[TrackingGraph],
    overlap_tracklets: list[TrackingGraph],
    overlap_reference_mapping: dict[Any, list[Any]],
):
    """Calculate weighted sum of the length of the longest overlap tracklet
    for each reference tracklet.

    Args:
        reference_tracklets (List[TrackingGraph]): The reference tracklets
        overlap_tracklets (List[TrackingGraph]): The tracklets that overlap
        overlap_reference_mapping (Dict[Any, List[Any]]): Mapping as a dict
            from the overlap tracklet nodes to the reference tracklet nodes

    """
    correct_count = 0
    total_count = 0

    # calculate all overlapping edges mapped onto GT ids
    overlap_tracklets_edges_mapped = []
    for overlap_tracklet in overlap_tracklets:
        edges = []
        for node1, node2 in overlap_tracklet.edges():
            mapped_nodes1 = overlap_reference_mapping.get(node1, [])
            mapped_nodes2 = overlap_reference_mapping.get(node2, [])
            if mapped_nodes1 and mapped_nodes2:
                for n1, n2 in product(mapped_nodes1, mapped_nodes2):
                    edges.append((n1, n2))
        overlap_tracklets_edges_mapped.append(edges)

    for reference_tracklet in reference_tracklets:
        # find the overlap tracklet with the largest overlap
        overlaps = [
            len(set(reference_tracklet.edges()) & set(edges))
            for edges in overlap_tracklets_edges_mapped
        ]
        max_overlap = max(overlaps)
        correct_count += max_overlap
        total_count += len(reference_tracklet.edges())

    return correct_count / total_count if total_count > 0 else -1
