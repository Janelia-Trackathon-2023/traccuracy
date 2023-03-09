from dataclasses import dataclass
from typing import Optional


@dataclass
class DivisionEvents:
    """A class to hold counts of tracking events or errors.

    Counts are generated based on the output of a matching
    (gt TrackingGraph, predicted TrackingGraph, matched nodes).

    This class provides a set of standard events that our library
    keeps track of.
    To add custom fields, you can create a subclass of this class.

    Fields:
        gt_divisions (int): The number of divisions in the ground truth graph.
            Defaults to None.
        fp_divisions (int): The number of divisions in the predicted graph
            that are not matched to a division in the ground truth graph.
            Defaults to None.
        fn_divisions (int): The number of divisions in the ground truth graph
            that are not matched to a division in the predicted graph.
            Defaults to None.
        frame_buffer (int): A predicted division can be matched with a ground
            truth division within this many frames. Defaults to 0.

    """

    gt_divisions: Optional[int] = None
    fp_divisions: Optional[int] = None
    fn_divisions: Optional[int] = None
    frame_buffer: int = 0
