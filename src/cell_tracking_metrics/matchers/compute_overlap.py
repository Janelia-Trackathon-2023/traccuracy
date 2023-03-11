"""Fast R-CNN via numba

adapted from Fast R-CNN
Written by Sergey Karayev
Licensed under The MIT License [see LICENSE for details]
Copyright (c) 2015 Microsoft
"""
import numpy as np


def compute_overlap(boxes: np.ndarray, query_boxes: np.ndarray) -> np.ndarray:
    """
    Args
        a: (N, 4) ndarray of float
        b: (K, 4) ndarray of float

    Returns
        overlaps: (N, K) ndarray of overlap between boxes and query_boxes
    """
    N = boxes.shape[0]
    K = query_boxes.shape[0]
    overlaps = np.zeros((N, K), dtype=np.float64)
    for k in range(K):
        box_area = (query_boxes[k, 2] - query_boxes[k, 0] + 1) * (
            query_boxes[k, 3] - query_boxes[k, 1] + 1
        )
        for n in range(N):
            iw = (
                min(boxes[n, 2], query_boxes[k, 2])
                - max(boxes[n, 0], query_boxes[k, 0])
                + 1
            )
            if iw > 0:
                ih = (
                    min(boxes[n, 3], query_boxes[k, 3])
                    - max(boxes[n, 1], query_boxes[k, 1])
                    + 1
                )
                if ih > 0:
                    ua = np.float64(
                        (boxes[n, 2] - boxes[n, 0] + 1)
                        * (boxes[n, 3] - boxes[n, 1] + 1)
                        + box_area
                        - iw * ih
                    )
                    overlaps[n, k] = iw * ih / ua
    return overlaps


def compute_overlap_3D(boxes: np.ndarray, query_boxes: np.ndarray) -> np.ndarray:
    """
    Args
        a: (N, 6) ndarray of float
        b: (K, 6) ndarray of float

    Returns
        overlaps: (N, K) ndarray of overlap between boxes and query_boxes
    """
    N = boxes.shape[0]
    K = query_boxes.shape[0]
    overlaps = np.zeros((N, K), dtype=np.float64)
    for k in range(K):
        box_volume = (
            (query_boxes[k, 3] - query_boxes[k, 0] + 1)
            * (query_boxes[k, 4] - query_boxes[k, 1] + 1)
            * (query_boxes[k, 5] - query_boxes[k, 2] + 1)
        )
        for n in range(N):
            id_ = (
                min(boxes[n, 3], query_boxes[k, 3])
                - max(boxes[n, 0], query_boxes[k, 0])
                + 1
            )
            if id_ > 0:
                iw = (
                    min(boxes[n, 4], query_boxes[k, 4])
                    - max(boxes[n, 1], query_boxes[k, 1])
                    + 1
                )
                if iw > 0:
                    ih = (
                        min(boxes[n, 5], query_boxes[k, 5])
                        - max(boxes[n, 2], query_boxes[k, 2])
                        + 1
                    )
                    if ih > 0:
                        ua = np.float64(
                            (boxes[n, 3] - boxes[n, 0] + 1)
                            * (boxes[n, 4] - boxes[n, 1] + 1)
                            * (boxes[n, 5] - boxes[n, 2] + 1)
                            + box_volume
                            - iw * ih * id_
                        )
                        overlaps[n, k] = iw * ih * id_ / ua
    return overlaps


try:
    import numba
except ImportError:
    import warnings
    import os

    if not os.getenv("NO_JIT_WARNING", False):
        warnings.warn(
            "Numba not installed, falling back to slower numpy implementation. "
            "Install numba for a significant speedup.  Set the environment "
            "variable NO_JIT_WARNING=1 to disable this warning."
        )
else:

    # compute_overlap 2d and 3d have the same signature
    signature = [
        "f8[:,::1](f8[:,::1], f8[:,::1])",
        numba.types.Array(numba.float64, 2, "C", readonly=True)(
            numba.types.Array(numba.float64, 2, "C", readonly=True),
            numba.types.Array(numba.float64, 2, "C", readonly=True),
        ),
    ]

    # variables that appear in the body of each function
    common_locals = {
        "N": numba.uint,
        "K": numba.uint,
        "overlaps": numba.types.Array(numba.float64, 2, "C"),
        "iw": numba.float64,
        "ih": numba.float64,
        "ua": numba.float64,
        "n": numba.uint,
        "k": numba.uint,
    }

    compute_overlap = numba.njit(
        signature,
        locals={**common_locals, "box_area": numba.float64},
        fastmath=True,
        nogil=True,
        boundscheck=False,
    )(compute_overlap)

    compute_overlap_3D = numba.njit(
        signature,
        locals={**common_locals, "id_": numba.float64, "box_volume": numba.float64},
        fastmath=True,
        nogil=True,
        boundscheck=False,
    )(compute_overlap_3D)
