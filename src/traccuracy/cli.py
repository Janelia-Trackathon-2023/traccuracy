import json
from typing import Optional

import typer

from traccuracy import run_metrics
from traccuracy.loaders import load_ctc_data

app = typer.Typer()


def load_all_ctc(
    gt_dir: "str",
    pred_dir: "str",
    gt_track_path: "Optional[str]" = None,
    pred_track_path: "Optional[str]" = None,
):
    gt_data = load_ctc_data(gt_dir, gt_track_path)
    pred_data = load_ctc_data(pred_dir, pred_track_path)
    return gt_data, pred_data


@app.command()
def run_ctc(
    gt_dir: "str",
    pred_dir: "str",
    gt_track_path: "Optional[str]" = None,
    pred_track_path: "Optional[str]" = None,
    loader: "str" = "ctc",
    out_path: "str" = "ctc_log.json",
):
    """Run TRA and DET metric on gt and pred data using CTC matching.

    If gt_track_path and pred_track_path are not passed, we find *_track.txt
    files in the data directories. If more than one such file is present, or
    no such files are present, an error is raised.

    Results will be dumped to out_path in JSON format.

    Args:
        gt_dir (str): path to GT tiffs
        pred_dir (str): path to prediction/RES tiffs
        gt_track_path (Optional[str], optional): path to ctc gt track file.
        Defaults to None.
        pred_track_path (Optional[str], optional): path to predicted track file.
        Defaults to None.
        loader (str, optional): Loader to bring data into memory. Defaults to "ctc".
        out_path (str, optional): Path to save results. Defaults to "ctc_log.json" in current
        working directory.

    Raises:
        ValueError: if any loader besides ctc is passed.
    """
    from traccuracy.matchers import CTCMatched
    from traccuracy.metrics import CTCMetrics

    if loader != "ctc":
        raise ValueError(
            f"Only cell tracking challenge (ctc) loader is available, but {loader} was passed."
        )
    gt_data, pred_data = load_all_ctc(gt_dir, pred_dir, gt_track_path, pred_track_path)
    result = run_metrics(gt_data, pred_data, CTCMatched, [CTCMetrics])
    with open(out_path, "w") as fp:
        json.dump(result, fp)
    print(f'TRA: {result["CTCMetrics"]["TRA"]}')
    print(f'DET: {result["CTCMetrics"]["DET"]}')


@app.command()
def run_aogm(
    gt_dir: "str",
    pred_dir: "str",
    gt_track_path: "Optional[str]" = None,
    pred_track_path: "Optional[str]" = None,
    loader: "str" = "ctc",
    out_path: "str" = "aogm_log.json",
    vertex_ns_weight: "float" = 1,
    vertex_fp_weight: "float" = 1,
    vertex_fn_weight: "float" = 1,
    edge_fp_weight: "float" = 1,
    edge_fn_weight: "float" = 1,
    edge_ws_weight: "float" = 1,
):
    """Run general AOGM measure on gt and pred data using CTC matching.

    If gt_track_path and pred_track_path are not passed, we find *_track.txt
    files in the data directories. If more than one such file is present, or
    no such files are present, an error is raised.

    Optionally, weights for each error type can be passed.

    Results will be dumped to out_path in JSON format.

    Args:
        gt_dir (str): path to GT tiffs
        pred_dir (str): path to prediction/RES tiffs
        gt_track_path (Optional[str], optional): path to ctc gt track file.
        Defaults to None.
        pred_track_path (Optional[str], optional): path to predicted track file.
        Defaults to None.
        loader (str, optional): Loader to bring data into memory. Defaults to "ctc".
        out_path (str, optional): Path to save results. Defaults to "ctc_log.json" in current
        working directory.
        vertex_ns_weight (float, optional): Weight to assign to nonsplit vertex errors.
        Defaults to 1.
        vertex_fp_weight (float, optional): Weight to assign to false positive vertex errors.
        Defaults to 1.
        vertex_fn_weight (float, optional): Weight to assign to false negative vertex errors.
        Defaults to 1.
        edge_fp_weight (float, optional): Weight to assign to false positive edge errors.
        Defaults to 1.
        edge_fn_weight (float, optional): Weight to assign to false negative edge errors.
        Defaults to 1.
        edge_ws_weight (float, optional): Weight to assign to edges with incorrect semantics.
        Defaults to 1.

    Raises:
        ValueError: if any loader besides ctc is passed.
    """
    from traccuracy.matchers import CTCMatched
    from traccuracy.metrics import AOGMMetrics

    if loader != "ctc":
        raise ValueError(
            f"Only cell tracking challenge (ctc) loader is available, but {loader} was passed."
        )
    gt_data, pred_data = load_all_ctc(gt_dir, pred_dir, gt_track_path, pred_track_path)
    result = run_metrics(
        gt_data,
        pred_data,
        CTCMatched,
        [AOGMMetrics],
        metrics_kwargs={
            "vertex_ns_weight": vertex_ns_weight,
            "vertex_fp_weight": vertex_fp_weight,
            "vertex_fn_weight": vertex_fn_weight,
            "edge_fp_weight": edge_fp_weight,
            "edge_fn_weight": edge_fn_weight,
            "edge_ws_weight": edge_ws_weight,
        },
    )
    with open(out_path, "w") as fp:
        json.dump(result, fp)
    print(f'AOGM: {result["AOGMMetrics"]["AOGM"]}')


