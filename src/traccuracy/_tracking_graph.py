import copy
import enum
import logging

import networkx as nx

logger = logging.getLogger(__name__)


@enum.unique
class NodeAttr(str, enum.Enum):
    """An enum containing all valid attributes that can be used to
    annotate the nodes of a TrackingGraph. If new metrics require new
    annotations, they should be added here to ensure strings do not overlap and
    are standardized. Note that the user specified frame and location
    attributes are also valid node attributes that will be stored on the graph
    and should not overlap with these values. Additionally, if a graph already
    has annotations using these strings before becoming a TrackGraph,
    this will likely ruin metrics computation!
    """

    # True positive nodes. Valid on gt and computed graphs.
    TRUE_POS = "is_tp"
    # False positive nodes. Valid on computed graph.
    FALSE_POS = "is_fp"
    # False negative nodes. Valid on gt graph.
    FALSE_NEG = "is_fn"
    # Non-split vertices as defined by CTC. Valid on computed graph
    # when many computed nodes can be matched to one gt node.
    NON_SPLIT = "is_ns"
    # True positive divisions. Valid on gt and computed graphs.
    TP_DIV = "is_tp_division"
    # False positive divisions. Valid on computed graph.
    FP_DIV = "is_fp_division"
    # False negative divisions. Valid on gt graph.
    FN_DIV = "is_fn_division"

    @classmethod
    def has_value(cls, value):
        """Check if a value is one of the enum's values.
        This can be used to check if other graph annotation strings are
        colliding with our reserved strings.

        Args:
            value : Check if the enum contains this value.

        Returns:
            bool: True if the value is already in the enum's values,
                false otherwise
        """
        return value in cls.__members__.values()


@enum.unique
class EdgeAttr(str, enum.Enum):
    """An enum containing all valid attributes that can be used to
    annotate the edges of a TrackingGraph. If new metrics require new
    annotations, they should be added here to ensure strings do not overlap and
    are standardized. Additionally, if a graph already
    has annotations using these strings before becoming a TrackGraph,
    this will likely ruin metrics computation!
    """

    # True positive edges. Valid on gt and computed graphs.
    TRUE_POS = "is_tp"
    # False positive edges.Valid on computed graph.
    FALSE_POS = "is_fp"
    # False negative nodes. Valid on gt graph.
    FALSE_NEG = "is_fn"
    # Edges between tracks as defined by CTC. Valid on gt and computed graphs.
    INTERTRACK_EDGE = "is_intertrack_edge"
    # Edges with wrong semantic as defined by CTC. Valid on computed graph.
    WRONG_SEMANTIC = "is_wrong_semantic"


