from functools import partial

from ..track_errors.division_events import DivisionEvents
from .metrics import Metrics


class DivisionMetrics(Metrics):
    # TODO: currently metrics expects a TrackEvents object not a division events

    def __init__(self, track_events):
        """Computes a set of metrics to describe division performance using a DivisionEvents object

        Args:
            track_events (DivisionEvents): DivisionEvents object

        Raises:
            ValueError: track_events input must be a DivisionEvents object
        """
        if not isinstance(track_events, DivisionEvents):
            raise ValueError('track_events input must be a DivisionEvents object')

        super().__init__(track_events)

        self.frame_buffer = track_events.frame_buffer

    @property
    def recall(self):
        try:
            self.recall = track_events.tp_divisions / (track_events.tp_divisions + track_events.fn_divisions)
        except ZeroDivisionError:
            self.recall = 0

        try:
            self.precision = track_events.tp_divisions / (track_events.tp_divisions + track_events.fp_divisions)
        except ZeroDivisionError:
            self.precision = 0

        try:
            self.f1 = 2 * (self.recall * self.precision) / (self.recall + self.precision)
        except ZeroDivisionError:
            self.f1 = 0

        try:
            self.mbc = track_events.tp_divisions / (track_events.tp_divisions + track_events.fn_divisions + track_events.fp_divisions)
        except ZeroDivisionError:
            self.mbc = 0

    def compute_metrics(self, n_digits=2):
        """Returns a dictionary of metrics after rounding to n_digits

        Args:
            n_digits (int, optional): Digits to round to. Defaults to 2.

        Returns:
            dict: Dictionary where keys are metrics names (str) and values are flots or ints
        """
        _round = partial(round, ndigits=n_digits)

        return {
            'Frame Buffer': self.frame_buffer,
            'Division Recall': _round(self.recall),
            'Division Precision': _round(self.precision),
            'Division F1': _round(self.f1),
            'Mitotic branching correctness': _round(self.mbc)
        }
