from test_utils import get_movie_with_graph
from traccuracy import run_metrics
from traccuracy.matchers import CTCMatcher
from traccuracy.metrics import CTCMetrics


def test_run_metrics():
    graph = get_movie_with_graph()

    metric = CTCMetrics()
    matcher = CTCMatcher()

    results = run_metrics(graph, graph, matcher, [metric])
    assert isinstance(results, dict)
    assert "CTCMetrics" in results
