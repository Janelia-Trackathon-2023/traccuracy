from typing import TYPE_CHECKING

from traccuracy.utils import get_relevant_kwargs, validate_matched_data

if TYPE_CHECKING:
    from typing import Dict, List, Optional, Type

    from traccuracy.matchers.matched import Matched
    from traccuracy.metrics.base import Metric
    from traccuracy.tracking_data import TrackingData


def run_metrics(
    gt_data: "TrackingData",
    pred_data: "TrackingData",
    matcher: "Type[Matched]",
    metrics: "List[Type[Metric]]",
    matcher_kwargs: "Optional[Dict]",
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
        matcher_kwargs (optional, dict): Dictionary of keyword argument for the
            matcher class
        **kwargs: Any keyword args for the Metric classes

    Returns:
        Dict: dictionary of metrics indexed by metric name. Dictionary will be
        nested for metrics that return multiple values.
    """
    matched = matcher(gt_data, pred_data, **matcher_kwargs)
    validate_matched_data(matched, metrics)
    metric_kwarg_dict = {
        m_class: get_relevant_kwargs(m_class, kwargs) for m_class in metrics
    }
    results = {}
    for _metric in metrics:
        relevant_kwargs = metric_kwarg_dict[_metric]
        result = _metric(matched, **relevant_kwargs)
        results[_metric.__name__] = result.results
    return results
