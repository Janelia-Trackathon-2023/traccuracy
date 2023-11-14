import networkx as nx
import numpy as np
import pytest
from traccuracy._tracking_graph import TrackingGraph
from traccuracy.matchers._ctc import CTCMatcher

from tests.test_utils import get_annotated_movie


def test_match_ctc():
    matcher = CTCMatcher()

    # shapes don't match
    with pytest.raises(ValueError):
        matcher.compute_mapping(
            TrackingGraph(nx.DiGraph(), segmentation=np.zeros((5, 10, 10))),
            TrackingGraph(nx.DiGraph(), segmentation=np.zeros((5, 10, 5))),
        )

    n_labels = 3
    n_frames = 3
    movie = get_annotated_movie(
        labels_per_frame=n_labels, frames=n_frames, mov_type="repeated"
    )

    # We can assume each object is present and connected across each frame
    g = nx.DiGraph()
    for t in range(n_frames - 1):
        for i in range(1, n_labels + 1):
            g.add_edge(f"{i}_{t}", f"{i}_{t+1}")

    attrs = {}
    for t in range(n_frames):
        for i in range(1, n_labels + 1):
            attrs[f"{i}_{t}"] = {"t": t, "y": 0, "x": 0, "segmentation_id": i}
    nx.set_node_attributes(g, attrs)

    matched = matcher.compute_mapping(
        TrackingGraph(g, segmentation=movie),
        TrackingGraph(g, segmentation=movie),
    )

    # Check for correct number of pairs
    assert len(matched.mapping) == n_frames * n_labels

    # gt and pred node should be the same
    for pair in matched.mapping:
        assert pair[0] == pair[1]
