import os
from pathlib import Path

import pytest

from tests.test_utils import get_movie_with_graph, gt_data
from traccuracy.loaders import load_ctc_data
from traccuracy.matchers import CTCMatcher
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
