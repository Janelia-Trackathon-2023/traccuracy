from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from traccuracy import __version__

if TYPE_CHECKING:
    from traccuracy.matchers import Matched


class Metric(ABC):
    """The base class for Metrics

    Data should be passed directly into the compute method
    Kwargs should be specified in the constructor
    """

    # Mapping criteria
    needs_one_to_one = False
    supports_one_to_many = False
    supports_many_to_one = False
    supports_many_to_many = False

    @abstractmethod
    def _compute(self, matched: Matched) -> dict:
        """The compute methods of Metric objects return a dictionary with counts and statistics.

        Raises:
            NotImplementedError

        Returns:
            dict: Dictionary of metric names and int/float values
        """
        raise NotImplementedError

    def compute(self, matched: Matched) -> Results:
        """The compute methods of Metric objects returns a Results object populated with results
        and associated metadata

        Args:
            matched (Matched): Matched data object to compute metrics on

        Returns:
            Results: Object containing metric results and associated pipeline metadata
        """

        res_dict = self._compute(matched)

        results = Results(
            results=res_dict,
            matcher_info=matched.matcher_info,
            metric_info=self.info,
            gt_name=matched.gt_graph.name,
            pred_name=matched.pred_graph.name,
        )
        return results

    @property
    def info(self):
        """Dictionary with Matcher name and any parameters"""
        return {"name": self.__class__.__name__, **self.__dict__}


class Results:
    """The Results object collects information about the pipeline used
    to generate the metric results

    Args:
        results (optional, dict): Dictionary with metric output
        matcher_info (optional, dict): Dictionary with matcher name and parameters
        metric_info (optional, dict): Dictionary with metric name and parameters
        gt_name (optional, str): Name of the ground truth data
        pred_name (optional, str): Name of the predicted data
    """

    def __init__(
        self,
        results: dict | None = None,
        matcher_info: dict | None = None,
        metric_info: dict | None = None,
        gt_name: str | None = None,
        pred_name: str | None = None,
    ):
        self.results = results
        self.matcher_info = matcher_info
        self.metric_info = metric_info
        self.gt_name = gt_name
        self.pred_name = pred_name

    @property
    def version(self) -> str:
        """Return current traccuracy version"""
        return __version__

    def to_dict(self):
        """Returns all attributes that are not None as a dictionary

        Returns:
            dict: Dictionary of Results attributes
        """
        output = {"version": self.version}
        if self.results:
            output["results"] = self.results
        if self.matcher_info:
            output["matcher"] = self.matcher_info
        if self.metric_info:
            output["metric"] = self.metric_info
        if self.gt_name:
            output["gt"] = self.gt_name
        if self.pred_name:
            output["pred"] = self.pred_name

        return output