class TrackingGraph:
    """A directed graph representing a tracking solution where edges go forward in time.

    Nodes represent cell detections and edges represent links between detections in the same track.
    Nodes in the graph must have an attribute that represents time frame (default to 't') and
    location (defaults to 'x' and 'y'). As in networkx, every cell must have a unique id, but these
    can be of any (hashable) type.

    We provide common functions for accessing parts of the track graph, for example
    all nodes in a certain frame, or all previous or next edges for a given node.
    Additional functionality can be accessed by querying the stored networkx graph
    with native networkx functions.

    Currently it is assumed that the structure of the networkx graph as well as the
    time frame and location of each node is not mutated after construction,
    although non-spatiotemporal attributes of nodes and edges can be modified freely.

    Attributes
        start_frame: int, the first frame with a node in the graph
        end_frame: int, the end of the span of frames containing nodes
            (one frame after the last frame that contains a node)
        nodes_by_frame: dict of int -> node_id
            Maps from frames to all node ids in that frame
        frame_key: str
            The name of the node attribute that corresponds to the frame of
            the node. Defaults to "t".
        location_keys: list of str
            Keys used to access the location of the cell in space.
    """

    def __init__(
        self,
        graph,
        frame_key="t",
        label_key="segmentation_id",
        location_keys=("x", "y"),
    ):
        """A directed graph representing a tracking solution where edges go
        forward in time.

        If the provided graph already has annotations that are strings
        included in NodeAttrs or EdgeAttrs, this will likely ruin
        metric computation!

        Args:
            graph (networkx.DiGraph): A directed graph representing a tracking
                solution where edges go forward in time. If the graph already
                has annotations that are strings included in NodeAttrs or
                EdgeAttrs, this will likely ruin metrics computation!
            frame_key (str, optional): The key on each node in graph that
                contains the time frameof the node. Every node must have a
                value stored at this key. Defaults to 't'.
            label_key (str, optional): The key on each node that denotes the
                pixel value of the node in the segmentation. Defaults to
                'segmentation_id'. Pass `None` if there is not a label
                attribute on the graph.
            location_keys (tuple, optional): The list of keys on each node in
                graph that contains the spatial location of the node. Every
                node must have a value stored at each of these keys.
                Defaults to ('x', 'y').
        """
        self.graph = graph
        if NodeAttr.has_value(frame_key):
            raise ValueError(
                f"Specified frame key {frame_key} is reserved for graph"
                "annotation. Please change the frame key."
            )
        self.frame_key = frame_key
        if label_key is not None and NodeAttr.has_value(label_key):
            raise ValueError(
                f"Specified label key {label_key} is reserved for graph"
                "annotation. Please change the label key."
            )
        self.label_key = label_key
        for loc_key in location_keys:
            if NodeAttr.has_value(loc_key):
                raise ValueError(
                    f"Specified location key {loc_key} is reserved for graph"
                    "annotation. Please change the location key."
                )
        self.location_keys = location_keys

        # Define empty attributes that will be set by update_graph
        self.graph = None
        self.nodes_by_frame = None
        self.start_frame = None
        self.end_frame = None

        self._update_graph(graph)

        # Record types of annotations that have been calculated
        self.division_annotations = False
        self.node_errors = False
        self.edge_errors = False

    def nodes(self, limit_to=None):
        """Get all the nodes in the graph, along with their attributes.

        Args:
            limit_to (list[hashable], optional): Limit returned dictionary
                to nodes with the provided ids. Defaults to None.
                Will raise KeyError if any of these node_ids are not present.

        Returns:
            dict[hashable, dict]: A dictionary from node ids to node attributes
        """
        nodes = self.graph.nodes.items()
        if limit_to is None:
            return dict(nodes)
        else:
            limited_nodes = {_id: data for _id, data in nodes if _id in limit_to}
            return limited_nodes

    def edges(self, limit_to=None):
        """Get all the edges in the graph, along with their attributes.

        Args:
            limit_to (list[tuple[hashable]], optional): Limit returned dictionary
                to edges with the provided ids. Defaults to None.
                Will raise KeyError if any of these edge ids are not present.

        Returns:
            dict[tuple[hashable], dict]: A dictionary from edge ids to edge attributes
        """
        edges = self.graph.edges.items()
        if limit_to is None:
            return dict(edges)
        else:
            limited_edges = {_id: data for _id, data in edges if _id in limit_to}
            return limited_edges

    def get_nodes_in_frame(self, frame):
        """Get the node ids of all nodes in the given frame.

        Args:
            frame (int): The frame to return all node ids for.
                If the provided frame is outside of the range
                (self.start_frame, self.end_frame), returns an empty list.

        Returns:
            list of node_ids: A list of node ids for all nodes in frame.
        """
        if frame in self.nodes_by_frame.keys():
            return self.nodes_by_frame[frame]
        else:
            return []

    def get_location(self, node_id):
        """Get the spatial location of the node with node_id using self.location_keys.

        Args:
            node_id (hashable): The node_id to get the location of

        Returns:
            list of float: A list of location values in the same order as self.location_keys
        """
        return [self.graph.nodes[node_id][key] for key in self.location_keys]

    def get_nodes_with_flag(self, attr):
        """Get all nodes with specified NodeAttr set to True.

        Args:
            attr (traccuracy.NodeAttr): the node attribute to query for

        Returns:
            (List(hashable)): A list of node_ids which have the given attribute
                and the value is True.
        """
        if not isinstance(attr, NodeAttr):
            raise ValueError(
                f"Function takes NodeAttr arguments, not {type(attr)}.")
        nodes_with_flag = [node for node, attrs in self.nodes().items()
                           if attr in attrs.keys() and attrs[attr] is True]
        return nodes_with_flag

    def get_nodes_with_attribute(self, attr, criterion=None, limit_to=None):
        """Get the node_ids of all nodes who have an attribute, optionally
        limiting to nodes whose value at that attribute meet a given criteria.

        For example, get all nodes that have an attribute called "division",
        or where the value for "division" == True.
        This also works on location keys, for example to get all nodes with y > 100.

        Args:
            attr (str): the name of the attribute to search for in the node metadata
            criterion ((any)->bool, optional): A function that takes a value and returns
                a boolean. If provided, nodes will only be returned if the value at
                node[attr] meets this criterion. Defaults to None.
            limit_to (list[hashable], optional): If provided the function will only
                return node ids in this list. Will raise KeyError if ids provided here
                are not present.

        Returns:
            list of hashable: A list of node_ids which have the given attribute
                (and optionally have values at that attribute that meet the given criterion,
                and/or are in the list of node ids.)
        """
        if not limit_to:
            limit_to = self.graph.nodes.keys()

        nodes = []
        for node in limit_to:
            attributes = self.graph.nodes[node]
            if attr in attributes.keys():
                if criterion is None or criterion(attributes[attr]):
                    nodes.append(node)
        return nodes

    def get_edges_with_attribute(self, attr, criterion=None, limit_to=None):
        """Get the edge_ids of all edges who have an attribute, optionally
        limiting to edges whose value at that attribute meet a given criteria.

        For example, get all edges that have an attribute called "fp",
        or where the value for "fp" == True.

        Args:
            attr (str): the name of the attribute to search for in the edge metadata
            criterion ((any)->bool, optional): A function that takes a value and returns
                a boolean. If provided, edges will only be returned if the value at
                edge[attr] meets this criterion. Defaults to None.
            limit_to (list[hashable], optional): If provided the function will only
                return edge ids in this list. Will raise KeyError if ids provided here
                are not present.

        Returns:
            list of hashable: A list of edge_ids which have the given attribute
                (and optionally have values at that attribute that meet the given criterion,
                and/or are in the list of edge ids.)
        """
        if not limit_to:
            limit_to = self.graph.edges.keys()

        edges = []
        for edge in limit_to:
            attributes = self.graph.edges[edge]
            if attr in attributes.keys():
                if criterion is None or criterion(attributes[attr]):
                    edges.append(edge)
        return edges

    def get_divisions(self):
        """Get all nodes that have at least two edges pointing to the next time frame

        Returns:
            list of hashable: a list of node ids for nodes that have more than one child
        """
        return [node for node, degree in self.graph.out_degree() if degree >= 2]

    def get_preds(self, node):
        """Get all predecessors of the given node.

        A predecessor node is any node from a previous time point that has an edge to
        the given node. In a case where merges are not allowed, each node will have a
        maximum of one predecessor.

        Args:
            node (hashable): A node id

        Returns:
            list of hashable: A list of node ids containing all nodes that
                have an edge to the given node.
        """
        return [pred for pred, _ in self.graph.in_edges(node)]

    def get_succs(self, node):
        """Get all successor nodes of the given node.

        A successor node is any node from a later time point that has an edge
        from the given node.  In a case where divisions are not allowed,
        a node will have a maximum of one successor.

        Args:
            node (hashable): A node id

        Returns:
            list of hashable: A list of node ids containing all nodes that have
                an edge from the given node.
        """
        return [succ for _, succ in self.graph.out_edges(node)]

    def get_connected_components(self):
        """Get a list of TrackingGraphs, each corresponding to one track
        (i.e., a connected component in the track graph).

        Returns:
            A list of TrackingGraphs, one for each track.
        """
        graph = self.graph
        if len(graph.nodes) == 0:
            return []

        return [self.get_subgraph(g) for g in nx.weakly_connected_components(graph)]

    def get_subgraph(self, nodes):
        """Returns a new TrackingGraph with the subgraph defined by the list of nodes

        Args:
            nodes (list): List of node ids to use in constructing the subgraph
        """

        new_graph = self.graph.subgraph(nodes).copy()
        new_trackgraph = copy.deepcopy(self)
        new_trackgraph._update_graph(new_graph)

        return new_trackgraph

    def _update_graph(self, graph):
        """Given a new graph, which is expected to be a subgraph of the current graph,
        update attributes which are dependent on the graph.

        Args:
            graph (nx.DiGraph): A networkx graph that is a subgraph of the original graph
        """
        self.graph = graph

        # construct a dictionary from frames to node ids for easy lookup
        self.nodes_by_frame = {}
        for node, attrs in self.graph.nodes.items():
            # check that every node has the time frame and location specified
            assert (
                self.frame_key in attrs.keys()
            ), f"Frame key {self.frame_key} not present for node {node}."
            for key in self.location_keys:
                assert (
                    key in attrs.keys()
                ), f"Location key {key} not present for node {node}."

            # store node id in nodes_by_frame mapping
            frame = attrs[self.frame_key]
            if frame not in self.nodes_by_frame.keys():
                self.nodes_by_frame[frame] = [node]
            else:
                self.nodes_by_frame[frame].append(node)

        # Store first and last frames for reference
        self.start_frame = min(self.nodes_by_frame.keys())
        self.end_frame = max(self.nodes_by_frame.keys()) + 1

    def set_node_attribute(self, ids, attr, value=True):
        """Set an attribute flag for a set of nodes specified by
        ids. If an id is not found in the graph, a KeyError will be raised.
        If the key already exists, the existing value will be overwritten.

        Args:
            ids (hashable | list[hashable]): The node id or list of node ids
                to set the attribute for.
            attr (traccuracy.NodeAttr): The node attribute to set. Must be
                of type NodeAttr - you may not not pass strings, even if they
                are included in the NodeAttr enum values.
            value (bool, optional): Attributes are flags and can only be set to
                True or False. Defaults to True.
        """
        if not isinstance(ids, list):
            ids = [ids]
        if not isinstance(attr, NodeAttr):
            raise ValueError(
                f"Provided attribute {attr} is not of type NodeAttr. "
                "Please use the enum instead of passing string values, "
                "and add new attributes to the class to avoid key collision."
            )
        for _id in ids:
            self.graph.nodes[_id][attr] = value

    def set_edge_attribute(self, ids, attr, value=True):
        """Set an attribute flag for a set of edges specified by
        ids. If an edge is not found in the graph, a KeyError will be raised.
        If the key already exists, the existing value will be overwritten.

        Args:
            ids (tuple(hashable) | list[tuple(hashable)]): The edge id or list of edge ids
                to set the attribute for. Edge ids are a 2-tuple of node ids.
            attr (traccuracy.EdgeAttr): The edge attribute to set. Must be
                of type EdgeAttr - you may not pass strings, even if they are
                included in the EdgeAttr enum values.
            value (bool): Attributes are flags and can only be set to
                True or False. Defaults to True.
        """
        if not isinstance(ids, list):
            ids = [ids]
        if not isinstance(attr, EdgeAttr):
            raise ValueError(
                f"Provided attribute {attr} is not of type EdgeAttr. "
                "Please use the enum instead of passing string values, "
                "and add new attributes to the class to avoid key collision."
            )
        for _id in ids:
            self.graph.edges[_id][attr] = value
