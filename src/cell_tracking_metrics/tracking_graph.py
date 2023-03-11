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

    def __init__(self, graph, frame_key="t", location_keys=("x", "y")):
        """A directed graph representing a tracking solution where edges go forward in time.

        Args:
            graph (networkx.DiGraph): A directed graph representing a tracking solution
                where edges go forward in time.
            frame_key (str, optional): The key on each node in graph that contains the time frame
                of the node. Every node must have a value stored at this key. Defaults to 't'.
            location_keys (tuple, optional): The list of keys on each node in graph
                that contains the spatial location of the node. Every node
                must have a value stored at each of these keys. Defaults to ('x', 'y').
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

        return [
            TrackingGraph(
                graph=graph.subgraph(g).copy(),
                frame_key=self.frame_key,
                location_keys=self.location_keys,
            )
            for g in nx.weakly_connected_components(graph)
        ]

    def set_node_attribute(self, ids, key, value):
        """Set a key/value pair in the attribute dictionary for the node or nodes
        specified by ids. If an id is not found in the graph, a KeyError will be raised.
        If the key already exists, the existing value will be overwritten.

        Args:
            ids (hashable | list[hashable]): The node id or list of node ids
                to set the attribute for.
            key (string): The name of the attribute to set.
            value (any): The value of the attribute to set.
        """
        if not isinstance(ids, list):
            ids = [ids]
        if key == self.frame_key or key in self.location_keys:
            raise ValueError(
                "Cannot change node attributes storing time frame or location. "
                f"(key: {key})"
            )
        for _id in ids:
            self.graph.nodes[_id][key] = value

    def set_edge_attribute(self, ids, key, value):
        """Set a key/value pair in the attribute dictionary for the edge or edges
        specified by ids. If an id is not found in the graph, a KeyError will be raised.
        If the key already exists, the existing value will be overwritten.

        Args:
            ids (tuple(hashable) | list[tuple(hashable)]): The edge id or list of edge ids
                to set the attribute for. Edge ids are a 2-tuple of node ids.
            key (string): The name of the attribute to set.
            value (any): The value of the attribute to set.
        """
        if not isinstance(ids, list):
            ids = [ids]
        if key == self.frame_key or key in self.location_keys:
            raise ValueError(
                "Cannot change node attributes storing time frame or location. "
                f"(key: {key})"
            )
        for _id in ids:
            self.graph.edges[_id][key] = value
