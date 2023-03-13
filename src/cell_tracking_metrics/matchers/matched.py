from abc import ABC, abstractmethod

from ..tracking_data import TrackingData


class Matched(ABC):
    def __init__(self, gt_data: "TrackingData", pred_data: "TrackingData"):
        self.gt_data = gt_data
        self.pred_data = pred_data

        self._mapping = None

    @abstractmethod
    def compute_mapping(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def mapping(self):
        if self._mapping is None:
            self.compute_mapping()
        return self._mapping
