import networkx as nx
import numpy as np
import pytest
from skimage.measure import regionprops
from traccuracy._tracking_graph import TrackingGraph
from traccuracy.matchers._iou import (
    IOUMatcher,
    _construct_time_to_seg_id_map,
    match_iou,
)

from tests.test_utils import get_annotated_image, get_movie_with_graph


def test__points_to_seg():
    # creat dummy image to test against
    num_labels = 5
    y1 = get_annotated_image(img_size=256, num_labels=num_labels, seed=1)
    t = 1
    # get centroids
    pred_graph = nx.DiGraph()
    props = regionprops(y1)
    for i, regionprop in enumerate(props):
        node_id = i
        attrs = {"t": t}
        pos_labels = ["y", "x"]
        for label, value in zip(pos_labels, centroid):
            attrs[label] = value
        centroid = regionprop.centroid  # [z,] y, x
        pred_graph.add_node(node_id, **attrs)

    # remove one node
    to_remove = list(pred_graph.nodes)[num_labels - 1]
    pred_graph.remove_node(to_remove)

    # duplicate one node
    to_dup = list(pred_graph.nodes)[0]
    data_to_dup = {
        "t": pred_graph.nodes[to_dup]["t"],
        "y": pred_graph.nodes[to_dup]["y"],
        "x": pred_graph.nodes[to_dup]["x"],
    }
    pred_graph.add_node(i + 1, **data_to_dup)

    # add FP node
    # TODO


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
