import copy
import os
import urllib.request
import zipfile

import pytest
from traccuracy.loaders import load_ctc_data
from traccuracy.matchers import CTCMatched, IOUMatched
from traccuracy.metrics import CTCMetrics, DivisionMetrics

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TIMEOUT_2D = 20
TIMEOUT_3D = 30


def download_gt_data(url):
    # Download GT data -- look into cacheing this in github actions
    data_dir = os.path.join(ROOT_DIR, "downloads")

    if not os.path.exists(data_dir):
        os.mkdir(data_dir)

    filename = url.split("/")[-1]
    file_path = os.path.join(data_dir, filename)

    if not os.path.exists(file_path):
        urllib.request.urlretrieve(url, file_path)

        # Unzip the data
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall(data_dir)


def gt_data(url, path):
    download_gt_data(url)
    return load_ctc_data(
        os.path.join(ROOT_DIR, path),
        os.path.join(ROOT_DIR, path, "man_track.txt"),
    )


@pytest.fixture(scope="module")
def gt_data_2d():
    url = "http://data.celltrackingchallenge.net/training-datasets/Fluo-N2DL-HeLa.zip"
    path = "downloads/Fluo-N2DL-HeLa/01_GT/TRA"
    return gt_data(url, path)


@pytest.fixture(scope="module")
def gt_data_3d():
    url = "http://data.celltrackingchallenge.net/training-datasets/Fluo-N3DH-CE.zip"
    path = "downloads/Fluo-N3DH-CE/01_GT/TRA"
    return gt_data(url, path)


@pytest.fixture(scope="module")
def pred_data_2d():
    path = "examples/sample-data/Fluo-N2DL-HeLa/01_RES"
    return load_ctc_data(
        os.path.join(ROOT_DIR, path),
        os.path.join(ROOT_DIR, path, "res_track.txt"),
    )


@pytest.fixture(scope="module")
def pred_data_3d(gt_data_3d):
    # For the time being, this is also GT data.
    return gt_data_3d


@pytest.fixture(scope="module")
def ctc_matched_2d(gt_data_2d, pred_data_2d):
    return CTCMatched(gt_data_2d, pred_data_2d)


@pytest.fixture(scope="module")
def ctc_matched_3d(gt_data_3d, pred_data_3d):
    return CTCMatched(gt_data_3d, pred_data_3d)


@pytest.fixture(scope="module")
def iou_matched_2d(gt_data_2d, pred_data_2d):
    return IOUMatched(gt_data_2d, pred_data_2d, iou_threshold=0.1)


@pytest.fixture(scope="module")
def iou_matched_3d(gt_data_3d, pred_data_3d):
    return IOUMatched(gt_data_3d, pred_data_3d, iou_threshold=0.1)


@pytest.mark.parametrize("dataset", ["Fluo-N2DL-HeLa", "Fluo-N3DH-CE"])
def test_load_gt_ctc_data(
    benchmark,
    dataset,
):
    url = f"http://data.celltrackingchallenge.net/training-datasets/{dataset}.zip"
    path = f"downloads/{dataset}/01_GT/TRA"
    download_gt_data(url)

    benchmark.pedantic(
        load_ctc_data,
        args=(
            os.path.join(ROOT_DIR, path),
            os.path.join(ROOT_DIR, path, "man_track.txt"),
        ),
        rounds=1,
        iterations=1,
    )


# TODO Add 3d results
@pytest.mark.parametrize(
    "path",
    [
        "examples/sample-data/Fluo-N2DL-HeLa/01_RES",
    ],
)
def test_load_pred_ctc_data(benchmark, path):
    benchmark.pedantic(
        load_ctc_data,
        args=(
            os.path.join(ROOT_DIR, path),
            os.path.join(ROOT_DIR, path, "res_track.txt"),
        ),
        rounds=1,
        iterations=1,
    )


@pytest.mark.timeout(TIMEOUT_2D)
def test_ctc_matched_2d(benchmark, gt_data_2d, pred_data_2d):
    benchmark.pedantic(
        CTCMatched,
        args=(gt_data_2d, pred_data_2d),
        rounds=1,
        iterations=1,
    )


