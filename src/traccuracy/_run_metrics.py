from typing import TYPE_CHECKING

# from traccuracy import TrackingGraph
# from traccuracy.matchers._base import Matcher
# from traccuracy.metrics._base import Metric

if TYPE_CHECKING:
    from typing import Dict, List


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
        gt_data (traccuracy.TrackingGraph): ground truth graph and optionally segmentation
        pred_data (traccuracy.TrackingGraph): predicted graph and optionally segmentation
        matcher (Matcher): instantiated matcher object
        metrics (List[Metric]): list of instantiated metrics objects to compute

    Returns:
        Dict: dictionary of metrics indexed by metric name. Dictionary will be
            nested for metrics that return multiple values.
    """
    # if not isinstance(gt_data, TrackingGraph) or not isinstance(pred_data, TrackingGraph):
    #     raise TypeError("gt_data and pred_data must be TrackingGraph objects")

    # if not isinstance(matcher, Matcher):
    #     raise TypeError("matcher must be an instantiated Matcher object")

    # if not all([isinstance(m, Metric) for m in metrics]):
    #     raise TypeError("metrics must be a list of instantiated Metric objects")

    matched = matcher.compute_mapping(gt_data, pred_data)
    results = []
    for _metric in metrics:
        result = _metric.compute(matched)
        report = {_metric.__class__.__name__: result, "parameters": _metric.__dict__}
        results.append(report)
    return results
