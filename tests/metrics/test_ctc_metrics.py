import networkx as nx
from traccuracy._tracking_data import TrackingData
from traccuracy.matchers._ctc import CTCMatched
from traccuracy.metrics._ctc import CTCMetrics

from tests.test_utils import get_movie_with_graph


def test_compute_mapping():
    # Test 2d data
    n_frames = 3
    n_labels = 3
    G, movie = get_movie_with_graph(ndims=3, n_frames=n_frames, n_labels=n_labels)
    nx.set_edge_attributes(G.graph, 0, "is_intertrack_edge")

    matched = CTCMatched(
        gt_data=TrackingData(G, movie), pred_data=TrackingData(G, movie)
    )
    metric = CTCMetrics(matched)
    assert metric.results
    assert "TRA" in metric.results
    assert "DET" in metric.results
    assert metric.results["TRA"] == 1
    assert metric.results["DET"] == 1
