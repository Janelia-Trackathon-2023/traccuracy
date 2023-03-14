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


def validate_matcher_choice(gt_data, pred_data, matcher, metrics):
    """Validate that given matcher supports requirements of each metric.

    Args:
        gt_data (TrackingData): ground truth graph and optionally segmentation
        pred_data (TrackingData): predicted graph and optionally segmentation
        matcher (Matched): matching class to use to create correspondence
        metrics (List[Metric]): list of metrics to compute as class names
    """
    ...
