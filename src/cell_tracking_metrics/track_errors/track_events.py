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
        identity_switches (int): The number of adjacent edges in the ground truth
            that are matched to non-consecutive edges in the prediction.
            This will only be non-zero if ground truth nodes can be matched
            to multiple predicted nodes.

        nonsplit_vertices (int):
        incorrect_semantics (int):

        division_counts(dict[int, DivisionEvents]): A mapping
            from a "frame buffer" (number of frames within which a division can
            be detected) to division event counts. If predicted divisions
            must be in the exact frame as the gt division to be considered
            correct, the frame buffer is 0. A frame buffer of 1 means that divisions
            predicted within 1 frame of the gt division are considered correct.
    """

    def __init__(
        self,
        fp_nodes=None,
        fn_nodes=None,
        fp_edges=None,
        fn_edges=None,
        identity_switches=None,
        nonsplit_vertices=None,
        incorrect_semantics=None,
        division_counts=None,
    ):
        self.fp_nodes = fp_nodes
        self.fn_nodes = fn_nodes
        self.fp_edges = fp_edges
        self.fn_edges = fn_edges
        self.identity_switches = identity_switches
        self.nonsplit_vertices = nonsplit_vertices
        self.incorrect_semantics = incorrect_semantics
        self.division_counts = {}
        if division_counts is not None:
            self.division_counts[division_counts.frame_buffer] = division_counts

    def add_division_counts(self, frame_buffer, counts):
        if self.division_counts is None:
            self.division_counts = {}
        self.division_counts[frame_buffer] = counts

    def get_division_counts(self, frame_buffer=0):
        if frame_buffer not in self.division_counts:
            return None
        return self.division_counts[frame_buffer]
    
    def add_events(self, name, value, fail_if_none=False):
        """Add value to the event with the given name.
        By default, None is considered to be equivalent to 0.
        If you want this operation to fail if the event with the 
        given name was not computed, set fail_if_none to True.

        Args:
            name (str): The name of the event. Will work for any attributes of this object,
                otherwise raises AttributeError.
            value (int): The number to add to the current value.
            fail_if_none (bool): Raise ValueError if either the
                current value or the provided value is None. Defaults to False.
        """
        current_value = getattr(self, name)
        if value is None:
            if fail_if_none:
                raise ValueError(f"Provided None value but fail_if_none=True")
            else:
                value = 0
        if current_value is None:
            if fail_if_none:
                raise ValueError(f"Current value for event {name} is None but fail_if_none=True")
            else:
                current_value = 0
        setattr(self, name, current_value + value)