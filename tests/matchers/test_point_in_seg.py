import networkx as nx
import pytest
from skimage.measure import regionprops
from traccuracy._tracking_graph import TrackingGraph
from traccuracy.matchers._point_in_seg import (
    GTPointInSegMatcher,
    PredPointInSegMatcher,
    match_point_in_seg,
)

from tests.test_utils import get_annotated_image, get_movie_with_graph


def test_match_point_in_seg():
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
        centroid = regionprop.centroid  # [z,] y, x
        for label, value in zip(pos_labels, centroid):
            attrs[label] = value
        pred_graph.add_node(node_id, **attrs)

    # remove one node
    to_remove = list(pred_graph.nodes)[num_labels - 1]
    pred_graph.remove_node(to_remove)

    # duplicate one node
    to_dup = next(iter(pred_graph.nodes))
    data_to_dup = {
        "t": pred_graph.nodes[to_dup]["t"],
        "y": pred_graph.nodes[to_dup]["y"],
        "x": pred_graph.nodes[to_dup]["x"],
    }
    pred_graph.add_node(i + 1, **data_to_dup)

    # add FP node
    # TODO


def test_match_point_in_seg_2d():
    # Test 2d data
    n_frames = 3
    n_labels = 3
    track_graph = get_movie_with_graph(ndims=3, n_frames=n_frames, n_labels=n_labels)
    mapper = match_point_in_seg(
        track_graph,
        track_graph,
    )

    # Check for correct number of pairs
    assert len(mapper) == n_frames * n_labels
    # gt and pred node should be the same
    for pair in mapper:
        assert pair[0] == pair[1]


def test_match_point_in_seg_3d():
    # Check 3d data
    n_frames = 3
    n_labels = 3
    track_graph = get_movie_with_graph(ndims=4, n_frames=n_frames, n_labels=n_labels)
    mapper = match_point_in_seg(
        track_graph,
        track_graph,
    )

    # Check for correct number of pairs
    assert len(mapper) == n_frames * n_labels
    # gt and pred node should be the same
    for pair in mapper:
        assert pair[0] == pair[1]


def test_gt_point_in_seg_matcher():
    matcher = GTPointInSegMatcher()

    n_frames = 3
    n_labels = 3
    seg_track_graph = get_movie_with_graph(
        ndims=4, n_frames=n_frames, n_labels=n_labels
    )
    points_track_graph = TrackingGraph(seg_track_graph.graph)
    with pytest.raises(ValueError):
        # pass in seg as GT and points as prediction
        matcher.compute_mapping(seg_track_graph, points_track_graph)

    matched = matcher.compute_mapping(points_track_graph, seg_track_graph)

    # Check for correct number of pairs
    assert len(matched.mapping) == n_frames * n_labels
    # gt and pred node should be the same
    for pair in matched.mapping:
        assert pair[0] == pair[1]


def test_pred_point_in_seg_matcher():
    matcher = PredPointInSegMatcher()

    n_frames = 3
    n_labels = 3
    seg_track_graph = get_movie_with_graph(
        ndims=4, n_frames=n_frames, n_labels=n_labels
    )
    points_track_graph = TrackingGraph(seg_track_graph.graph)
    with pytest.raises(ValueError):
        # pass in seg as pred and points as GT
        matcher.compute_mapping(points_track_graph, seg_track_graph)

    matched = matcher.compute_mapping(seg_track_graph, points_track_graph)

    # Check for correct number of pairs
    assert len(matched.mapping) == n_frames * n_labels
    # gt and pred node should be the same
    for pair in matched.mapping:
        assert pair[0] == pair[1]
