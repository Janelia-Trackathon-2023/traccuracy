import os
from pathlib import Path

import pytest
import numpy as np
import networkx as nx

from tests.test_utils import download_gt_data, get_division_graphs
import tests.examples.graphs as ex_graphs
from traccuracy import TrackingGraph
from traccuracy.loaders import load_ctc_data
from traccuracy.matchers import IOUMatcher, Matched
from traccuracy.metrics._divisions import DivisionMetrics

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


def test_iou_div_metrics(gt_hela, pred_hela):
    # Fail validation if one-to-one not enabled
    iou_matched = IOUMatcher(iou_threshold=0.1).compute_mapping(gt_hela, pred_hela)
    with pytest.raises(TypeError):
        div_results = DivisionMetrics().compute(iou_matched)

    iou_matched = IOUMatcher(iou_threshold=0.1, one_to_one=True).compute_mapping(
        gt_hela, pred_hela
    )
    div_results = DivisionMetrics().compute(iou_matched)

    assert div_results.results["Frame Buffer 0"]["False Negative Divisions"] == 19
    assert div_results.results["Frame Buffer 0"]["False Positive Divisions"] == 31
    assert div_results.results["Frame Buffer 0"]["True Positive Divisions"] == 69
    assert div_results.results["Frame Buffer 0"]["Wrong Children Divisions"] == 6


def test_DivisionMetrics():
    g_gt, g_pred, map_gt, map_pred = get_division_graphs()
    mapper = list(zip(map_gt, map_pred))
    matched = Matched(
        TrackingGraph(g_gt), TrackingGraph(g_pred), mapper, {"name": "DummyMatcher"}
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

class TestDivisionMetrics:
    def test_no_divisions(self):
        matched = ex_graphs.good_matched()
        results = DivisionMetrics()._compute(matched)

        metrics = [
            "Division Recall",
            "Division Precision",
            "Division F1",
            "Mitotic Branching Correctness"
        ]
        for m in metrics:
            assert np.isnan(results['Frame Buffer 0'][m])

    def test_fp_no_gt(self, caplog):
        matched = Matched(
            TrackingGraph(nx.DiGraph()),
            ex_graphs.basic_division(0),
            [],
            {}
        )
        results = DivisionMetrics()._compute(matched)['Frame Buffer 0']
        assert "No ground truth divisions present. Metrics may return np.nan" in caplog.text

        # FP so some nan some 0
        assert np.isnan(results["Division Recall"])
        assert results["Division Precision"] == 0
        assert np.isnan(results["Division F1"])
        assert results["Mitotic Branching Correctness"] == 0

    def test_frame_buffer(self):
        matched = ex_graphs.div_1late_end()
        results = DivisionMetrics(max_frame_buffer=1)._compute(matched)

        # Check TP changed with frame buffer
        assert results['Frame Buffer 0']['True Positive Divisions'] == 0
        assert results['Frame Buffer 1']['True Positive Divisions'] == 1