import networkx as nx
import numpy as np
import pytest
from traccuracy._tracking_graph import TrackingGraph
from traccuracy.matchers._iou import IOUMatcher, _match_nodes, match_iou

from tests.test_utils import get_annotated_image, get_movie_with_graph


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
