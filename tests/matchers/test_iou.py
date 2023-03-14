import networkx as nx
import numpy as np
import pytest
from cell_tracking_metrics.matchers.iou import IOUMatched, _match_nodes, match_iou
from cell_tracking_metrics.tracking_data import TrackingData
from cell_tracking_metrics.tracking_graph import TrackingGraph

from .test_utils import get_annotated_image, get_annotated_movie


def test_match_nodes():
    # Check shape error
    bad_shape = (2, 10, 10)
    with pytest.raises(ValueError):
        _match_nodes(np.zeros(bad_shape), np.zeros(bad_shape))

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


def get_movie_with_graph(ndims=3, n_frames=3, n_labels=3):
    movie = get_annotated_movie(
        labels_per_frame=n_labels, frames=n_frames, mov_type="repeated"
    )

    # Extend to 3d if needed
    if ndims == 4:
        movie = np.stack([movie, movie, movie], axis=-1)

    # We can assume each object is present and connected across each frame
    G = nx.DiGraph()
    for t in range(n_frames - 1):
        for i in range(1, n_labels + 1):
            G.add_edge(f"{i}_{t}", f"{i}_{t+1}")

    attrs = {}
    for t in range(n_frames):
        for i in range(1, n_labels + 1):
            a = {"t": t, "y": 0, "x": 0, "segmentation_id": i}
            if ndims == 4:
                a["z"] = 0
            attrs[f"{i}_{t}"] = a
    nx.set_node_attributes(G, attrs)

    return TrackingGraph(G), movie


def test_match_iou():
    # Bad input
    with pytest.raises(ValueError):
        match_iou("not tracking data", "not tracking data")

    # shapes don't match
    with pytest.raises(ValueError):
        match_iou(
            TrackingData(
                tracking_graph=nx.DiGraph(), segmentation=np.zeros((5, 10, 10))
            ),
            TrackingData(
                tracking_graph=nx.DiGraph(), segmentation=np.zeros((5, 10, 5))
            ),
        )

    # Test 2d data
    n_frames = 3
    n_labels = 3
    G, movie = get_movie_with_graph(ndims=3, n_frames=n_frames, n_labels=n_labels)
    mapper = match_iou(
        TrackingData(tracking_graph=G, segmentation=movie),
        TrackingData(tracking_graph=G, segmentation=movie),
    )

    # Check for correct number of pairs
    assert len(mapper) == n_frames * n_labels
    # gt and pred node should be the same
    for pair in mapper:
        assert pair[0] == pair[1]

    # Check 3d data
    G, movie = get_movie_with_graph(ndims=4, n_frames=n_frames, n_labels=n_labels)
    mapper = match_iou(
        TrackingData(tracking_graph=G, segmentation=movie),
        TrackingData(tracking_graph=G, segmentation=movie),
    )

    # Check for correct number of pairs
    assert len(mapper) == n_frames * n_labels
    # gt and pred node should be the same
    for pair in mapper:
        assert pair[0] == pair[1]


class TestIOUMatched:
    def test__init__(self):
        # No segmentation
        G, _ = get_movie_with_graph()
        data = TrackingData(G)

        with pytest.raises(ValueError):
            IOUMatched(data, data)

    def test_compute_mapping(self):
        # Test 2d data
        n_frames = 3
        n_labels = 3
        G, movie = get_movie_with_graph(ndims=3, n_frames=n_frames, n_labels=n_labels)

        matched = IOUMatched(
            gt_data=TrackingData(G, movie), pred_data=TrackingData(G, movie)
        )

        # Check for correct number of pairs
        assert len(matched.mapping) == n_frames * n_labels
        # gt and pred node should be the same
        for pair in matched.mapping:
            assert pair[0] == pair[1]
