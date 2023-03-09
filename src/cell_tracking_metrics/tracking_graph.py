import logging

import networkx as nx

logger = logging.getLogger(__name__)


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

    def __init__(self, graph, frame_key="t", location_keys=["x", "y"]):
        """A directed graph representing a tracking solution where edges go forward in time.

        Args:
            graph (networkx.DiGraph): A directed graph representing a tracking solution
                where edges go forward in time.
            frame_key (str, optional): The key on each node in graph that contains the time frame
                of the node. Every node must have a value stored at this key. Defaults to 't'.
            location_keys (list, optional): The list of keys on each node in graph
                that contains the spatial location of the node. Every node
                must have a value stored at each of these keys. Defaults to ['x', 'y'].
        """
        self.graph = graph
        self.frame_key = frame_key
        self.location_keys = location_keys

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

    def get_nodes_with_attribute(self, attr, criterion=None):
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

        Returns:
            list of hashable: A list of node_ids which have the given attribute
                (and optionally have values at that attribute that meet the given criterion.)
        """
        nodes = []
        for node, attributes in self.graph.nodes.items():
            if attr in attributes.keys():
                if criterion is None or criterion(attributes[attr]):
                    nodes.append(node)
        return nodes

    def get_divisions(self):
        """Get all nodes that have at least two edges pointing to the next time frame

        Returns:
            list of hashable: a list of node ids for nodes that have more than one child
        """
        return [node for node, degree in self.graph.out_degree() if degree >= 2]

    def get_parents(self, node):
        """Get all parent nodes of the given node.

        A parent node is any node from a previous time point that has an edge to
        the given node. A division is not necessary for a node to be considered a parent.
        In a case where merges are not allowed, each node will have a maximum of
        one parent.

        Args:
            node (hashable): A node id

        Returns:
            list of hashable: A list of node ids containing all nodes that
                have an edge to the given node.
        """
        return [parent for parent, _ in self.graph.in_edges(node)]

    def get_children(self, node):
        """Get all child nodes of the given node.

        A child node is any node from a later time point that has an edge
        from the given node. A division is not necessary for a node to be
        considered a child. In a case where divisions are not allowed,
        a node will have a maximum of one child.

        Args:
            node (hashable): A node id

        Returns:
            list of hashable: A list of node ids containing all nodes that have
                an edge from the given node.
        """
        return [child for _, child in self.graph.out_edges(node)]

    def get_connected_components(self):
        """Get a list of TrackingGraphs, each corresponding to one track
        (i.e., a connected component in the track graph).

        Returns:
            A list of TrackingGraphs, one for each track.
        """
        graph = self.graph
        if len(graph.nodes) == 0:
            return []

        return [
            TrackingGraph(
                graph=graph.subgraph(g).copy(),
                frame_key=self.frame_key,
                location_keys=self.location_keys,
            )
            for g in nx.weakly_connected_components(graph)
        ]

    def get_attributes(self, _id):
        """Get the attribute dictionary of a node or an edge.
        If the id passed in is a tuple, it is assumed to refer to an edge.
        Otherwise, it is assumed to refer to a node.
        If the id is not found in the graph, a KeyError will be raised.

        Args:
            _id (tuple of hashable, or hashable): The node id (hashable)
                or edge (2-tuple of hashable) id to get the attributes for.

        Returns:
            dict: A dictionary of key-value pairs for all the attributes of the node/edge,
                including frame and location for nodes.
        """
        if isinstance(_id, tuple):
            return self.graph.edges[_id]
        else:
            return self.graph.nodes[_id]

    def set_attribute(self, _id, key, value):
        """Set a key/value pair in the attribute dictionary for the node or edge specified by _id.
        If the id passed in is a tuple, it is assumed to refer to an edge.
        Otherwise, it is assumed to refer to a node.
        If the id is not found in the graph, a KeyError will be raised.
        If the key already exists, the existing value will be overwritten.

        Args:
            _id (typle of hashable, or hashable): The node id (hashable)
                or edge (2-tuple of hashable) id to set the attributes for.
            key (string): The name of the attribute to set.
            value (any): The value of the attribute to set.
        """
        if isinstance(_id, tuple):
            self.graph.edges[_id][key] = value
        else:
            if key == self.frame_key or key in self.location_keys:
                raise ValueError(
                    "Cannot change node attributes storing time frame or location. "
                    f"(node: {_id}, key: {key})"
                )
            self.graph.nodes[_id][key] = value
