from collections import Counter

import networkx as nx
import numpy as np
import pytest

import tests.examples.segs as ex_segs
from tests.test_utils import get_movie_with_graph
from traccuracy._tracking_graph import TrackingGraph
from traccuracy.matchers._iou import (
    IOUMatcher,
    _construct_time_to_seg_id_map,
    _match_nodes,
    match_iou,
)


class Test__match_nodes:
    @pytest.mark.parametrize(
        "data_fxn",
        [ex_segs.good_segmentation_2d, ex_segs.good_segmentation_3d],
        ids=["2D", "3D"],
    )
    def test_good_seg(self, data_fxn):
        gt, pred = data_fxn()
        expected_matches = [(1, 2)]

        # Low threshold
        gtcells, rescells = _match_nodes(gt, pred, threshold=0.4)
        assert Counter(expected_matches) == Counter(list(zip(gtcells, rescells)))

        # Low threshold one_to_one
        gtcells, rescells = _match_nodes(gt, pred, threshold=0.4, one_to_one=True)
        assert Counter(expected_matches) == Counter(list(zip(gtcells, rescells)))

        # High threshold -- no matches
        gtcells, rescells = _match_nodes(gt, pred, threshold=0.9)
        expected_matches = []
        assert Counter(expected_matches) == Counter(list(zip(gtcells, rescells)))

    @pytest.mark.parametrize(
        "data_fxn",
        [
            ex_segs.false_positive_segmentation_2d,
            ex_segs.false_positive_segmentation_3d,
        ],
        ids=["2D", "3D"],
    )
    def test_false_pos(self, data_fxn):
        gt, pred = data_fxn()
        expected_matches = []

        gtcells, rescells = _match_nodes(gt, pred)
        assert Counter(expected_matches) == Counter(list(zip(gtcells, rescells)))

    @pytest.mark.parametrize(
        "data_fxn",
        [
            ex_segs.false_negative_segmentation_2d,
            ex_segs.false_negative_segmentation_3d,
        ],
        ids=["2D", "3D"],
    )
    def test_false_neg(self, data_fxn):
        gt, pred = data_fxn()
        expected_matches = []

        gtcells, rescells = _match_nodes(gt, pred)
        assert Counter(expected_matches) == Counter(list(zip(gtcells, rescells)))

    @pytest.mark.parametrize(
        "data_fxn",
        [ex_segs.oversegmentation_2d, ex_segs.oversegmentation_3d],
        ids=["2D", "3D"],
    )
    def test_split(self, data_fxn):
        gt, pred = data_fxn()

        # Low threshold, both match
        expected_matches = [(1, 2), (1, 3)]
        gtcells, rescells = _match_nodes(gt, pred, threshold=0.3)
        assert Counter(expected_matches) == Counter(list(zip(gtcells, rescells)))

        # High threshold, no match
        expected_matches = []
        gtcells, rescells = _match_nodes(gt, pred, threshold=0.7)
        assert Counter(expected_matches) == Counter(list(zip(gtcells, rescells)))

        # Low threshold, one to one, only one matches
        gtcells, rescells = _match_nodes(gt, pred, threshold=0.3, one_to_one=True)
        computed_matches = list(zip(gtcells, rescells))
        assert ((1, 2) in computed_matches) != ((1, 3) in computed_matches)

    @pytest.mark.parametrize(
        "data_fxn",
        [ex_segs.undersegmentation_2d, ex_segs.undersegmentation_3d],
        ids=["2D", "3D"],
    )
    def test_merge(self, data_fxn):
        gt, pred = data_fxn()

        # Low threshold, both match
        expected_matches = [(1, 3), (2, 3)]
        gtcells, rescells = _match_nodes(gt, pred, threshold=0.3)
        assert Counter(expected_matches) == Counter(list(zip(gtcells, rescells)))

        # High threshold, no match
        expected_matches = []
        gtcells, rescells = _match_nodes(gt, pred, threshold=0.7)
        assert Counter(expected_matches) == Counter(list(zip(gtcells, rescells)))

        # Low threshold, one to one, only one matches
        gtcells, rescells = _match_nodes(gt, pred, threshold=0.3, one_to_one=True)
        computed_matches = list(zip(gtcells, rescells))
        assert ((1, 3) in computed_matches) != ((2, 3) in computed_matches)

    @pytest.mark.parametrize(
        "data_fxn", [ex_segs.multicell_2d, ex_segs.multicell_3d], ids=["2D", "3D"]
    )
    def test_multiple_objects(self, data_fxn):
        gt, pred = data_fxn()
        expected_matches = [(1, 3)]
        gtcells, rescells = _match_nodes(gt, pred)
        assert Counter(expected_matches) == Counter(list(zip(gtcells, rescells)))

    @pytest.mark.parametrize(
        "data_fxn", [ex_segs.no_overlap_2d, ex_segs.no_overlap_3d], ids=["2D", "3D"]
    )
    def test_no_overlap(self, data_fxn):
        gt, pred = data_fxn()
        expected_matches = []
        gtcells, rescells = _match_nodes(gt, pred)
        assert Counter(expected_matches) == Counter(list(zip(gtcells, rescells)))

    def test_input_error(self):
        im = np.zeros((10, 10))
        with pytest.raises(ValueError):
            # Test that threshold 0 is not valid when not one-to-one
            gtcells, rescells = _match_nodes(im, im, threshold=0.0)

    @pytest.mark.parametrize(
        "data_fxn", [ex_segs.no_overlap_2d, ex_segs.no_overlap_3d], ids=["2D", "3D"]
    )
    def test_non_sequential(self, data_fxn):
        # test when the segmentation ids are high numbers (the lower numbers should never appear)
        gt, pred = data_fxn()
        # Change id of segmentation to non sequntial high value
        gt[gt == 1] = 100
        pred[pred == 2] = 200

        expected_matches = []
        gtcells, rescells = _match_nodes(gt, pred)
        assert Counter(expected_matches) == Counter(list(zip(gtcells, rescells)))

        # Check case with one to one threshold 0
        gtcells, rescells = _match_nodes(gt, pred)
        assert Counter(expected_matches) == Counter(list(zip(gtcells, rescells)))


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
