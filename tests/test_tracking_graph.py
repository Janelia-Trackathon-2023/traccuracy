from collections import Counter

import networkx as nx
import pytest
from traccuracy import EdgeAttr, NodeAttr, TrackingGraph


@pytest.fixture
def nx_comp1():
    """Component 1: Y=1
    x
    3|
    2|       /--1_3--1_4
    1| 1_0--1_1
    0|       \\--1_2
    ---------------------- t
        0    1   2    3
    """
    cells = [
        {"id": "1_0", "t": 0, "y": 1, "x": 1},
        {"id": "1_1", "t": 1, "y": 1, "x": 1, "is_tp_division": True},
        {"id": "1_2", "t": 2, "y": 1, "x": 0},
        {"id": "1_3", "t": 2, "y": 1, "x": 2},
        {"id": "1_4", "t": 3, "y": 1, "x": 2},
    ]

    edges = [
        {"source": "1_0", "target": "1_1", "is_tp": True},
        {"source": "1_1", "target": "1_2", "is_tp": False},
        {"source": "1_1", "target": "1_3"},
        {"source": "1_3", "target": "1_4"},
    ]
    graph = nx.DiGraph()
    graph.add_nodes_from([(cell["id"], cell) for cell in cells])
    graph.add_edges_from([(edge["source"], edge["target"], edge) for edge in edges])
    return graph


@pytest.fixture
def nx_comp2():
    """Component 2: X=1
    y
    3|              /--2_4
    2|  2_0--2_1--2_2
    1|             \\--2_3
    0|
    ---------------------- t
        0    1     2    3
    """
    cells = [
        {"id": "2_0", "t": 0, "y": 2, "x": 1},
        {"id": "2_1", "t": 1, "y": 2, "x": 1},
        {"id": "2_2", "t": 2, "y": 2, "x": 1, "is_tp_division": True},
        {"id": "2_3", "t": 3, "y": 1, "x": 1},
        {"id": "2_4", "t": 3, "y": 3, "x": 1},
    ]

    edges = [
        {"source": "2_0", "target": "2_1"},
        {"source": "2_1", "target": "2_2"},
        {"source": "2_2", "target": "2_3"},
        {"source": "2_2", "target": "2_4"},
    ]
    graph = nx.DiGraph()
    graph.add_nodes_from([(cell["id"], cell) for cell in cells])
    graph.add_edges_from([(edge["source"], edge["target"]) for edge in edges])
    return graph


@pytest.fixture
def nx_merge():
    """
    3_0--3_1--\\
              3_2--3_3
    3_4--3_5--/
    """
    cells = [
        {"id": "3_0", "t": 0, "x": 0, "y": 0},
        {"id": "3_1", "t": 1, "x": 0, "y": 0},
        {"id": "3_2", "t": 2, "x": 0, "y": 0},
        {"id": "3_3", "t": 3, "x": 0, "y": 0},
        {"id": "3_4", "t": 0, "x": 0, "y": 0},
        {"id": "3_5", "t": 1, "x": 0, "y": 0},
    ]

    edges = [
        {"source": "3_0", "target": "3_1"},
        {"source": "3_1", "target": "3_2"},
        {"source": "3_2", "target": "3_3"},
        {"source": "3_4", "target": "3_5"},
        {"source": "3_5", "target": "3_2"},
    ]
    graph = nx.DiGraph()
    graph.add_nodes_from([(cell["id"], cell) for cell in cells])
    graph.add_edges_from([(edge["source"], edge["target"]) for edge in edges])
    return graph


@pytest.fixture
def merge_graph(nx_merge):
    return TrackingGraph(nx_merge)


@pytest.fixture
def simple_graph(nx_comp1):
    return TrackingGraph(nx_comp1)


@pytest.fixture
def complex_graph(nx_comp1, nx_comp2):
    return TrackingGraph(nx.compose(nx_comp1, nx_comp2))


def test_constructor(nx_comp1):
    tracking_graph = TrackingGraph(nx_comp1)
    assert tracking_graph.start_frame == 0
    assert tracking_graph.end_frame == 4
    assert tracking_graph.nodes_by_frame == {
        0: {"1_0"},
        1: {"1_1"},
        2: {"1_2", "1_3"},
        3: {"1_4"},
    }

    # raise AssertionError if frame key not present or ValueError if overlaps
    # with reserved values
    with pytest.raises(AssertionError):
        TrackingGraph(nx_comp1, frame_key="f")
    with pytest.raises(ValueError):
        TrackingGraph(nx_comp1, frame_key=NodeAttr.FALSE_NEG)
    with pytest.raises(AssertionError):
        TrackingGraph(nx_comp1, location_keys=["x", "y", "z"])
    with pytest.raises(ValueError):
        TrackingGraph(nx_comp1, location_keys=["x", NodeAttr.FALSE_NEG])


def test_get_cells_by_frame(simple_graph):
    assert simple_graph.get_nodes_in_frame(0) == ["1_0"]
    assert Counter(simple_graph.get_nodes_in_frame(2)) == Counter(["1_2", "1_3"])
    assert simple_graph.get_nodes_in_frame(5) == []


def test_get_nodes_by_roi(simple_graph):
    assert simple_graph.get_nodes_by_roi(t=(0, 1)) == ["1_0"]
    assert Counter(simple_graph.get_nodes_by_roi(x=(1, None))) == Counter(
        ["1_0", "1_1", "1_3", "1_4"]
    )
    assert Counter(simple_graph.get_nodes_by_roi(x=(None, 2), t=(1, None))) == Counter(
        ["1_1", "1_2"]
    )


