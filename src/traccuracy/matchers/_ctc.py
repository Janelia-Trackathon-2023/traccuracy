from __future__ import annotations

from typing import TYPE_CHECKING

import networkx as nx
import numpy as np
from tqdm import tqdm

if TYPE_CHECKING:
    from traccuracy._tracking_graph import TrackingGraph

from ._base import Matched, Matcher
from ._compute_overlap import get_labels_with_overlap


class CTCMatcher(Matcher):
    """Match graph nodes based on measure used in cell tracking challenge benchmarking.

    A computed marker (segmentation) is matched to a reference marker if the computed
    marker covers a majority of the reference marker.

    Each reference marker can therefore only be matched to one computed marker, but
    multiple reference markers can be assigned to a single computed marker.

    See https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0144959
    for complete details.
    """

    def _compute_mapping(self, gt_graph: TrackingGraph, pred_graph: TrackingGraph):
        """Run ctc matching

        Args:
            gt_graph (TrackingGraph): Tracking graph object for the gt
            pred_graph (TrackingGraph): Tracking graph object for the pred

        Returns:
            traccuracy.matchers.Matched: Matched data object containing the CTC mapping

        Raises:
            ValueError: if GT and pred segmentations are None or are not the same shape
        """
        gt = gt_graph
        pred = pred_graph
        gt_label_key = gt_graph.label_key
        pred_label_key = pred_graph.label_key
        G_gt, mask_gt = gt, gt.segmentation
        G_pred, mask_pred = pred, pred.segmentation

        if mask_gt is None or mask_pred is None:
            raise ValueError("Segmentation is None, cannot perform matching")

        if mask_gt.shape != mask_pred.shape:
            raise ValueError("Segmentation shapes must match between gt and pred")

        mapping = []
        # Get overlaps for each frame
        for i, t in enumerate(
            tqdm(
                range(gt.start_frame, gt.end_frame),
                desc="Matching frames",
            )
        ):
            gt_frame = mask_gt[i]
            pred_frame = mask_pred[i]
            gt_frame_nodes = gt.nodes_by_frame[t]
            pred_frame_nodes = pred.nodes_by_frame[t]

            # get the labels for this frame
            gt_labels = dict(
                filter(
                    lambda item: item[0] in gt_frame_nodes,
                    nx.get_node_attributes(G_gt.graph, gt_label_key).items(),
                )
            )
            gt_label_to_id = {v: k for k, v in gt_labels.items()}

            pred_labels = dict(
                filter(
                    lambda item: item[0] in pred_frame_nodes,
                    nx.get_node_attributes(G_pred.graph, pred_label_key).items(),
                )
            )
            pred_label_to_id = {v: k for k, v in pred_labels.items()}

            (
                overlapping_gt_labels,
                overlapping_pred_labels,
                intersection,
            ) = get_labels_with_overlap(gt_frame, pred_frame)

            for i in range(len(overlapping_gt_labels)):
                gt_label = overlapping_gt_labels[i]
                pred_label = overlapping_pred_labels[i]
                # CTC metrics only match comp IDs to a single GT ID if there is majority overlap
                if intersection[i] > 0.5:
                    mapping.append(
                        (gt_label_to_id[gt_label], pred_label_to_id[pred_label])
                    )

        return Matched(gt_graph, pred_graph, mapping)


def detection_test(gt_blob: np.ndarray, comp_blob: np.ndarray) -> int:
    """Check if computed marker overlaps majority of the reference marker.

    Given a reference marker and computer marker in original coordinates,
    return True if the computed marker overlaps strictly more than half
    of the reference marker's pixels, otherwise False.

    Parameters
    ----------
    gt_blob : np.ndarray
        2D or 3D boolean mask representing the pixels of the ground truth
        marker
    comp_blob : np.ndarray
        2D or 3D boolean mask representing the pixels of the computed
        marker

    Returns
    -------
    bool
        True if computed marker majority overlaps reference marker, else False.
    """
    n_gt_pixels = np.sum(gt_blob)
    intersection = np.logical_and(gt_blob, comp_blob)
    comp_blob_matches_gt_blob = int(np.sum(intersection) > 0.5 * n_gt_pixels)
    return comp_blob_matches_gt_blob
