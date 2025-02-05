import networkx as nx
import pytest

from traccuracy import TrackingGraph
from traccuracy.matchers import Matched
from traccuracy.metrics._base import Metric


class TestMetric:
    matched = Matched(TrackingGraph(nx.DiGraph()), TrackingGraph(nx.DiGraph()), [], {})

    def test_missing_attribute(self):
        # Should fail if super init isn't called and subclass init isn't used
        # Error doesn't occur until metric._validate_matcher is called
        class DummyMetric(Metric):
            def __init__(self):
                pass

            def _compute(self):
                pass

        metric = DummyMetric()
        with pytest.raises(
            AttributeError, match="Metric subclass does not define valid_match_types"
        ):
            metric._validate_matcher(self.matched)

    def test_empty_list(self):
        class DummyMetric(Metric):
            def __init__(self):
                super().__init__(valid_matches=[])

            def _compute(self):
                pass

        with pytest.raises(
            TypeError, match="New metrics must provide a list of valid matching types"
        ):
            DummyMetric()

    def test_invalid_option(self):
        bad_option = "not-valid"

        class DummyMetric(Metric):
            def __init__(self):
                super().__init__(valid_matches=[bad_option])

            def _compute(self):
                pass

        with pytest.raises(ValueError, match=r"Matching type .* is not supported."):
            DummyMetric()

    def test_matcher_override(self):
        class DummyMetric(Metric):
            def __init__(self):
                super().__init__(valid_matches=["one-to-one"])

            def _compute(self):
                return {"success": True}

        graph = TrackingGraph(nx.DiGraph())
        matched = Matched(
            graph, graph, [(1, 2), (1, 3)], {"matching type": "many-to-many"}
        )

        metric = DummyMetric()

        # Fail without override
        message = (
            "The matched data uses a matcher that does not meet the requirements "
            "of the metric. Check the documentation for the metric for more information."
        )
        with pytest.raises(TypeError, match=message):
            metric.compute(matched)

        # Override triggers warning
        message = (
            "Overriding matcher/metric validation may result in "
            "unpredictable/incorrect metric results"
        )
        with pytest.raises(UserWarning, match=message):
            results = metric.compute(matched, override_matcher=True)
            assert "success" in results.results
