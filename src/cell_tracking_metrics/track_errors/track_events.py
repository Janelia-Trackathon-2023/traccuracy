from dataclasses import dataclass
from typing import Optional

from .division_events import DivisionEvents


@dataclass
class TrackEvents:
    """A class to hold counts of tracking events or errors.

    Counts are generated based on the output of a matching
    (gt TrackingGraph, predicted TrackingGraph, matched nodes).

    This class provides a set of standard events that our library
    keeps track of.
    To add custom fields, you can create a subclass of this class.

    Fields:
        fp_nodes (int): The number of false positive nodes
            (present in predicted graph but not matched). Defaults to None.
        fn_nodes (int): The number of false negative ndoes
            (present in gt graph but not matched). Defaults to None.
        fp_edges (int): The number of false positive edges
            (present in the predicted graph but not matched). Defaults to None.
        fn_edges (int): The number of false negative edges
            (present in the gt graph but not matched). Defaults to None.

        division_counts(dict[int, DivisionEvents]): A mapping
            from a "frame buffer" (number of frames within which a division can
            be detected) to division event counts. If predicted divisions
            must be in the exact frame as the gt division to be considered
            correct, the frame buffer is 0. A frame buffer of 1 means that divisions
            predicted within 1 frame of the gt division are considered correct.
    """

    # nodes
    fp_nodes: Optional[int] = None
    fn_nodes: Optional[int] = None

    # edges
    fp_edges: Optional[int] = None
    fn_edges: Optional[int] = None

    division_counts: Optional[dict[int, DivisionEvents]] = None

    def add_division_counts(self, frame_buffer, counts):
        if self.division_counts is None:
            self.division_counts = {}
        self.division_counts[frame_buffer] = counts