@app.command()
def run_divisions_on_iou(
    gt_dir: "str",
    pred_dir: "str",
    gt_track_path: "Optional[str]" = None,
    pred_track_path: "Optional[str]" = None,
    loader: "str" = "ctc",
    out_path: "str" = "div_log_iou.json",
    match_threshold: "float" = 1,
    frame_buffer: "int" = 0,
):
    """Run division metrics on gt and pred data using IOU matching.

    If gt_track_path and pred_track_path are not passed, we find *_track.txt
    files in the data directories. If more than one such file is present, or
    no such files are present, an error is raised.

    Optionally, a match_threshold and frame_buffer can be passed.

    Results will be dumped to out_path in JSON format.

    Args:
        gt_dir (str): path to GT tiffs
        pred_dir (str): path to prediction/RES tiffs
        gt_track_path (Optional[str], optional): path to ctc gt track file.
        Defaults to None.
        pred_track_path (Optional[str], optional): path to predicted track file.
        Defaults to None.
        loader (str, optional): Loader to bring data into memory. Defaults to "ctc".
        out_path (str, optional): Path to save results. Defaults to "ctc_log.json" in current
        working directory.
        match_threshold (float, optional): Threshold above which the intersection over union
        of a gt and predicted detection match. Defaults to 1 requiring exact matching.
        frame_buffer (int, optional): Number of frames to use for division tolerance.
        Defaults to 0. Numbers greater than 0 will produce metrics for 0...n inclusive.

    Raises:
        ValueError: if any loader besides ctc is passed.
    """
    from traccuracy.matchers import IOUMatched
    from traccuracy.metrics import DivisionMetrics

    if loader != "ctc":
        raise ValueError(
            f"Only cell tracking challenge (ctc) loader is available, but {loader} was passed."
        )
    gt_data, pred_data = load_all_ctc(gt_dir, pred_dir, gt_track_path, pred_track_path)
    frame_buffer_tuple = tuple(range(0, frame_buffer + 1))
    result = run_metrics(
        gt_data,
        pred_data,
        IOUMatched,
        [DivisionMetrics],
        matcher_kwargs={"iou_threshold": match_threshold},
        metrics_kwargs={
            "frame_buffer": frame_buffer_tuple,
        },
    )
    with open(out_path, "w") as fp:
        json.dump(result, fp)
    res_str = ""
    for frame_buffer, res_dict in result["DivisionMetrics"].items():
        res_str += f'{frame_buffer} F1: {res_dict["Division F1"]}\n'
    print(res_str)


@app.command()
def run_divisions_on_ctc(
    gt_dir: "str",
    pred_dir: "str",
    gt_track_path: "Optional[str]" = None,
    pred_track_path: "Optional[str]" = None,
    loader: "str" = "ctc",
    out_path: "str" = "div_log_ctc.json",
    frame_buffer: "int" = 0,
):
    """Run division metrics on gt and pred data using CTC matching.

    If gt_track_path and pred_track_path are not passed, we find *_track.txt
    files in the data directories. If more than one such file is present, or
    no such files are present, an error is raised.

    Optionally, a frame_buffer can be passed.

    Results will be dumped to out_path in JSON format.

    Args:
        gt_dir (str): path to GT tiffs
        pred_dir (str): path to prediction/RES tiffs
        gt_track_path (Optional[str], optional): path to ctc gt track file.
        Defaults to None.
        pred_track_path (Optional[str], optional): path to predicted track file.
        Defaults to None.
        loader (str, optional): Loader to bring data into memory. Defaults to "ctc".
        out_path (str, optional): Path to save results. Defaults to "ctc_log.json" in current
        working directory.
        frame_buffer (int, optional): Number of frames to use for division tolerance.
        Defaults to 0. Numbers greater than 0 will produce metrics for 0...n inclusive.

    Raises:
        ValueError: if any loader besides ctc is passed.
    """
    from traccuracy.matchers import CTCMatched
    from traccuracy.metrics import DivisionMetrics

    if loader != "ctc":
        raise ValueError(
            f"Only cell tracking challenge (ctc) loader is available, but {loader} was passed."
        )
    gt_data, pred_data = load_all_ctc(gt_dir, pred_dir, gt_track_path, pred_track_path)
    frame_buffer_tuple = tuple(range(0, frame_buffer + 1))
    result = run_metrics(
        gt_data,
        pred_data,
        CTCMatched,
        [DivisionMetrics],
        metrics_kwargs={
            "frame_buffer": frame_buffer_tuple,
        },
    )
    with open(out_path, "w") as fp:
        json.dump(result, fp)
    res_str = ""
    for frame_buffer, res_dict in result["DivisionMetrics"].items():
        res_str += f'{frame_buffer} F1: {res_dict["Division F1"]}\n'
    print(res_str)


def main():
    app()
