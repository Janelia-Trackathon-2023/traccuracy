from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from collections import defaultdict
from typing import Any

from traccuracy._tracking_graph import TrackingGraph

logger = logging.getLogger(__name__)


class Matcher(ABC):
    """The Matcher base class provides a wrapper around the compute_mapping method

    Each Matcher subclass will implement its own kwargs as needed.
    In use, the Matcher object will be initialized with kwargs prior to running compute_mapping
    on a particular dataset
    """

    def compute_mapping(
        self, gt_graph: TrackingGraph, pred_graph: TrackingGraph
    ) -> Matched:
        """Run the matching on a given set of gt and pred TrackingGraph and returns a Matched object
        with a new copy of each TrackingGraph

        Args:
            gt_graph (traccuracy.TrackingGraph): Tracking graph object for the gt
            pred_graph (traccuracy.TrackingGraph): Tracking graph object for the pred

        Returns:
            matched (Matched): Matched data object

        Raises:
            ValueError: gt and pred must be a TrackingGraph object
        """
        if not isinstance(gt_graph, TrackingGraph) or not isinstance(
            pred_graph, TrackingGraph
        ):
            raise ValueError(
                "Input data must be a TrackingData object with a graph and segmentations"
            )

        mapping = self._compute_mapping(gt_graph, pred_graph)
        matched = Matched(gt_graph, pred_graph, mapping, self.info)

        # Report matching performance
        total_gt = len(matched.gt_graph.nodes)
        matched_gt = len(matched.gt_pred_map.keys())
        total_pred = len(matched.pred_graph.nodes)
        matched_pred = len(matched.pred_gt_map.keys())
        logger.info(f"Matched {matched_gt} out of {total_gt} ground truth nodes.")
        logger.info(f"Matched {matched_pred} out of {total_pred} predicted nodes.")

        return matched

    @abstractmethod
    def _compute_mapping(
        self, gt_graph: TrackingGraph, pred_graph: TrackingGraph
    ) -> list[tuple[Any, Any]]:
        """Computes a mapping of nodes in gt to nodes in pred and returns a mapping

        Returns:
            mapping: list of tuples

        Raises:
            NotImplementedError
        """
        raise NotImplementedError

    @property
    def info(self):
        """Dictionary of Matcher name and any parameters"""
        return {"name": self.__class__.__name__, **self.__dict__}


class Matched:
    """Matched data class which stores TrackingGraph objects for gt and pred
    and the computed mapping

    Each TrackingGraph will be a new copy of the original object

    Args:
        gt_graph (traccuracy.TrackingGraph): Tracking graph object for the gt
        pred_graph (traccuracy.TrackingGraph): Tracking graph object for the pred
        mapping (list[tuple[Any, Any]]): List of tuples where each tuple maps
            a gt node to a pred node
        matcher_info (dict): Dictionary containing name and parameters from
            the matcher that generated the mapping
    """

    def __init__(
        self,
        gt_graph: TrackingGraph,
        pred_graph: TrackingGraph,
        mapping: list[tuple[Any, Any]],
        matcher_info: dict,
    ):
        self.gt_graph = gt_graph
        self.pred_graph = pred_graph
        self.mapping = mapping
        self.matcher_info = matcher_info

        gt_pred_map = defaultdict(list)
        pred_gt_map = defaultdict(list)
        for gt_id, pred_id in mapping:
            pred_gt_map[pred_id].append(gt_id)
            gt_pred_map[gt_id].append(pred_id)

        # Set back to normal dict to remove default dict behavior
        self.gt_pred_map = dict(gt_pred_map)
        self.pred_gt_map = dict(pred_gt_map)
