import copy
import os
import urllib.request
import zipfile

import pytest
from traccuracy.loaders import load_ctc_data
from traccuracy.matchers import CTCMatched, IOUMatched
from traccuracy.metrics import CTCMetrics, DivisionMetrics

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def download_gt_data():
    # Download GT data -- look into cacheing this in github actions
    url = "http://data.celltrackingchallenge.net/training-datasets/Fluo-N2DL-HeLa.zip"
    data_dir = "downloads"

    if not os.path.exists(data_dir):
        os.mkdir(data_dir)

    filename = url.split("/")[-1]
    file_path = os.path.join(data_dir, filename)

    if not os.path.exists(file_path):
        urllib.request.urlretrieve(url, file_path)

        # Unzip the data
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall(data_dir)


@pytest.fixture
def gt_data():
    download_gt_data()
    return load_ctc_data(
        "downloads/Fluo-N2DL-HeLa/01_GT/TRA",
        "downloads/Fluo-N2DL-HeLa/01_GT/TRA/man_track.txt",
    )


@pytest.fixture
def pred_data():
    return load_ctc_data(
        os.path.join(ROOT_DIR, "examples/sample-data/Fluo-N2DL-HeLa/01_RES"),
        os.path.join(
            ROOT_DIR, "examples/sample-data/Fluo-N2DL-HeLa/01_RES/res_track.txt"
        ),
    )


@pytest.fixture
def ctc_matched(gt_data, pred_data):
    return CTCMatched(gt_data, pred_data)


@pytest.fixture
def iou_matched(gt_data, pred_data):
    return IOUMatched(gt_data, pred_data, iou_threshold=0.1)


def test_load_gt_data(benchmark):
    download_gt_data()
    benchmark(
        load_ctc_data,
        "downloads/Fluo-N2DL-HeLa/01_GT/TRA",
        "downloads/Fluo-N2DL-HeLa/01_GT/TRA/man_track.txt",
    )


def test_load_pred_data(benchmark):
    benchmark(
        load_ctc_data,
        "../examples/sample-data/Fluo-N2DL-HeLa/01_RES",
        "../examples/sample-data/Fluo-N2DL-HeLa/01_RES/res_track.txt",
    )


def test_ctc_matched(benchmark, gt_data, pred_data):
    benchmark(CTCMatched, gt_data, pred_data)


def test_ctc_metrics(benchmark, ctc_matched):
    def run_compute():
        return CTCMetrics(copy.deepcopy(ctc_matched)).compute()

    ctc_results = benchmark.pedantic(run_compute, rounds=1, iterations=1)

    assert ctc_results["fn_edges"] == 87
    assert ctc_results["fn_nodes"] == 39
    assert ctc_results["fp_edges"] == 60
    assert ctc_results["fp_nodes"] == 0
    assert ctc_results["ns_nodes"] == 0
    assert ctc_results["ws_edges"] == 51


def test_ctc_div_metrics(benchmark, ctc_matched):
    def run_compute():
        return DivisionMetrics(copy.deepcopy(ctc_matched)).compute()

    div_results = benchmark(run_compute)

    assert div_results["Frame Buffer 0"]["False Negative Divisions"] == 18
    assert div_results["Frame Buffer 0"]["False Positive Divisions"] == 30
    assert div_results["Frame Buffer 0"]["True Positive Divisions"] == 76


def test_iou_matched(benchmark, gt_data, pred_data):
    benchmark(IOUMatched, gt_data, pred_data, iou_threshold=0.5)


def test_iou_div_metrics(benchmark, iou_matched):
    def run_compute():
        return DivisionMetrics(copy.deepcopy(iou_matched)).compute()

    div_results = benchmark(run_compute)

    assert div_results["Frame Buffer 0"]["False Negative Divisions"] == 25
    assert div_results["Frame Buffer 0"]["False Positive Divisions"] == 31
    assert div_results["Frame Buffer 0"]["True Positive Divisions"] == 69
