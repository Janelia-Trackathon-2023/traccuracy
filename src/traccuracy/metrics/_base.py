from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from traccuracy.matchers._matched import Matched


class Metric(ABC):
    # Mapping criteria
    needs_one_to_one = False
    supports_one_to_many = False
    supports_many_to_one = False
    supports_many_to_many = False

    def __init__(self, matched_data: "Matched"):
        """Add Matched class which takes TrackingData objects for gt and pred,and computes matching

        Each current matching method will be a subclass of Matched e.g. CTCMatched or IOUMatched.
        The Matched objects will store both gt and pred data, as well as the mapping,
        and any additional private attributes that may be needed/used e.g. detection matrices.
        Metric subclasses will take keyword arguments to set the weights of various error counts.

        Args:
            matched_data (Matched): Matched object for set of GT and Pred data
        """
        self.data = matched_data
        self.results = self.compute()

    @abstractmethod
    def compute(self) -> dict:
        """The compute methods of Metric objects return a dictionary with counts and statistics.

        They may make use of TrackingEvents objects but do not have to.

        Raises:
            NotImplementedError

        Returns:
            dict: Dictionary of metric names and int/float values
        """
        raise NotImplementedError
