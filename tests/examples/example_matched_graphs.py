import networkx as nx
from traccuracy._tracking_graph import TrackingGraph
from traccuracy.matchers._base import Matched

"""A set of fixtures covering basic graph matching cases over 3 time frames
Covers edge cases, good matchings, fn nodes, fp nodes, two to one matchings in each
direction (pred -> gt, gt -> pred), and divisions
"""


def basic_graph(node_ids=(1, 2, 3), y_offset=0, frame_key="t", location_keys=("y")):
    nodes = [
        (
            node_ids[0],
            {
                frame_key: 0,
                location_keys[0]: 0 + y_offset,
            },
        ),
        (
            node_ids[1],
            {
                frame_key: 1,
                location_keys[0]: 0 + y_offset,
            },
        ),
        (
            node_ids[2],
            {
                frame_key: 2,
                location_keys[0]: 0 + y_offset,
            },
        ),
    ]

    edges = [(node_ids[0], node_ids[1]), (node_ids[1], node_ids[2])]
    graph = nx.DiGraph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)

    return TrackingGraph(graph, frame_key=frame_key, location_keys=location_keys)


# edge cases
def empty_pred():
    gt = basic_graph()
    pred = TrackingGraph(nx.DiGraph())
    mapping = []
    return Matched(gt, pred, mapping)


def empty_gt():
    pred = basic_graph()
    gt = TrackingGraph(nx.DiGraph())
    mapping = []
    return Matched(gt, pred, mapping)


# good
def good_matched():
    gt = basic_graph()
    pred = basic_graph(node_ids=(4, 5, 6), y_offset=1)
    mapping = [(1, 4), (2, 5), (3, 6)]
    return Matched(gt, pred, mapping)


# fn_node
def fn_node_matched(time_to_drop):  # 0, 1, or 2
    gt = basic_graph()
    pred_node_ids = (4, 5, 6)
    pred = basic_graph(node_ids=pred_node_ids, y_offset=1)
    mapping = [(1, 4), (2, 5), (3, 6)]
    pred.graph.remove_node(pred_node_ids[time_to_drop])
    del mapping[time_to_drop]
    return Matched(gt, pred, mapping)


# example of how to use
# @pytest.mark.parametrize("i", [0, 1, 2], ids=["0", "1", "2"])
# def test_fn_node(i):
#     matched = fn_node_matched(i)
#     assert ...


# fn_edge
def fn_edge_matched(edge_to_drop):  # 0 or 1
    gt = basic_graph()
    pred_node_ids = (4, 5, 6)
    pred = basic_graph(node_ids=pred_node_ids, y_offset=1)
    edge = (pred_node_ids[edge_to_drop], pred_node_ids[edge_to_drop + 1])
    pred.graph.remove_edge(*edge)
    mapping = [(1, 4), (2, 5), (3, 6)]
    return Matched(gt, pred, mapping)


# fp_node
def fp_node_matched(time_to_add):  # 0, 1, or 2
    gt = basic_graph()
    pred_node_ids = (4, 5, 6)
    pred = basic_graph(node_ids=pred_node_ids, y_offset=1)
    pred.graph.add_node(7, **{"t": time_to_add, "x": time_to_add, "y": 2})
    mapping = [(1, 4), (2, 5), (3, 6)]
    return Matched(gt, pred, mapping)


# fp_edge
def fp_edge_matched(edge_to_add):  # 0 or 1
    gt = basic_graph()
    pred_node_ids = (4, 5, 6)
    pred = basic_graph(node_ids=pred_node_ids, y_offset=1)
    pred.graph.add_node(7, **{"t": edge_to_add, "y": 2})
    pred.graph.add_node(8, **{"t": edge_to_add + 1, "y": 2})
    pred.graph.add_edge(7, 8)
    mapping = [(1, 4), (2, 5), (3, 6)]
    return Matched(gt, pred, mapping)


# two pred to one gt (identity switch)
def one_to_two(time):  # 0, 1, or 2
    gt_node_ids = (1, 2, 3)
    gt = basic_graph(node_ids=gt_node_ids, y_offset=1)
    pred_node_ids = (4, 5, 6)
    pred = basic_graph(node_ids=pred_node_ids, y_offset=0)
    pred.graph.add_node(7, **{"t": time, "y": 2})
    mapping = [(1, 4), (2, 5), (3, 6)]
    if time == 1:
        pred.graph.remove_edge(5, 6)
        pred.graph.add_edge(7, 6)
        pred.graph.nodes[6]["y"] = 2
    mapping.append((gt_node_ids[time], 7))
    return Matched(gt, pred, mapping)


# two gt to one pred (non split vertex)
def two_to_one(time):  # 0, 1, or 2
    gt_node_ids = (1, 2, 3)
    gt = basic_graph(node_ids=gt_node_ids, y_offset=0)
    pred_node_ids = (4, 5, 6)
    pred = basic_graph(node_ids=pred_node_ids, y_offset=1)
    gt.graph.add_node(7, **{"t": time, "y": 2})
    mapping = [(1, 4), (2, 5), (3, 6)]
    if time == 1:
        gt.graph.remove_edge(1, 2)
        gt.graph.add_edge(1, 7)
        gt.graph.nodes[1]["y"] = 2
    mapping.append((7, pred_node_ids[time]))
    return Matched(gt, pred, mapping)


def get_division_graphs():
    """
    G1
                                2_4
    1_0 -- 1_1 -- 1_2 -- 1_3 -<
                                3_4
    G2
                  2_2 -- 2_3 -- 2_4
    1_0 -- 1_1 -<
                  3_2 -- 3_3 -- 3_4
    """

    G1 = nx.DiGraph()
    G1.add_edge("1_0", "1_1")
    G1.add_edge("1_1", "1_2")
    G1.add_edge("1_2", "1_3")
    G1.add_edge("1_3", "2_4")
    G1.add_edge("1_3", "3_4")

    attrs = {}
    for node in G1.nodes:
        attrs[node] = {"t": int(node[-1:]), "x": 0, "y": 0}
    nx.set_node_attributes(G1, attrs)

    G2 = nx.DiGraph()
    G2.add_edge("1_0", "1_1")
    # Divide to generate 2 lineage
    G2.add_edge("1_1", "2_2")
    G2.add_edge("2_2", "2_3")
    G2.add_edge("2_3", "2_4")
    # Divide to generate 3 lineage
    G2.add_edge("1_1", "3_2")
    G2.add_edge("3_2", "3_3")
    G2.add_edge("3_3", "3_4")

    attrs = {}
    for node in G2.nodes:
        attrs[node] = {"t": int(node[-1:]), "x": 0, "y": 0}
    nx.set_node_attributes(G2, attrs)

    mapper = [("1_0", "1_0"), ("1_1", "1_1"), ("2_4", "2_4"), ("3_4", "3_4")]

    return G1, G2, mapper
