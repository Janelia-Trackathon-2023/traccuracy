import logging
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from traccuracy._tracking_graph import TrackingGraph

logger = logging.getLogger(__name__)


class Matched(ABC):
    def __init__(self, gt_graph: "TrackingGraph", pred_graph: "TrackingGraph"):
        """Matched class which takes TrackingData objects for gt and pred, and computes matching.

        Each current matching method will be a subclass of Matched e.g. CTCMatched or IOUMatched.
        The Matched objects will store both gt and pred data, as well as the mapping,
        and any additional private attributes that may be needed/used e.g. detection matrices.

        Args:
            gt_graph (TrackingGraph): Tracking graph object for the gt
            pred_graph (TrackingGraph): Tracking graph object for the pred
        """
        self.gt_graph = gt_graph
        self.pred_graph = pred_graph

        self.mapping = self.compute_mapping()

        # Report matching performance
        total_gt = len(self.gt_graph.nodes())
        matched_gt = len({m[0] for m in self.mapping})
        total_pred = len(self.pred_graph.nodes())
        matched_pred = len({m[1] for m in self.mapping})
        logger.info(f"Matched {matched_gt} out of {total_gt} ground truth nodes.")
        logger.info(f"Matched {matched_pred} out of {total_pred} predicted nodes.")

    @abstractmethod
    def compute_mapping(self):
        """Computes a mapping of nodes in gt to nodes in pred

        The mapping must be a list of tuples, e.g. [(gt_node, pred_node)]

        Raises:
            NotImplementedError
        """
        raise NotImplementedError
