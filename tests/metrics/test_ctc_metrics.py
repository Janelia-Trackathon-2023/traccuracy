import os
from pathlib import Path

import pytest

from tests.test_utils import get_gap_close_graphs, get_movie_with_graph, gt_data
from traccuracy import EdgeFlag, NodeFlag, TrackingGraph
from traccuracy.loaders import load_ctc_data
from traccuracy.matchers import CTCMatcher, Matched
from traccuracy.metrics import CTCMetrics

ROOT_DIR = Path(__file__).resolve().parents[2]


@pytest.fixture(scope="module")
def gt_hela():
    url = "http://data.celltrackingchallenge.net/training-datasets/Fluo-N2DL-HeLa.zip"
    path = "downloads/Fluo-N2DL-HeLa/01_GT/TRA"
    return gt_data(url, ROOT_DIR, path)


@pytest.fixture(scope="module")
def pred_hela():
    path = "examples/sample-data/Fluo-N2DL-HeLa/01_RES"
    return load_ctc_data(
        os.path.join(ROOT_DIR, path),
        os.path.join(ROOT_DIR, path, "res_track.txt"),
    )


def test_ctc_metrics(gt_hela, pred_hela):
    ctc_matched = CTCMatcher().compute_mapping(gt_hela, pred_hela)
    ctc_results = CTCMetrics().compute(ctc_matched)

    assert ctc_results.results["fn_edges"] == 87
    assert ctc_results.results["fn_nodes"] == 39
    assert ctc_results.results["fp_edges"] == 60
    assert ctc_results.results["fp_nodes"] == 0
    assert ctc_results.results["ns_nodes"] == 0
    assert ctc_results.results["ws_edges"] == 47


def test_compute_mapping():
    # Test 2d data
    n_frames = 3
    n_labels = 3
    track_graph = get_movie_with_graph(ndims=3, n_frames=n_frames, n_labels=n_labels)

    matched = CTCMatcher().compute_mapping(gt_graph=track_graph, pred_graph=track_graph)
    results = CTCMetrics()._compute(matched)
    assert results
    assert "TRA" in results
    assert "DET" in results
    assert results["TRA"] == 1
    assert results["DET"] == 1


def test_compute_metrics_gap_close():
    g_gt, g_pred, gt_mapped, g_pred_mapped = get_gap_close_graphs()
    mapper = list(zip(gt_mapped, g_pred_mapped))
    matched = Matched(
        gt_graph=TrackingGraph(g_gt),
        pred_graph=TrackingGraph(g_pred),
        mapping=mapper,
        matcher_info={"name": "DummyMatcher"},
    )
    CTCMetrics().compute(matched)

    # check that missing gap closing edge is false negative
    assert g_gt.edges[("1_1", "2_3")][EdgeFlag.CTC_FALSE_NEG]
    # check that "extra" node is FP
    assert g_pred.nodes["1_2"][NodeFlag.CTC_FALSE_POS]
    # check that correct edge is not annotated with errors
    for error_attr in [EdgeFlag.CTC_FALSE_POS, EdgeFlag.WRONG_SEMANTIC]:
        assert error_attr not in g_pred.edges[("2_6", "4_10")]
