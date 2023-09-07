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
        {"id": "1_1", "t": 1, "y": 1, "x": 1, "division": True},
        {"id": "1_2", "t": 2, "y": 1, "x": 0},
        {"id": "1_3", "t": 2, "y": 1, "x": 2},
        {"id": "1_4", "t": 3, "y": 1, "x": 2},
    ]

    edges = [
        {"source": "1_0", "target": "1_1"},
        {"source": "1_1", "target": "1_2"},
        {"source": "1_1", "target": "1_3"},
        {"source": "1_3", "target": "1_4"},
    ]
    graph = nx.DiGraph()
    graph.add_nodes_from([(cell["id"], cell) for cell in cells])
    graph.add_edges_from([(edge["source"], edge["target"]) for edge in edges])
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
        {"id": "2_2", "t": 2, "y": 2, "x": 1, "division": True},
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
        0: ["1_0"],
        1: ["1_1"],
        2: ["1_2", "1_3"],
        3: ["1_4"],
    }

    # raise AssertionError if frame key not present or overlaps with
    # reserved values
    with pytest.raises(AssertionError):
        TrackingGraph(nx_comp1, frame_key="f")
    with pytest.raises(AssertionError):
        TrackingGraph(nx_comp1, frame_key=NodeAttr.FALSE_NEG.value)
    with pytest.raises(AssertionError):
        TrackingGraph(nx_comp1, location_keys=["x", "y", "z"])
    with pytest.raises(AssertionError):
        TrackingGraph(nx_comp1, location_keys=["x", NodeAttr.FALSE_NEG.value])


def test_get_cells_by_frame(simple_graph):
    assert simple_graph.get_nodes_in_frame(0) == ["1_0"]
    assert simple_graph.get_nodes_in_frame(2) == ["1_2", "1_3"]
    assert simple_graph.get_nodes_in_frame(5) == []


def test_get_location(nx_comp1):
    graph1 = TrackingGraph(nx_comp1, location_keys=["x", "y"])
    assert graph1.get_location("1_2") == [0, 1]
    assert graph1.get_location("1_4") == [2, 1]
    graph2 = TrackingGraph(nx_comp1, location_keys=["y", "x"])
    assert graph2.get_location("1_2") == [1, 0]
    assert graph2.get_location("1_4") == [1, 2]


def test_get_nodes_with_attribute(simple_graph):
    assert simple_graph.get_nodes_with_attribute("division") == ["1_1"]
    assert simple_graph.get_nodes_with_attribute("null") == []
    assert simple_graph.get_nodes_with_attribute("division", criterion=lambda x: x) == [
        "1_1"
    ]
    assert (
        simple_graph.get_nodes_with_attribute("division", criterion=lambda x: not x)
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


def test_get_preds(simple_graph):
    assert simple_graph.get_preds("1_0") == []
    assert simple_graph.get_preds("1_1") == ["1_0"]
    assert simple_graph.get_preds("1_2") == ["1_1"]


def test_get_succs(simple_graph):
    assert simple_graph.get_succs("1_0") == ["1_1"]
    assert simple_graph.get_succs("1_1") == ["1_2", "1_3"]
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
        "division": True,
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
    assert simple_graph.edges()[("1_0", "1_1")] == {}

    simple_graph.set_edge_attribute(
        ("1_0", "1_1"),
        EdgeAttr.TRUE_POS,
        value=False)
    assert simple_graph.edges()[("1_0", "1_1")] == {EdgeAttr.TRUE_POS: False}
    with pytest.raises(ValueError):
        simple_graph.set_edge_attribute(("1_0", "1_1"), "x", 2)