def test_get_location(nx_comp1):
    graph1 = TrackingGraph(nx_comp1, location_keys=["x", "y"])
    assert graph1.get_location("1_2") == [0, 1]
    assert graph1.get_location("1_4") == [2, 1]
    graph2 = TrackingGraph(nx_comp1, location_keys=["y", "x"])
    assert graph2.get_location("1_2") == [1, 0]
    assert graph2.get_location("1_4") == [1, 2]


def test_get_nodes_with_flag(simple_graph):
    assert simple_graph.get_nodes_with_flag(NodeAttr.TP_DIV) == ["1_1"]
    assert simple_graph.get_nodes_with_flag(NodeAttr.FP_DIV) == []
    with pytest.raises(ValueError):
        assert simple_graph.get_nodes_with_flag("is_tp_division")


def test_get_edges_with_flag(simple_graph):
    assert simple_graph.get_edges_with_flag(EdgeAttr.TRUE_POS) == [("1_0", "1_1")]
    assert simple_graph.get_edges_with_flag(EdgeAttr.FALSE_NEG) == []
    with pytest.raises(ValueError):
        assert simple_graph.get_nodes_with_flag("is_tp")


def test_get_nodes_with_attribute(simple_graph):
    assert simple_graph.get_nodes_with_attribute("is_tp_division") == ["1_1"]
    assert simple_graph.get_nodes_with_attribute("null") == []
    assert simple_graph.get_nodes_with_attribute(
        "is_tp_division", criterion=lambda x: x
    ) == ["1_1"]
    assert (
        simple_graph.get_nodes_with_attribute(
            "is_tp_division", criterion=lambda x: not x
        )
        == []
    )
    assert simple_graph.get_nodes_with_attribute("x", criterion=lambda x: x > 1) == [
        "1_3",
        "1_4",
    ]
    assert simple_graph.get_nodes_with_attribute(
        "x", criterion=lambda x: x > 1, limit_to=["1_3"]
    ) == [
        "1_3",
    ]
    assert (
        simple_graph.get_nodes_with_attribute(
            "x", criterion=lambda x: x > 1, limit_to=["1_0"]
        )
        == []
    )
    with pytest.raises(KeyError):
        simple_graph.get_nodes_with_attribute("x", limit_to=["5"])


def test_get_divisions(complex_graph):
    assert complex_graph.get_divisions() == ["1_1", "2_2"]


def test_get_merges(merge_graph):
    assert merge_graph.get_merges() == ["3_2"]


def test_get_preds(simple_graph, merge_graph):
    # Division graph
    assert simple_graph.get_preds("1_0") == []
    assert simple_graph.get_preds("1_1") == ["1_0"]
    assert simple_graph.get_preds("1_2") == ["1_1"]

    # Merge graph
    assert merge_graph.get_preds("3_3") == ["3_2"]
    assert merge_graph.get_preds("3_2") == ["3_1", "3_5"]


def test_get_succs(simple_graph):
    assert simple_graph.get_succs("1_0") == ["1_1"]
    assert Counter(simple_graph.get_succs("1_1")) == Counter(["1_2", "1_3"])
    assert simple_graph.get_succs("1_2") == []


def test_get_connected_components(complex_graph, nx_comp1, nx_comp2):
    tracks = complex_graph.get_connected_components()
    assert len(tracks) == 2
    if "1_1" in tracks[0].graph:
        track1 = tracks[0]
        track2 = tracks[1]
    else:
        track1 = tracks[1]
        track2 = tracks[0]
    assert track1.graph.nodes == nx_comp1.nodes
    assert track1.graph.edges == nx_comp1.edges
    assert track2.graph.nodes == nx_comp2.nodes
    assert track2.graph.edges == nx_comp2.edges


def test_get_and_set_node_attributes(simple_graph):
    assert simple_graph.nodes()["1_0"] == {"id": "1_0", "t": 0, "y": 1, "x": 1}
    assert simple_graph.nodes()["1_1"] == {
        "id": "1_1",
        "t": 1,
        "y": 1,
        "x": 1,
        "is_tp_division": True,
    }

    simple_graph.set_node_attribute("1_0", NodeAttr.FALSE_POS, value=False)
    assert simple_graph.nodes()["1_0"] == {
        "id": "1_0",
        "t": 0,
        "y": 1,
        "x": 1,
        NodeAttr.FALSE_POS: False,
    }
    with pytest.raises(ValueError):
        simple_graph.set_node_attribute("1_0", "x", 2)


def test_get_and_set_edge_attributes(simple_graph):
    print(simple_graph.edges())
    assert EdgeAttr.TRUE_POS not in simple_graph.edges()[("1_1", "1_3")]

    simple_graph.set_edge_attribute(("1_1", "1_3"), EdgeAttr.TRUE_POS, value=False)
    assert simple_graph.edges()[("1_1", "1_3")][EdgeAttr.TRUE_POS] is False
    with pytest.raises(ValueError):
        simple_graph.set_edge_attribute(("1_1", "1_3"), "x", 2)


def test_get_tracklets(simple_graph):
    tracklets = simple_graph.get_tracklets()
    for tracklet in tracklets:
        start_nodes = [n for n, d in tracklet.graph.in_degree() if d == 0]
        assert len(start_nodes) == 1
        end_nodes = [n for n, d in tracklet.graph.out_degree() if d == 0]
        assert len(end_nodes)

        if start_nodes[0] == "1_0":
            assert end_nodes[0] == "1_1"
        elif start_nodes[0] == "1_2":
            assert end_nodes[0] == "1_2"
        elif start_nodes[0] == "1_3":
            assert end_nodes[0] == "1_4"
