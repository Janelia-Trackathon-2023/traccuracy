import numpy as np
from tqdm import tqdm

from traccuracy.matchers.compute_overlap import (
    get_labels_with_overlap,
)
from traccuracy.tracking_data import TrackingData

from .matched import Matched


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

    overlapping_gt_labels, overlapping_res_labels = get_labels_with_overlap(gt, res)

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


def match_iou(gt, pred, threshold=0.6):
    """Identifies pairs of cells between gt and pred that have iou > threshold

    This can return more than one match for any node
    Assumes that within a frame, each object has a unique segmentation label
    and that the label is recorded on each node using label_key

    Args:
        gt (TrackingData): Tracking data object containing graph and segmentations
        pred (TrackingData): Tracking data object containing graph and segmentations
        threshold (float, optional): Minimum IoU for matching cells. Defaults to 0.6.

    Returns:
        list[(gt_node, pred_node)]: list of tuples where each tuple contains a gt node and pred node

    Raises:
        ValueError: gt and pred must be a TrackingData object
        ValueError: GT and pred segmentations must be the same shape
    """
    if not isinstance(gt, TrackingData) or not isinstance(pred, TrackingData):
        raise ValueError(
            "Input data must be a TrackingData object with a graph and segmentations"
        )

    mapper = []

    G_gt, mask_gt = gt.tracking_graph, gt.segmentation
    G_pred, mask_pred = pred.tracking_graph, pred.segmentation

    if mask_gt.shape != mask_pred.shape:
        raise ValueError("Segmentation shapes must match between gt and pred")

    # Get overlaps for each frame
    frame_range = range(gt.tracking_graph.start_frame, gt.tracking_graph.end_frame)
    total = len(list(frame_range))
    for i, t in tqdm(enumerate(frame_range), desc="Matching frames", total=total):
        matches = _match_nodes(mask_gt[i], mask_pred[i], threshold=threshold)

        # Construct node id tuple for each match
        for gt_id, pred_id in zip(*matches):
            # Find node id based on time and segmentation label
            gt_node = G_gt.get_nodes_with_attribute(
                G_gt.label_key,
                criterion=lambda x: x == gt_id,  # noqa
                limit_to=G_gt.get_nodes_in_frame(t),
            )[0]
            pred_node = G_pred.get_nodes_with_attribute(
                G_pred.label_key,
                criterion=lambda x: x == pred_id,  # noqa
                limit_to=G_pred.get_nodes_in_frame(t),
            )[0]
            mapper.append((gt_node, pred_node))
    return mapper


class IOUMatched(Matched):
    def __init__(self, gt_data, pred_data, iou_threshold=0.6):
        """Constructs a mapping between gt and pred nodes using the IoU of the segmentations

        Lower values for iou_threshold will be more permissive of imperfect matches

        Args:
            gt_data (TrackingData): TrackingData for the ground truth with segmentations
            pred_data (TrackingData): TrackingData for the prediction with segmentations
            iou_threshold (float, optional): Minimum IoU value to assign a match. Defaults to 0.6.

        Raises:
            ValueError: Segmentation data must be provided for both gt and pred data
        """
        self.iou_threshold = iou_threshold

        # Check that segmentations exist in the data
        if gt_data.segmentation is None or pred_data.segmentation is None:
            raise ValueError(
                "Segmentation data must be provided for both gt and pred data"
            )

        super().__init__(gt_data, pred_data)

    def compute_mapping(self):
        return match_iou(self.gt_data, self.pred_data, threshold=self.iou_threshold)
