from typing import Any

import numpy as np
from scipy.optimize import linear_sum_assignment
from scipy.spatial import KDTree

from traccuracy._tracking_graph import TrackingGraph

from ._base import Matcher


class PointMatcher(Matcher):
    def __init__(self, threshold: float):
        self.threshold = threshold

    def _compute_mapping(
        self, gt_graph: TrackingGraph, pred_graph: TrackingGraph
    ) -> list[tuple[Any, Any]]:
        mapping: list[tuple[Any, Any]] = []
        if gt_graph.start_frame is None or gt_graph.end_frame is None:
            return mapping
        for frame in range(gt_graph.start_frame, gt_graph.end_frame):
            gt_nodes = list(gt_graph.nodes_by_frame[frame])
            pred_nodes = list(pred_graph.nodes_by_frame.get(frame, []))
            if len(gt_nodes) == 0 or len(pred_nodes) == 0:
                continue

            gt_kdtree = KDTree([gt_graph.get_location(node) for node in gt_nodes])
            pred_kdtree = KDTree([pred_graph.get_location(node) for node in pred_nodes])
            # indices correspond to indices in the gt_nodes, pred_nodes lists
            sdm: dict[tuple[Any, Any], float] = gt_kdtree.sparse_distance_matrix(
                pred_kdtree, max_distance=self.threshold
            )
            # unmapped cost has to be higher than the max distance so if something can
            # be matched it will
            unmapped_cost = self.threshold * 4
            # indices in this matrix correspond to indices in the concatenated gt_nodes
            # + pred_nodes list
            num_gt = len(gt_nodes)
            num_pred = len(pred_nodes)
            total_objects = num_gt + num_pred
            # initialize to unmapped cost + 1
            cost_matrix: np.ndarray = np.ones(shape=(total_objects, total_objects)) * (
                unmapped_cost + 1
            )

            # update costs for those pairs below threshold
            for pair, dist in sdm.items():
                gt_idx, pred_idx = pair
                # put it in the top left corner
                cost_matrix[gt_idx, pred_idx] = dist
                # put the transpose in the bottom right corner
                cost_matrix[-1 * pred_idx, -1 * gt_idx] = dist

            # Calculate unassigned corners, with base cost of 10*unmapped cost
            # Diagonals are set to unmapped_cost
            bot_left = np.full((num_pred, num_pred), unmapped_cost * 10)
            np.fill_diagonal(bot_left, unmapped_cost)
            top_right = np.full((num_gt, num_gt), unmapped_cost * 10)
            np.fill_diagonal(top_right, unmapped_cost)

            # Assign diagonals to cm
            cost_matrix[total_objects - num_pred :, :num_pred] = bot_left
            cost_matrix[:num_gt, total_objects - num_gt :] = top_right

            row_ind, col_ind = linear_sum_assignment(cost_matrix)
            # go back to matched node ids from matrix indices
            for row, col in zip(row_ind, col_ind):
                # it said they were sorted by row index, so we only want the top left corner
                if row > num_gt:
                    break
                if (
                    col > num_pred
                ):  # the gt was unmatched (matched to the unmatched cost in the top right)
                    continue
                gt_id = gt_nodes[row]
                pred_id = pred_nodes[col]
                mapping.append((gt_id, pred_id))
        return mapping
