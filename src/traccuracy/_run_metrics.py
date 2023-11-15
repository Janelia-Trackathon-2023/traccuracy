from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Dict, List

    from traccuracy import TrackingGraph
    from traccuracy.matchers._base import Matcher
    from traccuracy.metrics._base import Metric


def run_metrics(
    gt_data: "TrackingGraph",
    pred_data: "TrackingGraph",
    matcher: "Matcher",
    metrics: "List[Metric]",
) -> "Dict":
    """Compute given metrics on data using the given matcher.

    The returned result dictionary will contain all metrics computed by
    the given Metric classes, as well as general summary numbers
    e.g. false positive/false negative detection and edge counts.

    Args:
        gt_data (TrackingGraph): ground truth graph and optionally segmentation
        pred_data (TrackingGraph): predicted graph and optionally segmentation
        matcher (traccuracy.matchers.Matcher): instantiated matcher object
        metrics (List[Metric]): list of instantiated metrics objects to compute

    Returns:
        Dict: dictionary of metrics indexed by metric name. Dictionary will be
            nested for metrics that return multiple values.
    """
    matched = matcher.compute_mapping(gt_data, pred_data)
    results = {}
    for _metric in metrics:
        result = _metric.compute(matched)
        results[_metric.__class__.__name__] = result
    return results
