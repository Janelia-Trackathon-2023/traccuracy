from abc import ABC, abstractmethod

from ..matchers import Matched


class Metric(ABC):
    # Mapping criteria
    needs_det_matrix = False
    needs_one_to_one = False
    supports_one_to_many = False
    supports_many_to_one = False
    supports_many_to_many = False

    def __init__(self, matched_data: "Matched"):
        self.data = matched_data

    @abstractmethod
    def compute(self) -> dict:
        raise NotImplementedError
