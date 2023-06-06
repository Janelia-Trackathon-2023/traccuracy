import networkx as nx
import numpy as np
import pytest
from traccuracy._tracking_data import TrackingData
from traccuracy._tracking_graph import TrackingGraph
from traccuracy.matchers._ctc import CTCMatched

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
