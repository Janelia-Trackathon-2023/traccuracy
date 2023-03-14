class DivisionEvents:
    """A class to hold counts of tracking events or errors.

    Counts are generated based on the output of a matching
    (gt TrackingGraph, predicted TrackingGraph, matched nodes).

    This class provides a set of standard events that our library
    keeps track of.
    To add custom fields, you can create a subclass of this class.

    Fields:
        gt_divisions (list): The number of divisions in the ground truth graph.
            Defaults to None.
        fp_divisions (list): The number of divisions in the predicted graph
            that are not matched to a division in the ground truth graph.
            Defaults to None.
        fn_divisions (list): The number of divisions in the ground truth graph
            that are not matched to a division in the predicted graph.
            Defaults to None.
        tp_divisions (list): The number of divisions in the ground truth graph
            that are correctly identified in the predicted graph.
            Defaults to None.
        frame_buffer (int): A predicted division can be matched with a ground
            truth division within this many frames. Defaults to 0.

    """

    def __init__(
        self,
        gt_divisions=None,
        tp_divisions=None,
        fp_divisions=None,
        fn_divisions=None,
        frame_buffer=0,
    ):
        if isinstance(gt_divisions, list):
            self.gt_divisions = gt_divisions
        else:
            self.gt_divisions = []

        if isinstance(tp_divisions, list):
            self.tp_divisions = tp_divisions
        else:
            self.tp_divisions = []

        if isinstance(fp_divisions, list):
            self.fp_divisions = fp_divisions
        else:
            self.fp_divisions = []

        if isinstance(fn_divisions, list):
            self.fn_divisions = fn_divisions
        else:
            self.fn_divisions = []

        self.frame_buffer = frame_buffer

    @property
    def gt_division_count(self):
        return len(self.gt_divisions)

    @property
    def tp_division_count(self):
        return len(self.tp_divisions)

    @property
    def fp_division_count(self):
        return len(self.fp_divisions)

    @property
    def fn_division_count(self):
        return len(self.fn_divisions)

    @property
    def count_dict(self):
        return {
            "Total GT Divisions": self.gt_division_count,
            "True Positive Divisions": self.tp_division_count,
            "False Positive Divisions": self.fp_division_count,
            "False Negative Divisions": self.fn_division_count,
        }
