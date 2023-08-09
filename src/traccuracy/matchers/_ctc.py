import networkx as nx
import numpy as np
from tqdm import tqdm

from traccuracy._tracking_data import TrackingData

from ._compute_overlap import get_labels_with_overlap
from ._matched import Matched


class CTCMatched(Matched):
    def compute_mapping(self):
        mapping = self._match_ctc()
        return mapping

    def _match_ctc(self):
        """Match graph nodes based on measure used in cell tracking challenge benchmarking.

        A computed marker (segmentation) is matched to a reference marker if the computed
        marker covers a majority of the reference marker.

        Each reference marker can therefore only be matched to one computed marker, but
        multiple reference markers can be assigned to a single computed marker.

        See https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0144959
        for complete details.

        Returns:
            list[(gt_node, pred_node)]: list of tuples where each tuple contains a gt node
            and pred node

        Raises:
            ValueError: gt and pred must be a TrackingData object
            ValueError: GT and pred segmentations must be the same shape
        """
        if not isinstance(self.gt_data, TrackingData) or not isinstance(
            self.pred_data, TrackingData
        ):
            raise ValueError(
                "Input data must be a TrackingData object with a graph and segmentations"
            )
        gt = self.gt_data
        pred = self.pred_data
        gt_label_key = self.gt_data.tracking_graph.label_key
        pred_label_key = self.pred_data.tracking_graph.label_key
        G_gt, mask_gt = gt.tracking_graph, gt.segmentation
        G_pred, mask_pred = pred.tracking_graph, pred.segmentation

        if mask_gt.shape != mask_pred.shape:
            raise ValueError("Segmentation shapes must match between gt and pred")

        mapping = []
        # Get overlaps for each frame
        for i, t in enumerate(
            tqdm(
                range(gt.tracking_graph.start_frame, gt.tracking_graph.end_frame),
                desc="Matching frames",
            )
        ):
            gt_frame = mask_gt[i]
            pred_frame = mask_pred[i]
            gt_frame_nodes = gt.tracking_graph.nodes_by_frame[t]
            pred_frame_nodes = pred.tracking_graph.nodes_by_frame[t]

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
        return mapping


def detection_test(gt_blob: "np.ndarray", comp_blob: "np.ndarray") -> int:
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
