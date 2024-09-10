from collections import Counter

import networkx as nx
import numpy as np
import pytest
from traccuracy._tracking_graph import TrackingGraph
from traccuracy.matchers._iou import (
    IOUMatcher,
    _construct_time_to_seg_id_map,
    _match_nodes,
    match_iou,
)

from tests.test_utils import get_annotated_image, get_movie_with_graph


# tests with new fixtures (incomplete)
def test_good_seg(good_segmentation_2d, good_segmentation_3d):
    # 2d
    gt_2d, pred_2d = good_segmentation_2d
    expected_matches = [(1, 2)]
    # Test for merge and force one to one
    gtcells, rescells = _match_nodes(gt_2d, pred_2d, threshold=0.4, one_to_one=True)
    computed_matches = list(zip(gtcells, rescells))
    assert Counter(expected_matches) == Counter(computed_matches)

    gtcells, rescells = _match_nodes(gt_2d, pred_2d, threshold=0.5)
    computed_matches = list(zip(gtcells, rescells))
    assert Counter(expected_matches) == Counter(computed_matches)

    gtcells, rescells = _match_nodes(gt_2d, pred_2d, threshold=0.8)
    computed_matches = list(zip(gtcells, rescells))
    expected_matches = []
    assert Counter(expected_matches) == Counter(computed_matches)

    # 3d
    gt_3d, pred_3d = good_segmentation_3d
    expected_matches = [(1, 2)]
    # Test for merge and force one to one
    gtcells, rescells = _match_nodes(gt_3d, pred_3d, threshold=0.4, one_to_one=True)
    computed_matches = list(zip(gtcells, rescells))
    assert Counter(expected_matches) == Counter(computed_matches)

    gtcells, rescells = _match_nodes(gt_3d, pred_3d, threshold=0.5)
    computed_matches = list(zip(gtcells, rescells))
    assert Counter(expected_matches) == Counter(computed_matches)


# test with old data
def get_two_to_one(w, h, imw, imh):
    """Basic two cell merge/split

    Mapping [(1,3), (2,4), (2,5)]

    """
    x = np.random.randint(2, imw - w * 2)
    y = np.random.randint(2, imh - h * 2)

    merge = np.zeros((imw, imh))
    merge[0:2, 0:2] = 1
    merge[x : x + w, y : y + h] = 2
    merge[x + w : x + 2 * w, y : y + h] = 2

    split = np.zeros((imw, imh))
    split[0:2, 0:2] = 3
    split[x : x + w, y : y + h] = 4
    split[x + w : x + 2 * w, y : y + h] = 5

    return merge.astype("int"), split.astype("int")


def get_no_overlap(imw, imh):
    """two non-overlapping segmentations that start at high number labels

    Mapping []

    """

    im1 = np.zeros((imw, imh))
    im1[0:2, 0:2] = 100

    im2 = np.zeros((imw, imh))
    im2[4:6, 4:6] = 222

    return im1.astype("int"), im2.astype("int")


def test__match_nodes():
    # creat dummy image to test against
    num_labels = 5
    y1 = get_annotated_image(img_size=256, num_labels=num_labels, seed=1)
    # test same movie
    gtcells, rescells = _match_nodes(y1, y1)
    for gt_cell, res_cell in zip(gtcells, rescells):
        assert gt_cell == res_cell

    # test different movies (no assertions about matching)
    y2 = get_annotated_image(img_size=256, num_labels=num_labels, seed=10)
    gtcells, rescells = _match_nodes(y1, y2)

    # Test for merge without forcing one to one
    im1, im2 = get_two_to_one(10, 10, 30, 30)
    gtcells, rescells = _match_nodes(im1, im2, threshold=0.4)
    for gt_cell, res_cell in zip(gtcells, rescells):
        assert (int(gt_cell), int(res_cell)) in [(1, 3), (2, 4), (2, 5)]

    # Test for merge and force one to one
    gtcells, rescells = _match_nodes(im1, im2, threshold=0.4, one_to_one=True)
    # Create match tuples
    matches = list(zip(gtcells, rescells))
    # Check for direct match
    assert (1, 3) in matches
    # Check that only one of the merge matches is present
    assert ((2, 4) in matches) != ((2, 5) in matches)

    with pytest.raises(ValueError):
        # Test that threshold 0 is not valid when not one-to-one
        gtcells, rescells = _match_nodes(im1, im2, threshold=0.0)


