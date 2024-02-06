from __future__ import annotations

from typing import Hashable

import numpy as np
from tqdm import tqdm

from traccuracy._tracking_graph import TrackingGraph

from ._base import Matched, Matcher
from ._compute_overlap import get_labels_with_overlap


def _match_nodes(gt, res, threshold=1):
    """Identify overlapping objects according to IoU and a threshold for minimum overlap.

    QUESTION: Does this rely on sequential segmentation labels

    Args:
        gt (np.ndarray): labeled frame
        res (np.ndarray): labeled frame
        threshold (optional, float): threshold value for IoU to count as same cell. Default 1.
            If segmentations are identical, 1 works well.
            For imperfect segmentations try 0.6-0.8 to get better matching
    Returns:
        gtcells (np arr): Array of overlapping ids in the gt frame.
        rescells (np arr): Array of overlapping ids in the res frame.
    """
    iou = np.zeros((np.max(gt) + 1, np.max(res) + 1))

    overlapping_gt_labels, overlapping_res_labels, _ = get_labels_with_overlap(gt, res)

    for index in range(len(overlapping_gt_labels)):
        iou_gt_idx = overlapping_gt_labels[index]
        iou_res_idx = overlapping_res_labels[index]
        intersection = np.logical_and(gt == iou_gt_idx, res == iou_res_idx)
        union = np.logical_or(gt == iou_gt_idx, res == iou_res_idx)
        iou[iou_gt_idx, iou_res_idx] = intersection.sum() / union.sum()

    pairs = np.where(iou >= threshold)

    # Catch the case where there are no overlaps
    if len(pairs) < 2:
        gtcells, rescells = [], []
    else:
        gtcells, rescells = pairs[0], pairs[1]

    return gtcells, rescells


def _construct_time_to_seg_id_map(
    graph: TrackingGraph,
) -> dict[int, dict[Hashable, Hashable]]:
    """For each time frame in the graph, create a mapping from segmentation ids
    (the ids in the segmentation array, stored in graph.label_key) to the
    node ids (the ids of the TrackingGraph nodes).

    Args:
        graph(TrackingGraph): a tracking graph with a label_key on each node

    Returns:
      dict[int, dict[Hashable, Hashable]]: a dictionary from {time: {segmentation_id: node_id}}

    Raises:
        AssertionError: If two nodes in a time frame have the same segmentation_id
    """
    time_to_seg_id_map: dict[int, dict[Hashable, Hashable]] = {}
    for node_id, data in graph.nodes(data=True):
        time = data[graph.frame_key]
        seg_id = data[graph.label_key]
        seg_id_to_node_id_map = time_to_seg_id_map.get(time, {})
        assert (
            seg_id not in seg_id_to_node_id_map
        ), f"Segmentation ID {seg_id} occurred twice in frame {time}."
        seg_id_to_node_id_map[seg_id] = node_id
        time_to_seg_id_map[time] = seg_id_to_node_id_map
    return time_to_seg_id_map


def match_iou(gt, pred, threshold=0.6):
    """Identifies pairs of cells between gt and pred that have iou > threshold

    This can return more than one match for any node
    Assumes that within a frame, each object has a unique segmentation label
    and that the label is recorded on each node using label_key

    Args:
        gt (traccuracy.TrackingGraph): Tracking data object containing graph and segmentations
        pred (traccuracy.TrackingGraph): Tracking data object containing graph and segmentations
        threshold (float, optional): Minimum IoU for matching cells. Defaults to 0.6.

    Returns:
        list[(gt_node, pred_node)]: list of tuples where each tuple contains a gt node and pred node

    Raises:
        ValueError: gt and pred must be a TrackingData object
        ValueError: GT and pred segmentations must be the same shape
    """
    if not isinstance(gt, TrackingGraph) or not isinstance(pred, TrackingGraph):
        raise ValueError(
            "Input data must be a TrackingData object with a graph and segmentations"
        )

    mapper = []

    if gt.segmentation.shape != pred.segmentation.shape:
        raise ValueError("Segmentation shapes must match between gt and pred")

    # Get overlaps for each frame
    gt_frames = sorted(gt.nodes_by_frame.keys())
    total = len(gt_frames)

    gt_time_to_seg_id_map = _construct_time_to_seg_id_map(gt)
    pred_time_to_seg_id_map = _construct_time_to_seg_id_map(pred)

    for i, t in tqdm(enumerate(gt_frames), desc="Matching frames", total=total):
        matches = _match_nodes(
            gt.segmentation[i], pred.segmentation[i], threshold=threshold
        )
        # Construct node id tuple for each match
        for gt_seg_id, pred_seg_id in zip(*matches):
            # Find node id based on time and segmentation label
            gt_node = gt_time_to_seg_id_map[t][gt_seg_id]
            pred_node = pred_time_to_seg_id_map[t][pred_seg_id]
            mapper.append((gt_node, pred_node))
    return mapper


class IOUMatcher(Matcher):
    """Constructs a mapping between gt and pred nodes using the IoU of the segmentations

    Lower values for iou_threshold will be more permissive of imperfect matches

    Args:
        iou_threshold (float, optional): Minimum IoU value to assign a match. Defaults to 0.6.
    """

    def __init__(self, iou_threshold=0.6):
        self.iou_threshold = iou_threshold

    def _compute_mapping(self, gt_graph: TrackingGraph, pred_graph: TrackingGraph):
        """Computes IOU mapping for a set of grpahs

        Args:
            gt_graph (TrackingGraph): Tracking graph object for the gt with segmentation data
            pred_graph (TrackingGraph): Tracking graph object for the pred with segmentation data

        Raises:
            ValueError: Segmentation data must be provided for both gt and pred data

        Returns:
            Matched: Matched data object containing IOU mapping
        """
        # Check that segmentations exist in the data
        if gt_graph.segmentation is None or pred_graph.segmentation is None:
            raise ValueError(
                "Segmentation data must be provided for both gt and pred data"
            )

        mapping = match_iou(gt_graph, pred_graph, threshold=self.iou_threshold)

        return Matched(gt_graph, pred_graph, mapping)
