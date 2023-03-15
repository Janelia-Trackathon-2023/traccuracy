import networkx as nx
import numpy as np
import pytest
from traccuracy._tracking_data import TrackingData
from traccuracy._tracking_graph import TrackingGraph
from traccuracy.matchers._ctc import CTCMatched, get_node_matching_map

from tests.test_utils import get_annotated_movie


def test_match_ctc():
    # Bad input
    with pytest.raises(ValueError):
        CTCMatched("not tracking data", "not tracking data")

    # shapes don't match
    with pytest.raises(ValueError):
        CTCMatched(
            TrackingData(
                tracking_graph=nx.DiGraph(), segmentation=np.zeros((5, 10, 10))
            ),
            TrackingData(
                tracking_graph=nx.DiGraph(), segmentation=np.zeros((5, 10, 5))
            ),
        )

    n_labels = 3
    n_frames = 3
    movie = get_annotated_movie(
        labels_per_frame=n_labels, frames=n_frames, mov_type="repeated"
    )

    # We can assume each object is present and connected across each frame
    G = nx.DiGraph()
    for t in range(n_frames - 1):
        for i in range(1, n_labels + 1):
            G.add_edge(f"{i}_{t}", f"{i}_{t+1}")

    attrs = {}
    for t in range(n_frames):
        for i in range(1, n_labels + 1):
            attrs[f"{i}_{t}"] = {"t": t, "y": 0, "x": 0, "segmentation_id": i}
    nx.set_node_attributes(G, attrs)

    G = TrackingGraph(G)

    matched = CTCMatched(
        TrackingData(tracking_graph=G, segmentation=movie),
        TrackingData(tracking_graph=G, segmentation=movie),
    )

    # Check for correct number of pairs
    assert len(matched.mapping) == n_frames * n_labels

    # gt and pred node should be the same
    for pair in matched.mapping:
        assert pair[0] == pair[1]

    # there should be something saved in detection matrices
    assert matched._det_matrices


def test_get_node_matching_map():
    comp_ids = [3, 7, 10]
    gt_ids = [4, 12, 14, 15]
    mtrix = np.zeros((3, 4), dtype=np.uint8)
    mtrix[0, 1] = 1
    mtrix[0, 3] = 1
    mtrix[1, 2] = 1
    mtrix_dict = {0: {"det": mtrix, "comp_ids": comp_ids, "gt_ids": gt_ids}}
    matching = get_node_matching_map(mtrix_dict)
    assert matching == [(12, 3), (15, 3), (14, 7)]


def test_get_node_matching_map_multiple_frames():
    comp_ids = [3, 7, 10]
    gt_ids = [4, 12, 14, 15]
    mtrix = np.zeros((3, 4), dtype=np.uint8)
    mtrix[0, 1] = 1
    mtrix[0, 3] = 1
    mtrix[1, 2] = 1

    mtrix2 = np.zeros((3, 4), dtype=np.uint8)
    mtrix2[1, 1] = 1
    mtrix2[2, 0] = 1
    mtrix_dict = {
        0: {"det": mtrix, "comp_ids": comp_ids, "gt_ids": gt_ids},
        1: {"det": mtrix2, "comp_ids": comp_ids, "gt_ids": gt_ids},
    }
    matching = get_node_matching_map(mtrix_dict)
    assert matching == [(12, 3), (15, 3), (14, 7), (12, 7), (4, 10)]
