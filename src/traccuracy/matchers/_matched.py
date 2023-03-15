from abc import ABC, abstractmethod

from traccuracy._tracking_data import TrackingData


class Matched(ABC):
    def __init__(self, gt_data: "TrackingData", pred_data: "TrackingData"):
        """Matched class which takes TrackingData objects for gt and pred, and computes matching.

        Each current matching method will be a subclass of Matched e.g. CTCMatched or IOUMatched.
        The Matched objects will store both gt and pred data, as well as the mapping,
        and any additional private attributes that may be needed/used e.g. detection matrices.

        Args:
            gt_data (TrackingData): Tracking data object for the gt
            pred_data (TrackingData): Tracking data object for the pred
        """
        self.gt_data = gt_data
        self.pred_data = pred_data

        self.mapping = self.compute_mapping()

    @abstractmethod
    def compute_mapping(self):
        """Computes a mapping of nodes in gt to nodes in pred

        The mapping must be a list of tuples, e.g. [(gt_node, pred_node)]

        Raises:
            NotImplementedError
        """
        raise NotImplementedError
