from traccuracy._tracking_graph import EdgeAttr, NodeAttr, TrackingGraph
from traccuracy.matchers._base import Matched
from traccuracy.matchers._ctc import CTCMatcher
from traccuracy.metrics._ctc import CTCMetrics
from tests.test_utils import get_movie_with_graph, get_gap_close_graphs


def test_compute_mapping():
    # Test 2d data
    n_frames = 3
    n_labels = 3
    track_graph = get_movie_with_graph(ndims=3, n_frames=n_frames, n_labels=n_labels)

    matched = CTCMatcher().compute_mapping(gt_graph=track_graph, pred_graph=track_graph)
    results = CTCMetrics().compute(matched)
    assert results
    assert "TRA" in results
    assert "DET" in results
    assert results["TRA"] == 1
    assert results["DET"] == 1

def test_compute_metrics_gap_close():
    g_gt, g_pred, mapper = get_gap_close_graphs()
    matched = Matched(gt_graph=TrackingGraph(g_gt), pred_graph=TrackingGraph(g_pred), mapping=mapper)
    results = CTCMetrics().compute(matched)

    # check that missing gap closing edge is false negative
    assert g_gt.edges[("1_1", "2_3")][EdgeAttr.FALSE_NEG]
    # check that "extra" node is FP
    assert g_pred.nodes["1_2"][NodeAttr.FALSE_POS]
    # check that correct edge is not annotated with errors
    for error_attr in [EdgeAttr.FALSE_POS, EdgeAttr.WRONG_SEMANTIC]:
        assert not g_pred.edges[("2_6", "4_10")][error_attr]