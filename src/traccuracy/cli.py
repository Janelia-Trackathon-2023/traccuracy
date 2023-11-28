import json
import logging
from typing import Optional

import typer

from traccuracy import run_metrics
from traccuracy.loaders import load_ctc_data

logger = logging.getLogger(__name__)

app = typer.Typer()


def load_all_ctc(
    gt_dir: str,
    pred_dir: str,
    gt_track_path: Optional[str] = None,
    pred_track_path: Optional[str] = None,
):
    gt_data = load_ctc_data(gt_dir, gt_track_path)
    pred_data = load_ctc_data(pred_dir, pred_track_path)
    return gt_data, pred_data


@app.command()
def run_ctc(
    gt_dir: str = typer.Argument(..., help="Path to GT tiffs", show_default=False),
    pred_dir: str = typer.Argument(
        ..., help="Path to prediction/RES tiffs", show_default=False
    ),
    gt_track_path: Optional[str] = typer.Option(
        None, help="Path to ctc gt track file", show_default=False
    ),
    pred_track_path: Optional[str] = typer.Option(
        None, help="Path to predicted track file", show_default=False
    ),
    loader: str = typer.Option("ctc", help="Loader to bring data into memory"),
    out_path: str = typer.Option("ctc_log.json", help="Path to save results"),
):
    """
    Run TRA and DET metric on gt and pred data using CTC matching.

    If --gt_track_path and --pred_track_path are not passed, we find ``*_track.txt``
    files in the data directories. If more than one such file is present, or
    no such files are present, an error is raised.

    Results will be dumped to --out_path in JSON format.

    Raises ValueError: if any --loader besides ctc is passed.
    """
    from traccuracy.matchers import CTCMatcher
    from traccuracy.metrics import CTCMetrics

    if loader != "ctc":
        raise ValueError(
            f"Only cell tracking challenge (ctc) loader is available, but {loader} was passed."
        )
    gt_data, pred_data = load_all_ctc(gt_dir, pred_dir, gt_track_path, pred_track_path)
    result = run_metrics(gt_data, pred_data, CTCMatcher(), [CTCMetrics()])
    with open(out_path, "w") as fp:
        json.dump(result, fp)
    logger.info(f'TRA: {result[0]["results"]["TRA"]}')
    logger.info(f'DET: {result[0]["results"]["DET"]}')


@app.command()
def run_aogm(
    gt_dir: str = typer.Argument(..., help="Path to GT tiffs", show_default=False),
    pred_dir: str = typer.Argument(
        ..., help="Path to prediction/RES tiffs", show_default=False
    ),
    gt_track_path: Optional[str] = typer.Option(
        None, help="Path to ctc gt track file", show_default=False
    ),
    pred_track_path: Optional[str] = typer.Option(
        None, help="Path to predicted track file", show_default=False
    ),
    loader: str = typer.Option("ctc", help="Loader to bring data into memory"),
    out_path: str = typer.Option("aogm_log.json", help="Path to save results"),
    vertex_ns_weight: float = typer.Option(
        1, help="Weight to assign to nonsplit vertex errors"
    ),
    vertex_fp_weight: float = typer.Option(
        1, help="Weight to assign to false positive vertex errors"
    ),
    vertex_fn_weight: float = typer.Option(
        1, help="Weight to assign to false negative vertex errors"
    ),
    edge_fp_weight: float = typer.Option(
        1, help="Weight to assign to false positive edge errors"
    ),
    edge_fn_weight: float = typer.Option(
        1, help="Weight to assign to false negative edge errors"
    ),
    edge_ws_weight: float = typer.Option(
        1, help="Weight to assign to edges with incorrect semantics"
    ),
):
    """Run general AOGM measure on gt and pred data using CTC matching.

    If gt_track_path and pred_track_path are not passed, we find ``*_track.txt``
    files in the data directories. If more than one such file is present, or
    no such files are present, an error is raised.

    Optionally, weights for each error type can be passed.

    Results will be dumped to out_path in JSON format.

    Raises ValueError: if any --loader besides ctc is passed.
    """
    from traccuracy.matchers import CTCMatcher
    from traccuracy.metrics import AOGMMetrics

    if loader != "ctc":
        raise ValueError(
            f"Only cell tracking challenge (ctc) loader is available, but {loader} was passed."
        )
    gt_data, pred_data = load_all_ctc(gt_dir, pred_dir, gt_track_path, pred_track_path)
    result = run_metrics(
        gt_data,
        pred_data,
        CTCMatcher(),
        [
            AOGMMetrics(
                vertex_ns_weight=vertex_ns_weight,
                vertex_fp_weight=vertex_fp_weight,
                vertex_fn_weight=vertex_fn_weight,
                edge_fp_weight=edge_fp_weight,
                edge_fn_weight=edge_fn_weight,
                edge_ws_weight=edge_ws_weight,
            )
        ],
    )
    with open(out_path, "w") as fp:
        json.dump(result, fp)
    logger.info(f'AOGM: {result[0]["results"]["AOGM"]}')


