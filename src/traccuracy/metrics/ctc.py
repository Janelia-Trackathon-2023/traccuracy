from typing import TYPE_CHECKING

from traccuracy.metrics.base import Metric
from traccuracy.track_errors.ctc import evaluate_ctc_events

if TYPE_CHECKING:
    from .base import Matched


class AOGMMetrics(Metric):
    needs_det_matrix = True

    def __init__(
        self,
        matched_data: "Matched",
        vertex_ns_weight=1,
        vertex_fp_weight=1,
        vertex_fn_weight=1,
        edge_fp_weight=1,
        edge_fn_weight=1,
        edge_ws_weight=1,
    ):
        self.v_weights = {
            "ns": vertex_ns_weight,
            "fp": vertex_fp_weight,
            "fn": vertex_fn_weight,
        }
        self.e_weights = {
            "fp": edge_fp_weight,
            "fn": edge_fn_weight,
            "ws": edge_ws_weight,
        }
        super().__init__(matched_data)

    def compute(self):
        gt_graph = self.data.gt_data.tracking_graph
        pred_graph = self.data.pred_data.tracking_graph
        mapping = self.data.mapping
        matrices = self.data._det_matrices

        track_events = evaluate_ctc_events(gt_graph, pred_graph, mapping, matrices)
        vertex_error_counts = {
            "ns": track_events.nonsplit_vertices_count,
            "fp": track_events.fp_node_count,
            "fn": track_events.fn_node_count,
        }
        edge_error_counts = {
            "ws": track_events.incorrect_semantics_count,
            "fp": track_events.fp_edge_count,
            "fn": track_events.fn_edge_count,
        }
        error_sum = get_weighted_error_sum(
            vertex_error_counts,
            edge_error_counts,
            self.v_weights["ns"],
            self.v_weights["fp"],
            self.v_weights["fn"],
            self.e_weights["fp"],
            self.e_weights["fn"],
            self.e_weights["ws"],
        )
        return {
            "AOGM": error_sum,
            "fp_nodes": vertex_error_counts["fp"],
            "fn_nodes": vertex_error_counts["fn"],
            "ns_nodes": vertex_error_counts["ns"],
            "fp_edges": edge_error_counts["fp"],
            "fn_edges": edge_error_counts["fn"],
            "ws_edges": edge_error_counts["ws"],
        }


class CTCMetrics(AOGMMetrics):
    def __init__(self, matched_data: "Matched"):
        vertex_weight_ns = 5
        vertex_weight_fn = 10
        vertex_weight_fp = 1

        edge_weight_fp = 1
        edge_weight_fn = 1.5
        edge_weight_ws = 1
        super().__init__(
            matched_data,
            vertex_ns_weight=vertex_weight_ns,
            vertex_fp_weight=vertex_weight_fp,
            vertex_fn_weight=vertex_weight_fn,
            edge_fp_weight=edge_weight_fp,
            edge_fn_weight=edge_weight_fn,
            edge_ws_weight=edge_weight_ws,
        )

    def compute(self):
        # AOGM-0 is the cost of creating the gt graph from scratch
        gt_graph = self.data.gt_data.tracking_graph.graph
        n_nodes = gt_graph.number_of_nodes()
        n_edges = gt_graph.number_of_edges()
        aogm_0 = n_nodes * self.v_weights["fn"] + n_edges * self.e_weights["fn"]
        if aogm_0 == 0:
            raise RuntimeError(
                f"AOGM0 is 0 - cannot compute TRA from GT graph with {n_nodes} nodes and"
                + f" {n_edges} edges with {self.v_weights['fn']} vertex FN weight and"
                + f" {self.e_weights['fn']} edge FN weight"
            )
        errors = super().compute()
        aogm = errors["AOGM"]
        tra = 1 - min(aogm, aogm_0) / aogm_0
        errors["TRA"] = tra

        aogmd_0 = n_nodes * self.v_weights["fn"]
        aogmd = get_weighted_vertex_error_sum(
            {
                "ns": errors["ns_nodes"],
                "fp": errors["fp_nodes"],
                "fn": errors["fn_nodes"],
            },
            self.v_weights["ns"],
            self.v_weights["fp"],
            self.v_weights["fn"],
        )
        det = 1 - min(aogmd, aogmd_0) / aogmd_0
        errors["DET"] = det
        return errors


def get_weighted_vertex_error_sum(
    vertex_error_counts, vertex_ns_weight=1, vertex_fp_weight=1, vertex_fn_weight=1
):
    vertex_ns_count = vertex_error_counts["ns"]
    vertex_fp_count = vertex_error_counts["fp"]
    vertex_fn_count = vertex_error_counts["fn"]
    vertex_error_sum = (
        vertex_ns_weight * vertex_ns_count
        + vertex_fp_weight * vertex_fp_count
        + vertex_fn_weight * vertex_fn_count
    )
    return vertex_error_sum


def get_weighted_edge_error_sum(
    edge_error_counts, edge_fp_weight=1, edge_fn_weight=1, edge_ws_weight=1
):
    edge_fp_count = edge_error_counts["fp"]
    edge_fn_count = edge_error_counts["fn"]
    edge_ws_count = edge_error_counts["ws"]
    edge_error_sum = (
        edge_fp_weight * edge_fp_count
        + edge_fn_weight * edge_fn_count
        + edge_ws_weight * edge_ws_count
    )
    return edge_error_sum


def get_weighted_error_sum(
    vertex_error_counts,
    edge_error_counts,
    vertex_ns_weight=1,
    vertex_fp_weight=1,
    vertex_fn_weight=1,
    edge_fp_weight=1,
    edge_fn_weight=1,
    edge_ws_weight=1,
):
    vertex_error_sum = get_weighted_vertex_error_sum(
        vertex_error_counts, vertex_ns_weight, vertex_fp_weight, vertex_fn_weight
    )
    edge_error_sum = get_weighted_edge_error_sum(
        edge_error_counts, edge_fp_weight, edge_fn_weight, edge_ws_weight
    )
    return vertex_error_sum + edge_error_sum