import copy
import os
from pathlib import Path

import pandas as pd
import pytest
from traccuracy.loaders import (
    _check_ctc,
    _get_node_attributes,
    _load_tiffs,
    load_ctc_data,
)
from traccuracy.matchers import CTCMatcher, IOUMatcher
from traccuracy.metrics import CTCMetrics, DivisionMetrics

from tests.test_utils import download_gt_data, gt_data

ROOT_DIR = Path(__file__).resolve().parents[1]
TIMEOUT = 20


@pytest.fixture(scope="module")
def gt_data_2d():
    url = "http://data.celltrackingchallenge.net/training-datasets/PhC-C2DL-PSC.zip"
    path = "downloads/Fluo-N2DL-HeLa/01_GT/TRA"
    return gt_data(url, ROOT_DIR, path)


@pytest.fixture(scope="module")
def gt_data_3d():
    url = "http://data.celltrackingchallenge.net/training-datasets/Fluo-N3DH-CE.zip"
    path = "downloads/Fluo-N3DH-CE/01_GT/TRA"
    return gt_data(url, ROOT_DIR, path)


@pytest.fixture(scope="module")
def pred_data_2d(gt_data_2d):
    # For now this is also GT data.
    return copy.deepcopy(gt_data_2d)


@pytest.fixture(scope="module")
def pred_data_3d(gt_data_3d):
    # For now this is also GT data.
    return copy.deepcopy(gt_data_3d)


@pytest.fixture(scope="module")
def ctc_matched_2d(gt_data_2d, pred_data_2d):
    return CTCMatcher().compute_mapping(gt_data_2d, pred_data_2d)


@pytest.fixture(scope="module")
def ctc_matched_3d(gt_data_3d, pred_data_3d):
    return CTCMatcher().compute_mapping(gt_data_3d, pred_data_3d)


@pytest.fixture(scope="module")
def iou_matched_2d(gt_data_2d, pred_data_2d):
    return IOUMatcher(iou_threshold=0.1).compute_mapping(gt_data_2d, pred_data_2d)


@pytest.fixture(scope="module")
def iou_matched_3d(gt_data_3d, pred_data_3d):
    return IOUMatcher(iou_threshold=0.1).compute_mapping(gt_data_3d, pred_data_3d)


@pytest.mark.parametrize(
    "dataset",
    ["Fluo-N2DL-HeLa", "Fluo-N3DH-CE"],
    ids=["2d", "3d"],
)
def test_load_gt_ctc_data(
    benchmark,
    dataset,
):
    url = f"http://data.celltrackingchallenge.net/training-datasets/{dataset}.zip"
    path = f"downloads/{dataset}/01_GT/TRA"
    download_gt_data(url, ROOT_DIR)

    benchmark.pedantic(
        load_ctc_data,
        args=(
            os.path.join(ROOT_DIR, path),
            os.path.join(ROOT_DIR, path, "man_track.txt"),
        ),
        kwargs={"run_checks": False},
        rounds=1,
        iterations=1,
    )


# TODO Add 3d results
@pytest.mark.parametrize(
    "path",
    [
        "examples/sample-data/Fluo-N2DL-HeLa/01_RES",
    ],
    ids=["2d"],
)
def test_load_pred_ctc_data(benchmark, path):
    benchmark.pedantic(
        load_ctc_data,
        args=(
            os.path.join(ROOT_DIR, path),
            os.path.join(ROOT_DIR, path, "res_track.txt"),
        ),
        kwargs={"run_checks": False},
        rounds=1,
        iterations=1,
    )


def test_ctc_checks(benchmark):
    names = ["Cell_ID", "Start", "End", "Parent_ID"]

    tracks = pd.read_csv(
        os.path.join(
            ROOT_DIR, "examples/sample-data/Fluo-N2DL-HeLa/01_RES/res_track.txt"
        ),
        header=None,
        sep=" ",
        names=names,
    )

    masks = _load_tiffs(
        os.path.join(ROOT_DIR, "examples/sample-data/Fluo-N2DL-HeLa/01_RES")
    )
    detections = _get_node_attributes(masks)
    benchmark(_check_ctc, tracks, detections, masks)


@pytest.mark.parametrize(
    "gt_data,pred_data",
    [
        ("gt_data_2d", "pred_data_2d"),
        ("gt_data_3d", "pred_data_3d"),
    ],
    ids=["2d", "3d"],
)
def test_ctc_matcher(benchmark, gt_data, pred_data, request):
    gt_data = request.getfixturevalue(gt_data)
    pred_data = request.getfixturevalue(pred_data)
    benchmark.pedantic(
        CTCMatcher().compute_mapping,
        args=(gt_data, pred_data),
        rounds=1,
        iterations=1,
    )


@pytest.mark.parametrize(
    "ctc_matched",
    ["ctc_matched_2d", "ctc_matched_3d"],
    ids=["2d", "3d"],
)
def test_ctc_metrics(benchmark, ctc_matched, request):
    ctc_matched = request.getfixturevalue(ctc_matched)

    def run_compute():
        return CTCMetrics().compute(copy.deepcopy(ctc_matched))

    benchmark.pedantic(run_compute, rounds=1, iterations=1)


@pytest.mark.xfail
@pytest.mark.timeout(TIMEOUT)
@pytest.mark.parametrize(
    "gt_data,pred_data",
    [
        ("gt_data_2d", "pred_data_2d"),
        ("gt_data_3d", "pred_data_3d"),
    ],
    ids=["2d", "3d"],
)
def test_iou_matcher(benchmark, gt_data, pred_data):
    benchmark.pedantic(
        IOUMatcher(iou_threshold=0.1).compute_mapping,
        args=(gt_data, pred_data),
        rounds=1,
        iterations=1,
    )


@pytest.mark.xfail
@pytest.mark.timeout(TIMEOUT)
@pytest.mark.parametrize(
    "iou_matched",
    ["iou_matched_2d", "iou_matched_3d"],
    ids=["2d", "3d"],
)
def test_iou_div_metrics(benchmark, iou_matched):
    def run_compute():
        return DivisionMetrics().compute(copy.deepcopy(iou_matched))

    benchmark.pedantic(run_compute, rounds=1, iterations=1)
