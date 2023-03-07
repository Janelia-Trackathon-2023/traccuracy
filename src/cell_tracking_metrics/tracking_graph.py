class TrackGraph:
    """Wrapper around networkx graphs.

    with additional functionality such as getting the position of a node.
    https://github.com/funkelab/linajea/blob/master/linajea/tracking/track_graph.py
    See this for inspiration (but we probably don't need the same functionality.).
    """

    def __init__(self, graph):
        self.graph = graph