@pytest.mark.xfail
@pytest.mark.timeout(TIMEOUT_3D)
def test_ctc_matched_3d(benchmark, gt_data_3d, pred_data_3d):
    benchmark.pedantic(
        CTCMatched,
        args=(gt_data_3d, pred_data_3d),
        rounds=1,
        iterations=1,
    )


@pytest.mark.timeout(TIMEOUT_2D)
def test_ctc_metrics_2d(benchmark, ctc_matched_2d):
    def run_compute():
        return CTCMetrics(copy.deepcopy(ctc_matched_2d)).compute()

    ctc_results = benchmark.pedantic(run_compute, rounds=1, iterations=1)

    assert ctc_results["fn_edges"] == 87
    assert ctc_results["fn_nodes"] == 39
    assert ctc_results["fp_edges"] == 60
    assert ctc_results["fp_nodes"] == 0
    assert ctc_results["ns_nodes"] == 0
    assert ctc_results["ws_edges"] == 47


@pytest.mark.xfail
@pytest.mark.timeout(TIMEOUT_3D)
def test_ctc_metrics_3d(benchmark, ctc_matched_3d):
    def run_compute():
        return CTCMetrics(copy.deepcopy(ctc_matched_3d)).compute()

    benchmark.pedantic(run_compute, rounds=1, iterations=1)


@pytest.mark.timeout(TIMEOUT_2D)
def test_ctc_div_metrics_2d(benchmark, ctc_matched_2d):
    def run_compute():
        return DivisionMetrics(copy.deepcopy(ctc_matched_2d)).compute()

    div_results = benchmark.pedantic(run_compute, rounds=1, iterations=1)

    assert div_results["Frame Buffer 0"]["False Negative Divisions"] == 18
    assert div_results["Frame Buffer 0"]["False Positive Divisions"] == 30
    assert div_results["Frame Buffer 0"]["True Positive Divisions"] == 76


@pytest.mark.xfail
@pytest.mark.timeout(TIMEOUT_3D)
def test_ctc_div_metrics_3d(benchmark, ctc_matched_3d):
    def run_compute():
        return DivisionMetrics(copy.deepcopy(ctc_matched_3d)).compute()

    benchmark.pedantic(run_compute, rounds=1, iterations=1)


@pytest.mark.timeout(TIMEOUT_2D)
def test_iou_matched_2d(benchmark, gt_data_2d, pred_data_2d):
    benchmark.pedantic(
        IOUMatched,
        args=(gt_data_2d, pred_data_2d),
        kwargs={"iou_threshold": 0.5},
        rounds=1,
        iterations=1,
    )


@pytest.mark.xfail
@pytest.mark.timeout(TIMEOUT_3D)
def test_iou_matched_3d(benchmark, gt_data_3d, pred_data_3d):
    benchmark.pedantic(
        IOUMatched,
        args=(gt_data_3d, pred_data_3d),
        kwargs={"iou_threshold": 0.5},
        rounds=1,
        iterations=1,
    )


@pytest.mark.timeout(TIMEOUT_2D)
def test_iou_div_metrics_2d(benchmark, iou_matched_2d):
    def run_compute():
        return DivisionMetrics(copy.deepcopy(iou_matched_2d)).compute()

    div_results = benchmark.pedantic(run_compute, rounds=1, iterations=1)

    assert div_results["Frame Buffer 0"]["False Negative Divisions"] == 25
    assert div_results["Frame Buffer 0"]["False Positive Divisions"] == 31
    assert div_results["Frame Buffer 0"]["True Positive Divisions"] == 69


@pytest.mark.xfail
@pytest.mark.timeout(TIMEOUT_3D)
def test_iou_div_metrics_3d(benchmark, iou_matched_3d):
    def run_compute():
        return DivisionMetrics(copy.deepcopy(iou_matched_3d)).compute()

    benchmark.pedantic(run_compute, rounds=1, iterations=1)
