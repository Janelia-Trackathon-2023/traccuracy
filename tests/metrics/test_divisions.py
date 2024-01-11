from traccuracy import TrackingGraph
from traccuracy.matchers import Matched
from traccuracy.metrics._divisions import DivisionMetrics

from tests.test_utils import get_division_graphs


def test_DivisionMetrics():
    g_gt, g_pred, mapper = get_division_graphs()
    matched = Matched(
        TrackingGraph(g_gt),
        TrackingGraph(g_pred),
        mapper,
    )
    frame_buffer = 2

    results = DivisionMetrics(max_frame_buffer=frame_buffer)._compute(matched)

    for name, r in results.items():
        buffer = int(name[-1:])
        assert buffer in list(range(frame_buffer + 1))
        if buffer in (0, 1):
            # No corrections
            assert r["True Positive Divisions"] == 0
            assert r["False Positive Divisions"] == 1
            assert r["False Negative Divisions"] == 1
        else:
            # Correction
            assert r["True Positive Divisions"] == 1
            assert r["False Positive Divisions"] == 0
            assert r["False Negative Divisions"] == 0
