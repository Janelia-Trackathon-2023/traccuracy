from __future__ import annotations

import warnings
from abc import ABC, abstractmethod
from importlib.metadata import version
from typing import TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    from traccuracy.matchers._base import Matched


MATCHING_TYPES = ["one-to-one", "one-to-many", "many-to-one", "many-to-many"]


class Metric(ABC):
    """The base class for Metrics

    Data should be passed directly into the compute method
    Kwargs should be specified in the constructor
    """

    def __init__(self, valid_matches: list):
        # Check that we have gotten a list of valid match types
        if len(valid_matches) == 0:
            raise TypeError("New metrics must provide a list of valid matching types")

        for mtype in valid_matches:
            if mtype not in MATCHING_TYPES:
                raise ValueError(
                    f"Matching type {mtype} is not supported. Choose from {{MATCHING_TYPES}}."
                )

        self.valid_match_types = valid_matches

    def _validate_matcher(self, matched: Matched) -> bool:
        """Verifies that the matched meets the assumptions of the metric
        Returns True if matcher is valid and False if matcher is not valid"""
        if not hasattr(self, "valid_match_types"):
            raise AttributeError("Metric subclass does not define valid_match_types")
        return matched.matching_type in self.valid_match_types

    @abstractmethod
    def _compute(self, matched: Matched) -> dict:
        """The compute methods of Metric objects return a dictionary with counts and statistics.

        Args:
            matched (traccuracy.matchers.Matched): Matched data object to compute metrics on

        Raises:
            NotImplementedError

        Returns:
            dict: Dictionary of metric names and int/float values
        """
        raise NotImplementedError

    def compute(self, matched: Matched, override_matcher: bool = False) -> Results:
        """The compute methods of Metric objects returns a Results object populated with results
        and associated metadata

        Args:
            matched (traccuracy.matchers.Matched): Matched data object to compute metrics on

        Returns:
            Results: Object containing metric results and associated pipeline metadata
        """
        if override_matcher:
            warnings.warn(
                "Overriding matcher/metric validation may result in "
                "unpredictable/incorrect metric results",
                stacklevel=2,
            )
        else:
            valid_matcher = self._validate_matcher(matched)
            if not valid_matcher:
                raise TypeError(
                    "The matched data uses a matcher that does not meet the requirements "
                    "of the metric. Check the documentation for the metric for more information."
                )

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
        """Dictionary with Metric name and any parameters"""
        return {"name": self.__class__.__name__, **self.__dict__}

    def _get_precision(self, numerator, denominator) -> float:
        """Compute precision and return np.nan if denominator is 0

        Args:
            numerator (int): Typically TP
            denominator (int): Typically TP + FP

        Returns:
            float: Precision
        """
        if denominator == 0:
            return np.nan
        return numerator / denominator

    def _get_recall(self, numerator, denominator) -> float:
        """Compute recall and return np.nan if denominator is 0

        Args:
            numerator (int): Typically TP
            denominator (int): Typically TP + FN

        Returns:
            float: Recall
        """
        if denominator == 0:
            return np.nan
        return numerator / denominator

    def _get_f1(self, precision, recall) -> float:
        """Compute F1 and return np.nan if precision and recall both equal 0

        Args:
            precision (float): Precision score
            recall (float): Recall score

        Returns:
            float: F1
        """
        if precision + recall == 0:
            return np.nan
        return 2 * (recall * precision) / (recall + precision)


class Results:
    """The Results object collects information about the pipeline used
    to generate the metric results

    Args:
        results (dict): Dictionary with metric output
        matcher_info (dict): Dictionary with matcher name and parameters
        metric_info (dict): Dictionary with metric name and parameters
        gt_name (optional, str): Name of the ground truth data
        pred_name (optional, str): Name of the predicted data
    """

    def __init__(
        self,
        results: dict,
        matcher_info: dict | None,
        metric_info: dict,
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
        return version("traccuracy")

    def to_dict(self):
        """Returns all attributes that are not None as a dictionary

        Returns:
            dict: Dictionary of Results attributes
        """
        output = {
            "version": self.version,
            "results": self.results,
            "matcher": self.matcher_info,
            "metric": self.metric_info,
        }
        if self.gt_name:
            output["gt"] = self.gt_name
        if self.pred_name:
            output["pred"] = self.pred_name

        return output
