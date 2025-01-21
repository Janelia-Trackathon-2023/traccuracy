import numpy as np


def get_labels_with_overlap(
    gt_frame: np.ndarray,
    res_frame: np.ndarray,
    overlap: str = "iou",
) -> list[tuple[int, int, float]]:
    """Get all labels IDs in gt_frame and res_frame whose bounding boxes
    overlap.

    Args:
        gt_frame (np.ndarray): ground truth segmentation for a single frame
        res_frame (np.ndarray): result segmentation for a given frame
        overlap (str, optional): Choose between intersection-over-ground-truth (``iogt``)
            or intersection-over-union (``iou``).

    Returns:
        list[tuple[int, int, float]]: List of tuples of label in gt_frame, label in
            res_frame, and iou values. Labels that have no overlap are not included.
    """
    gt_frame = gt_frame.flatten()
    res_frame = res_frame.flatten()
    # get indices where both are not zero (ignore background)
    # this speeds up computation significantly
    non_zero_indices = np.logical_and(gt_frame, res_frame)
    flattened_stacked = np.array(
        [gt_frame[non_zero_indices], res_frame[non_zero_indices]]
    )

    values, counts = np.unique(flattened_stacked, axis=1, return_counts=True)
    gt_values, gt_counts = np.unique(gt_frame, return_counts=True)
    gt_label_sizes = dict(zip(gt_values, gt_counts))
    res_values, res_counts = np.unique(res_frame, return_counts=True)
    res_label_sizes = dict(zip(res_values, res_counts))
    overlaps: list[tuple[int, int, float]] = []
    for index in range(values.shape[1]):
        pair = values[:, index]
        intersection = counts[index]
        gt_label, res_label = pair
        if overlap == "iou":
            denom = gt_label_sizes[gt_label] + res_label_sizes[res_label] - intersection
        elif overlap == "iogt":
            denom = gt_label_sizes[gt_label]
        else:
            raise ValueError(f"Unknown overlap type: {overlap}")
        overlaps.append((gt_label, res_label, intersection / denom))
    return overlaps
