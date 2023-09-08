from traccuracy import TrackingData, TrackingGraph
from traccuracy.matchers._matched import Matched
from traccuracy.metrics._divisions import DivisionMetrics

from ..test_utils import get_division_graphs


class DummyMatched(Matched):
    def __init__(self, gt_data, pred_data, mapper):
        self.mapper = mapper
        super().__init__(gt_data, pred_data)

    def compute_mapping(self):
        return self.mapper


def test_DivisionMetrics():
    g_gt, g_pred, mapper = get_division_graphs()
    matched = DummyMatched(
        TrackingData(TrackingGraph(g_gt)),
        TrackingData(TrackingGraph(g_pred)),
        mapper=mapper,
    )
    frame_buffer = (0, 1, 2)

    metrics = DivisionMetrics(matched, frame_buffer=frame_buffer)
    results = metrics.compute()

    for name, r in results.items():
        buffer = int(name[-1:])
        assert buffer in frame_buffer
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
