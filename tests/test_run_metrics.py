from traccuracy import run_metrics
from traccuracy.matchers._base import Matched, Matcher
from traccuracy.metrics._base import Metric

from tests.test_utils import get_movie_with_graph


class DummyMetric(Metric):
    def compute(self, matched):
        return {}


class DummyMetricParam(Metric):
    def __init__(self, param="value"):
        self.param = param

    def compute(self, matched):
        return {}


class DummyMatcher(Matcher):
    def __init__(self, mapping=[]):
        self.mapping = mapping

    def _compute_mapping(self, gt_graph, pred_graph):
        return Matched(gt_graph, pred_graph, self.mapping)


def test_run_metrics():
    graph = get_movie_with_graph()
    mapping = [(n, n) for n in graph.nodes()]

    # # Check matcher input -- not instantiated
    # with pytest.raises(TypeError):
    #     run_metrics(graph, graph, DummyMatcher, [DummyMetric()])

    # # Check matcher input -- wrong type
    # with pytest.raises(TypeError):
    #     run_metrics(graph, graph, 'rando', DummyMetric())

    # # Check metric input -- not instantiated
    # with pytest.raises(TypeError):
    #     run_metrics(graph, graph, DummyMatcher(), [DummyMetric])

    # # Check metric input -- wrong type
    # with pytest.raises(TypeError):
    #     run_metrics(graph, graph, DummyMatcher(), [DummyMetric(), 'rando'])

    # One metric
    results = run_metrics(graph, graph, DummyMatcher(mapping), [DummyMetric()])
    assert isinstance(results, list)
    assert len(results) == 1
    assert "DummyMetric" in results[0]

    # Duplicate metric with different params
    results = run_metrics(
        graph,
        graph,
        DummyMatcher(mapping),
        [DummyMetricParam("param1"), DummyMetricParam("param2")],
    )
    assert len(results) == 2
    assert "DummyMetricParam" in results[0]
    assert results[0]["parameters"] == {"param": "param1"}
    assert "DummyMetricParam" in results[1]
    assert results[1]["parameters"] == {"param": "param2"}
