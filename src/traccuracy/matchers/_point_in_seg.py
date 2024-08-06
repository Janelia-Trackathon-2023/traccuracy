from __future__ import annotations

from typing import TYPE_CHECKING

from ._base import Matched, Matcher
from ._iou import _construct_time_to_seg_id_map

if TYPE_CHECKING:
    from traccuracy._tracking_graph import TrackingGraph


def match_point_in_seg(seg_graph, points_graph):
    """Match points from the points_graph to points from the seg_graph
    if they are within the corresponding segmentation.
    This allows multiple points_graph nodes to be matched to the same
    seg_graph node.

    Args:
        seg_graph (TrackingGraph): _description_
        points_graph (TrackingGraph): _description_

    Returns:
        list of tuples: [(seg_node, points_node), ...]
    """
    mapping = []
    seg = seg_graph.segmentation
    time_to_seg_id_map = _construct_time_to_seg_id_map(seg_graph)
    for points_node in points_graph.nodes():
        frame = points_graph.nodes[points_node][points_graph.frame_key]
        location = points_graph.get_location(points_node)
        slices = [slice(dim) for dim in location]
        print(seg.shape)
        print(frame)
        print(slices)
        seg_id = seg[frame][slices]
        if seg_id is None or seg_id == 0:
            continue
        seg_node = time_to_seg_id_map[frame][seg_id]
        mapping.append((seg_node, points_node))

    return mapping


class PredPointInSegMatcher(Matcher):
    # many pred can be matched to one GT
    def _compute_mapping(
        self, gt_graph: TrackingGraph, pred_graph: TrackingGraph
    ) -> Matched:
        # Check that segmentation exist in the gt data
        if gt_graph.segmentation is None:
            raise ValueError("Segmentation must be provided for gt data")

        mapping = match_point_in_seg(
            gt_graph,
            pred_graph,
        )

        return Matched(gt_graph, pred_graph, mapping)


class GTPointInSegMatcher(Matcher):
    # many GT can be matched to one pred
    def _compute_mapping(
        self, gt_graph: TrackingGraph, pred_graph: TrackingGraph
    ) -> Matched:
        # Check that segmentation exist in the pred data
        if pred_graph.segmentation is None:
            raise ValueError("Segmentation must be provided for pred data")

        mapping = match_point_in_seg(
            pred_graph,
            gt_graph,
        )

        # invert the mapping order
        mapping = [(b, a) for (a, b) in mapping]

        return Matched(gt_graph, pred_graph, mapping)
