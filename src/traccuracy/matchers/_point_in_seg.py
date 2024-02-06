from typing import TYPE_CHECKING

from ._base import Matched, Matcher
from ._iou import _construct_time_to_seg_id_map

if TYPE_CHECKING:
    from traccuracy._tracking_graph import TrackingGraph


class PointInSegMatcher(Matcher):
    def match_points_to_seg(self, gt_graph, pred_graph):
        """Match points from the pred_graph to points from the gt_graph
        if they are within the corresponding segmentation.
        This allows multiple predicted nodes to be matched to the same
        gt node.

        Args:
            gt_graph (TrackingGraph): _description_
            pred_graph (TrackingGraph): _description_

        Returns:
            list of tuples: [(gt_node_id, pred_node_id), ...]
        """
        mapping = []
        gt_seg = gt_graph.segmentation
        gt_time_to_seg_id_map = _construct_time_to_seg_id_map(gt_graph)
        for pred_node in pred_graph.nodes():
            frame = pred_graph.nodes[pred_node][pred_graph.frame_key]
            location = pred_graph.get_location(pred_node)
            gt_seg_id = gt_seg[location]
            if gt_seg_id is None:
                continue
            gt_node_id = gt_time_to_seg_id_map[frame][gt_seg_id]
            mapping.append((gt_node_id, pred_node))

        return mapping

    def _compute_mapping(
        self, gt_graph: TrackingGraph, pred_graph: TrackingGraph
    ) -> Matched:
        # Check that segmentation exist in the gt data
        if gt_graph.segmentation is None:
            raise ValueError("Segmentation must be provided for gt data")

        mapping = self.match_points_to_seg(
            gt_graph,
            pred_graph,
        )

        return Matched(gt_graph, pred_graph, mapping)
