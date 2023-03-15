from typing import Tuple

import typer

from traccuracy import run_metrics
from traccuracy.loaders.ctc import load_ctc_data

app = typer.Typer()


def load_all_ctc(gt_dir, pred_dir, gt_track_path, pred_track_path):
    gt_data = load_ctc_data(gt_dir, gt_track_path)
    pred_data = load_ctc_data(pred_dir, pred_track_path)
    return gt_data, pred_data


@app.command()
def run_ctc(
    gt_dir: "str",
    pred_dir: "str",
    gt_track_path: "str",
    pred_track_path: "str",
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
    run_metrics(gt_data, pred_data, CTCMatched, [CTCMetrics], None)


@app.command()
def run_aogm(
    gt_path: "str",
    pred_path: "str",
    gt_track_path: "str",
    pred_track_path: "str",
    loader: "str" = "ctc",
    out_path: "str" = "ctc_log.json",
    vertex_ns_weight: "float" = 1,
    vertex_fp_weight: "float" = 1,
    vertex_fn_weight: "float" = 1,
    edge_fp_weight: "float" = 1,
    edge_fn_weight: "float" = 1,
    edge_ws_weight: "float" = 1,
):
    pass


@app.command()
def run_divisions(
    gt_path: "str",
    pred_path: "str",
    gt_track_path: "str",
    pred_track_path: "str",
    loader: "str" = "ctc",
    out_path: "str" = "ctc_log.json",
    match_threshold: "float" = 1,
    frame_buffer: "Tuple[int]" = (0,),
):
    pass


if __name__ == "__main__":
    app()
