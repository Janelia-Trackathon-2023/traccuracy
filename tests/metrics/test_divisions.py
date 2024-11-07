import os
from pathlib import Path

import pytest
from traccuracy import TrackingGraph
from traccuracy.loaders import load_ctc_data
from traccuracy.matchers import CTCMatcher, IOUMatcher, Matched
from traccuracy.metrics._divisions import DivisionMetrics

from tests.test_utils import download_gt_data, get_division_graphs

ROOT_DIR = Path(__file__).resolve().parents[2]


@pytest.fixture(scope="module")
def download_gt_hela():
    url = "http://data.celltrackingchallenge.net/training-datasets/Fluo-N2DL-HeLa.zip"
    download_gt_data(url, ROOT_DIR)


@pytest.fixture(scope="function")
def gt_hela():
    path = "downloads/Fluo-N2DL-HeLa/01_GT/TRA"
    return load_ctc_data(
        os.path.join(ROOT_DIR, path),
        os.path.join(ROOT_DIR, path, "man_track.txt"),
    )


@pytest.fixture(scope="function")
def pred_hela():
    path = "examples/sample-data/Fluo-N2DL-HeLa/01_RES"
    return load_ctc_data(
        os.path.join(ROOT_DIR, path),
        os.path.join(ROOT_DIR, path, "res_track.txt"),
    )


def test_ctc_div_metrics(gt_hela, pred_hela):
    ctc_matched = CTCMatcher().compute_mapping(gt_hela, pred_hela)
    div_results = DivisionMetrics().compute(ctc_matched)

    assert div_results.results["Frame Buffer 0"]["False Negative Divisions"] == 18
    assert div_results.results["Frame Buffer 0"]["False Positive Divisions"] == 30
    assert div_results.results["Frame Buffer 0"]["True Positive Divisions"] == 76


def test_iou_div_metrics(gt_hela, pred_hela):
    iou_matched = IOUMatcher(iou_threshold=0.1).compute_mapping(gt_hela, pred_hela)
    div_results = DivisionMetrics().compute(iou_matched)

    assert div_results.results["Frame Buffer 0"]["False Negative Divisions"] == 25
    assert div_results.results["Frame Buffer 0"]["False Positive Divisions"] == 31
    assert div_results.results["Frame Buffer 0"]["True Positive Divisions"] == 69


def test_DivisionMetrics():
    g_gt, g_pred, map_gt, map_pred = get_division_graphs()
    mapper = list(zip(map_gt, map_pred))
    matched = Matched(
        TrackingGraph(g_gt),
        TrackingGraph(g_pred),
        mapper,
    )
    frame_buffer = 2

    results = DivisionMetrics(max_frame_buffer=frame_buffer)._compute(matched)

    for name, r in results.items():
        buffer = int(name[-1:])
        assert buffer in list(range(frame_buffer + 1))
        if buffer in (0, 1):
            # No corrections
            assert r["True Positive Divisions"] == 0
            assert r["False Positive Divisions"] == 1
            assert r["False Negative Divisions"] == 1
        else:
            # Correction
            assert r["True Positive Divisions"] == 1
            assert r["False Positive Divisions"] == 0
            assert r["False Negative Divisions"] == 0
