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
                super().__init__([])

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
                super().__init__([bad_option])

            def _compute(self):
                pass

        with pytest.raises(ValueError, match=r"Matching type .* is not supported."):
            DummyMetric()