def test__match_nodes_threshold():
    im1, im2 = get_two_to_one(10, 10, 30, 30)
    # Test high threshold
    gtcells, rescells = _match_nodes(im1, im2, threshold=1)
    # Create match tuples
    matches = list(zip(gtcells, rescells))
    # Check that nothing is matched
    assert len(matches) == 1

    # Test for high threshold and one to one
    gtcells, rescells = _match_nodes(im1, im2, threshold=0.7, one_to_one=True)
    # Create match tuples
    matches = list(zip(gtcells, rescells))
    # Check that nothing is matched
    assert len(matches) == 1


def test__match_nodes_non_sequential():
    # test when the segmentation ids are high numbers (the lower numbers should never appear)

    im1, im2 = get_no_overlap(30, 30)

    # Test that phantom segmentations are not matched
    gtcells, rescells = _match_nodes(im1, im2, threshold=0.1)
    # Create match tuples
    matches = list(zip(gtcells, rescells))
    # Check that nothing is matched
    assert len(matches) == 0

    # Test that with one-to-one, phantom segmentations are not matched,
    # even with threshold 0
    gtcells, rescells = _match_nodes(im1, im2, threshold=0.0, one_to_one=True)
    # Create match tuples
    matches = list(zip(gtcells, rescells))
    # Check that nothing is matched
    assert len(matches) == 0


def test__construct_time_to_seg_id_map():
    # Test 2d data
    n_frames = 3
    n_labels = 3
    track_graph = get_movie_with_graph(ndims=3, n_frames=n_frames, n_labels=n_labels)
    time_to_seg_id_map = _construct_time_to_seg_id_map(track_graph)
    for t in range(n_frames):
        for i in range(1, n_labels):
            assert time_to_seg_id_map[t][i] == f"{i}_{t}"

    # Test 3d data
    track_graph = get_movie_with_graph(ndims=4, n_frames=n_frames, n_labels=n_labels)
    time_to_seg_id_map = _construct_time_to_seg_id_map(track_graph)
    for t in range(n_frames):
        for i in range(1, n_labels):
            assert time_to_seg_id_map[t][i] == f"{i}_{t}"


def test_match_iou():
    # Bad input
    with pytest.raises(ValueError):
        match_iou("not tracking data", "not tracking data")

    # shapes don't match
    with pytest.raises(ValueError):
        match_iou(
            TrackingGraph(nx.DiGraph(), segmentation=np.zeros((5, 10, 10))),
            TrackingGraph(nx.DiGraph(), segmentation=np.zeros((5, 10, 5))),
        )

    # Test 2d data
    n_frames = 3
    n_labels = 3
    track_graph = get_movie_with_graph(ndims=3, n_frames=n_frames, n_labels=n_labels)
    mapper = match_iou(
        track_graph,
        track_graph,
    )

    # Check for correct number of pairs
    assert len(mapper) == n_frames * n_labels
    # gt and pred node should be the same
    for pair in mapper:
        assert pair[0] == pair[1]

    # Check 3d data
    track_graph = get_movie_with_graph(ndims=4, n_frames=n_frames, n_labels=n_labels)
    mapper = match_iou(
        track_graph,
        track_graph,
    )

    # Check for correct number of pairs
    assert len(mapper) == n_frames * n_labels
    # gt and pred node should be the same
    for pair in mapper:
        assert pair[0] == pair[1]


class TestIOUMatched:
    def test__init__(self):
        # No segmentation
        track_graph = get_movie_with_graph()
        data = TrackingGraph(track_graph.graph)

        matcher = IOUMatcher()

        with pytest.raises(ValueError):
            matcher.compute_mapping(data, data)

    def test_compute_mapping(self):
        # Test 2d data
        n_frames = 3
        n_labels = 3
        track_graph = get_movie_with_graph(
            ndims=3, n_frames=n_frames, n_labels=n_labels
        )

        matcher = IOUMatcher()
        matched = matcher.compute_mapping(gt_graph=track_graph, pred_graph=track_graph)

        # Check for correct number of pairs
        assert len(matched.mapping) == n_frames * n_labels
        # gt and pred node should be the same
        for pair in matched.mapping:
            assert pair[0] == pair[1]
