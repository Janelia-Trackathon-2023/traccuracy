import inspect


def find_gt_node_matches(matches, gt_node):
    """For a given gt node, finds all pred nodes that are matches

    Args:
        matches ([(gt_node, pred_node)]): List of tuples of node pairs
        gt_node (hashable): GT node ID
    """
    return [pair[1] for pair in matches if pair[0] == gt_node]


def find_pred_node_matches(matches, pred_node):
    """For a given pred node, finds all gt nodes that are matches

    Args:
        matches ([(gt_node, pred_node)]): List of tuples of node pairs
        pred_node (hashable): pred node ID
    """
    return [pair[0] for pair in matches if pair[1] == pred_node]


def validate_matched_data(matched_data, metrics):
    """Validate that given matcher supports requirements of each metric.

    Args:
        matched_data (traccuracy.matcher.Matched): matching class with mapping between gt and pred
        metrics (List[Metric]): list of metrics to compute as class names
    """
    ...


def get_relevant_kwargs(metric_class, kwargs):
    """Get all params in kwargs that are valid for given metric class.

    If required parameters are not satisfied, an error is raised.

    Args:
        metric_class (Metric): class name of metric to check
        kwargs (dict): dictionary of keyword arguments to validate
    """
    sig = inspect.signature(metric_class)
    relevant_kwargs = {}
    missing_args = []
    for param in sig.parameters.values():
        name = param.name
        is_required = (param.default is param.empty) and name != "matched_data"
        if kwargs and name in kwargs:
            relevant_kwargs[name] = kwargs[name]
        elif is_required:
            missing_args.append(name)
    if missing_args:
        raise ValueError(
            f"Metric class {metric_class.__name__} is missing required"
            + f" arguments: {missing_args}. Add arguments to"
            + " `run_metrics` or consider skipping this metric."
        )
    return relevant_kwargs
