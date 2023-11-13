from __future__ import annotations

import copy
import logging
from abc import ABC, abstractmethod
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

        # Copy graphs to avoid possible changes to graphs while computing mapping
        matched = self._compute_mapping(
            copy.deepcopy(gt_graph), copy.deepcopy(pred_graph)
        )

        # Report matching performance
        total_gt = len(matched.gt_graph.nodes())
        matched_gt = len({m[0] for m in matched.mapping})
        total_pred = len(matched.pred_graph.nodes())
        matched_pred = len({m[1] for m in matched.mapping})
        logger.info(f"Matched {matched_gt} out of {total_gt} ground truth nodes.")
        logger.info(f"Matched {matched_pred} out of {total_pred} predicted nodes.")

        return matched

    @abstractmethod
    def _compute_mapping(
        self, gt_graph: TrackingGraph, pred_graph: TrackingGraph
    ) -> Matched:
        """Computes a mapping of nodes in gt to nodes in pred and returns a Matched object

        Raises:
            NotImplementedError
        """
        raise NotImplementedError


class Matched:
    """Matched data class which stores TrackingGraph objects for gt and pred
    and the computed mapping

    Each TrackingGraph will be a new copy of the original object

    Args:
        gt_graph (traccuracy.TrackingGraph): Tracking graph object for the gt
        pred_graph (traccuracy.TrackingGraph): Tracking graph object for the pred
        mapping (list[tuple[Any, Any]]): List of tuples where each tuple maps
            a gt node to a pred node
    """

    def __init__(
        self,
        gt_graph: TrackingGraph,
        pred_graph: TrackingGraph,
        mapping: list[tuple[Any, Any]],
    ):
        self.gt_graph = gt_graph
        self.pred_graph = pred_graph
        self.mapping = mapping
