import sys

from traccuracy._tracking_graph import TrackingGraph

sys.path.append("../tests/examples")
from pathlib import Path

import matplotlib.pyplot as plt
from example_matched_graphs import (
    empty_gt,
    empty_pred,
    fn_edge_matched,
    fn_node_matched,
    fp_edge_matched,
    fp_node_matched,
    good_matched,
    one_to_two,
    two_to_one,
)
from matplotlib.patches import Patch


def get_loc(graph, node):
    return graph.graph.nodes[node]["t"], graph.graph.nodes[node]["y"]


def plot_graph(ax, graph: TrackingGraph, color="black"):
    if graph.graph.number_of_nodes() == 0:
        return 0
    ids = list(graph.graph.nodes)
    print(ids)
    x = [graph.graph.nodes[node]["t"] for node in ids]
    y = [graph.graph.nodes[node]["y"] for node in ids]
    ax.scatter(x, y, color=color)
    for _x, _y, _id in zip(x, y, ids):
        ax.text(_x + 0.05, _y + 0.05, str(_id))

    for u, v in graph.graph.edges():
        print(u, v)
        xs = [graph.graph.nodes[u]["t"], graph.graph.nodes[v]["t"]]
        ys = [graph.graph.nodes[u]["y"], graph.graph.nodes[v]["y"]]
        ax.plot(xs, ys, color=color)

    return max(y)


def plot_matching(ax, matched, color="grey"):
    for u, v in matched.mapping:
        xs = [
            matched.gt_graph.graph.nodes[u]["t"],
            matched.pred_graph.graph.nodes[v]["t"],
        ]
        ys = [
            matched.gt_graph.graph.nodes[u]["y"],
            matched.pred_graph.graph.nodes[v]["y"],
        ]
        ax.plot(xs, ys, color=color, linestyle="dashed")


def save_matched(examples, title):
    gt_color = "black"
    pred_color = "blue"
    mapping_color = "grey"
    fig, ax = plt.subplots(1, len(examples) + 1, figsize=(3 * len(examples) + 1, 2))
    for i, matched in enumerate(examples):
        axis = ax[i]
        maxY = plot_graph(axis, matched.gt_graph, color=gt_color)
        maxY = max([maxY, plot_graph(axis, matched.pred_graph, color=pred_color)])
        plot_matching(axis, matched, color=mapping_color)
        axis.set_ybound(-0.5, maxY + 0.5)
        axis.set_xbound(-0.5, 2.5)
        axis.set_ylabel("Y Value")
        axis.set_xlabel("Time")

    handles = [
        Patch(color=gt_color),
        Patch(color=pred_color),
        Patch(color=mapping_color),
    ]
    labels = ["Ground Truth", "Prediction", "Mapping"]
    ax[-1].legend(handles=handles, labels=labels, loc="center")
    ax[-1].set_axis_off()
    fig.tight_layout()
    fig.suptitle(title)
    fig.savefig(outpath)


if __name__ == "__main__":
    graph_examples = {
        "Empty Ground Truth": [empty_gt()],
        "Empty Prediction": [empty_pred()],
        "Good Matching": [good_matched()],
        "False Negative Node": [fn_node_matched(t) for t in [0, 1, 2]],
        "False Negative Edge": [fn_edge_matched(t) for t in [0, 1]],
        "False Positive Node": [fp_node_matched(t) for t in [0, 1, 2]],
        "False Positive Edge": [fp_edge_matched(t) for t in [0, 1]],
        "Two Ground Truth to One Prediction": [two_to_one(t) for t in [0, 1, 2]],
        "One Ground Truth to Two Predictions": [one_to_two(t) for t in [0, 1, 2]],
    }
    outdir = Path("source/test_cases/matched_graph/")
    print(outdir.exists())
    for name, matched in graph_examples.items():
        print(name)
        outpath = outdir / f"{name}.svg"
        save_matched(matched, name)
