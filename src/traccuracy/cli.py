import json
from typing import Optional

import typer

from traccuracy import run_metrics
from traccuracy.loaders.ctc import load_ctc_data

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
    out_path: "str" = "div_log.json",
    match_threshold: "float" = 1,
    frame_buffer: "int" = 0,
):
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
    out_path: "str" = "div_log.json",
    frame_buffer: "int" = 0,
):
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
