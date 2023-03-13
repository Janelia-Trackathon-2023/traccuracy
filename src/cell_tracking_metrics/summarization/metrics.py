from abc import ABC, abstractmethod


class Metrics(ABC):
    def __init__(self, track_events, ground_truth=None, prediction=None, matches=None):
        """A class to compute metrics/summary statistics for a tracking solution.

        Multiple metrics can be computed in the same class for efficiency.
        However, some metrics are incompatible with each other due to requirements for the matching,
        and should be in different classes. Each class should document assumptions about
        the matching and/or track events that are necessary for the metrics to be valid.

        Args:
            track_events (TrackEvents): A set of event counts for a tracking solution.
            ground_truth Optional(TrackingGraph): Ground truth tracking graph with
                false negative nodes, edges, and divisions annotated. Defaults to None.
            prediction Optional(TrackingGraph): Prediction tracking graph with
                false positive nodes, edges, and divisions annotated. Defaults to None
            matches Optional(list[gt_node_id, pred_node_id]]): List of 2-tuples of node_ids that 
                represent matchings of gt and prediction nodes. Defaults to None.
        """
        self.track_events = track_events
        self.ground_truth = ground_truth
        self.prediction = prediction
        self.matches = matches

    @abstractmethod
    def compute_metrics(self):
        """Computes the metrics described by this particular metrics object.

        The set of metrics are saved in self.metrics and returned
        Returns:
            dict: a map from strings (metric names) to values (usually floats, but can be anything)
        """
        raise NotImplementedError()