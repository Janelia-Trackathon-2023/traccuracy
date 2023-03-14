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

    @property
    def fp_node_count(self):
        if self.fp_nodes is not None:
            return len(self.fp_nodes)

    @property
    def fn_node_count(self):
        if self.fn_nodes is not None:
            return len(self.fn_nodes)

    @property
    def nonsplit_vertices_count(self):
        if self.nonsplit_vertices is not None:
            return len(self.nonsplit_vertices)

    @property
    def fp_edge_count(self):
        if self.fp_edges is not None:
            return len(self.fp_edges)

    @property
    def fn_edge_count(self):
        if self.fn_edges is not None:
            return len(self.fn_edges)

    @property
    def incorrect_semantics_count(self):
        if self.incorrect_semantics is not None:
            return len(self.incorrect_semantics)
