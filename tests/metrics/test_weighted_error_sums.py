import pytest
from traccuracy.metrics.ctc import (
    get_weighted_edge_error_sum,
    get_weighted_error_sum,
    get_weighted_vertex_error_sum,
)


def test_weighted_edge_sum():
    edge_error_counts = {"fp": 5, "fn": 12, "ws": 2}
    error_sum = get_weighted_edge_error_sum(edge_error_counts)
    assert error_sum == 19

    error_sum = get_weighted_edge_error_sum(edge_error_counts, 2, 2, 2)
    assert error_sum == 38

    error_sum = get_weighted_edge_error_sum(edge_error_counts, 0.5)
    assert error_sum == 16.5

    error_sum = get_weighted_edge_error_sum(edge_error_counts, 0.5, 2, 0.2)
    assert error_sum == 26.9

    error_sum = get_weighted_edge_error_sum(edge_error_counts, 0, 0, 0)
    assert error_sum == 0


def test_weighted_vertex_sum():
    vertex_error_counts = {"fp": 12, "fn": 4, "ns": 6}

    error_sum = get_weighted_vertex_error_sum(vertex_error_counts)
    assert error_sum == 22

    error_sum = get_weighted_vertex_error_sum(vertex_error_counts, 0.5)
    assert error_sum == 19

    error_sum = get_weighted_vertex_error_sum(vertex_error_counts, 0.5, 0.2, 0.8)
    assert pytest.approx(error_sum) == 8.6

    error_sum = get_weighted_vertex_error_sum(vertex_error_counts, 0, 0, 0)
    assert error_sum == 0


def test_weighted_error_sum():
    edge_error_counts = {"fp": 5, "fn": 12, "ws": 2}
    vertex_error_counts = {"fp": 12, "fn": 4, "ns": 7}

    error_sum = get_weighted_error_sum(vertex_error_counts, edge_error_counts)
    assert error_sum == 42

    error_sum = get_weighted_error_sum(
        vertex_error_counts, edge_error_counts, vertex_ns_weight=0, edge_ws_weight=0
    )
    assert error_sum == 33

    error_sum = get_weighted_error_sum(
        vertex_error_counts, edge_error_counts, 0.5, 0.5, 0.5
    )
    assert error_sum == 30.5