@app.command()
def run_divisions_on_iou(
    gt_dir: str = typer.Argument(..., help="Path to GT tiffs", show_default=False),
    pred_dir: str = typer.Argument(
        ..., help="Path to prediction/RES tiffs", show_default=False
    ),
    gt_track_path: Optional[str] = typer.Option(
        None, help="Path to ctc gt track file", show_default=False
    ),
    pred_track_path: Optional[str] = typer.Option(
        None, help="Path to predicted track file", show_default=False
    ),
    loader: str = typer.Option("ctc", help="Loader to bring data into memory"),
    out_path: str = typer.Option("div_log_iou.json", help="Path to save results"),
    match_threshold: float = typer.Option(
        1,
        help="Threshold above which the intersection over union of a gt and predicted"
        " detection match. Default of 1 requires exact matching.",
    ),
    frame_buffer: int = typer.Option(
        0,
        help="Number of frames to use for division tolerance."
        " Numbers greater than 0 will produce metrics for 0...n inclusive.",
    ),
):
    """Run division metrics on gt and pred data using IOU matching.

    If --gt_track_path and --pred_track_path are not passed, we find ``*_track.txt``
    files in the data directories. If more than one such file is present, or
    no such files are present, an error is raised.

    Optionally, a --match_threshold and --frame_buffer can be passed.

    Results will be dumped to --out_path in JSON format.

    Raises ValueError: if any --loader besides ctc is passed.
    """
    from traccuracy.matchers import IOUMatcher
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
        IOUMatcher(iou_threshold=match_threshold),
        [DivisionMetrics(frame_buffer=frame_buffer_tuple)],
    )
    with open(out_path, "w") as fp:
        json.dump(result, fp)
    res_str = ""
    for frame_buffer, res_dict in result[0]["results"].items():
        res_str += f'{frame_buffer} F1: {res_dict["Division F1"]}\n'
    logger.info(res_str)


@app.command()
def run_divisions_on_ctc(
    gt_dir: str = typer.Argument(..., help="Path to GT tiffs", show_default=False),
    pred_dir: str = typer.Argument(
        ..., help="Path to prediction/RES tiffs", show_default=False
    ),
    gt_track_path: Optional[str] = typer.Option(
        None, help="Path to ctc gt track file", show_default=False
    ),
    pred_track_path: Optional[str] = typer.Option(
        None, help="Path to predicted track file", show_default=False
    ),
    loader: str = typer.Option("ctc", help="Loader to bring data into memory"),
    out_path: str = typer.Option("div_log_ctc.json", help="Path to save results"),
    frame_buffer: int = typer.Option(
        0,
        help="Number of frames to use for division tolerance."
        " Numbers greater than 0 will produce metrics for 0...n inclusive.",
    ),
):
    """Run division metrics on gt and pred data using CTC matching.

    If --gt_track_path and --pred_track_path are not passed, we find ``*_track.txt``
    files in the data directories. If more than one such file is present, or
    no such files are present, an error is raised.

    Optionally, a --frame_buffer can be passed.

    Results will be dumped to --out_path in JSON format.

    Raises ValueError: if any --loader besides ctc is passed.
    """
    from traccuracy.matchers import CTCMatcher
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
        CTCMatcher(),
        [DivisionMetrics(frame_buffer=frame_buffer_tuple)],
    )
    with open(out_path, "w") as fp:
        json.dump(result, fp)
    res_str = ""
    for frame_buffer, res_dict in result[0]["results"].items():
        res_str += f'{frame_buffer} F1: {res_dict["Division F1"]}\n'
    logger.info(res_str)


typer_click_object = typer.main.get_command(app)


def main():
    app()
