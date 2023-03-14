from typing import TYPE_CHECKING

from traccuracy.utils import get_relevant_kwargs, validate_matched_data

if TYPE_CHECKING:
    from typing import Dict, List, Type

    from traccuracy.matchers.matched import Matched
    from traccuracy.metrics.base import Metric
    from traccuracy.tracking_data import TrackingData


def run_metrics(
    gt_data: "TrackingData",
    pred_data: "TrackingData",
    matcher: "Type[Matched]",
    metrics: "List[Type[Metric]]",
    **kwargs,  # weights
) -> "Dict":
    """Compute given metrics on data using the given matcher.

    An error will be thrown if the given matcher is not compatible with
    all metrics in the given list. The returned result dictionary will
    contain all metrics computed by the given Metric classes, as well as
    general summary numbers e.g. false positive/false negative detection
    and edge counts.

    Args:
        gt_data (TrackingData): ground truth graph and optionally segmentation
        pred_data (TrackingData): predicted graph and optionally segmentation
        matcher (Matched): matching class to use to create correspondence
        metrics (List[Metric]): list of metrics to compute as class names

    Returns:
        Dict: dictionary of metrics indexed by metric name. Dictionary will be
        nested for metrics that return multiple values.
    """
    matched = matcher(gt_data, pred_data)
    validate_matched_data(matched, metrics)
    metric_kwarg_dict = {
        m_class: get_relevant_kwargs(m_class, kwargs) for m_class in metrics
    }
    results = {}
    for _metric in metrics:
        relevant_kwargs = metric_kwarg_dict[_metric]
        result = _metric(matched, **relevant_kwargs)
        results[_metric.__name__] = result
    return results


if __name__ == "__main__":
    from traccuracy.loaders.ctc import load_ctc_data
    from traccuracy.matchers import CTCMatched
    from traccuracy.metrics import CTCMetrics, DivisionMetrics

    gt_data = load_ctc_data(
        "/home/draga/PhD/data/cell_tracking_challenge/Fluo-N2DL-HeLa/01_GT/TRA/",
        "/home/draga/PhD/data/cell_tracking_challenge/Fluo-N2DL-HeLa/01_GT/TRA/man_track.txt",
    )
    res_data = load_ctc_data(
        "/home/draga/PhD/data/cell_tracking_challenge/Fluo-N2DL-HeLa/01_RES/",
        "/home/draga/PhD/data/cell_tracking_challenge/Fluo-N2DL-HeLa/01_RES/res_track.txt",
    )
    results = run_metrics(gt_data, res_data, CTCMatched, [CTCMetrics, DivisionMetrics])
