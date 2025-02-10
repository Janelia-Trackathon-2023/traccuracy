# %% [markdown]
# # Node Error Types
#
# This set of node errors applies only to graphs with a one-to-one matching.

# %% nbsphinx="hidden"
import sys

sys.path.append("../../../tests")

import matplotlib.pyplot as plt
from matplotlib.patches import Patch

import examples.graphs as ex_graphs
from traccuracy._tracking_graph import TrackingGraph


def get_loc(graph, node):
    return graph.graph.nodes[node]["t"], graph.graph.nodes[node]["y"]


def plot_graph(
    ax, graph: TrackingGraph, color="black", annotations={}, ann_color="red"
):
    if graph.graph.number_of_nodes() == 0:
        return [0, 0], [0, 0]
    ids = list(graph.graph.nodes)
    x = [graph.graph.nodes[node]["t"] for node in ids]
    y = [graph.graph.nodes[node]["y"] for node in ids]
    ax.scatter(x, y, color=color)
    for _x, _y, _id in zip(x, y, ids):
        ax.text(_x + 0.05, _y + 0.05, str(_id))
        # Plot annotation if available
        ann = annotations.get(_id)
        if ann:
            ax.text(
                _x - 0.1, _y - 0.25, ann, color="purple", horizontalalignment="right"
            )

    for u, v in graph.graph.edges():
        xs = [graph.graph.nodes[u]["t"], graph.graph.nodes[v]["t"]]
        ys = [graph.graph.nodes[u]["y"], graph.graph.nodes[v]["y"]]
        ax.plot(xs, ys, color=color)

    return [max(x), min(x)], [max(y), min(y)]


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


def plot_matched(examples, annotations, suptitle, titles):
    gt_color = "black"
    pred_color = "blue"
    mapping_color = "grey"

    if len(examples) > 1:
        yheight = 2.5
    else:
        yheight = 2

    fig, ax = plt.subplots(
        1, len(examples) + 1, figsize=(3 * len(examples) + 1, yheight)
    )
    for i, (matched, anns, title) in enumerate(zip(examples, annotations, titles)):
        axis = ax[i]
        xbounds, ybounds = plot_graph(
            axis, matched.gt_graph, color=gt_color, annotations=anns
        )
        bounds = plot_graph(
            axis, matched.pred_graph, color=pred_color, annotations=anns
        )
        xbounds.extend(bounds[0])
        ybounds.extend(bounds[1])
        plot_matching(axis, matched, color=mapping_color)
        axis.set_ybound(min(ybounds) - 0.5, max(ybounds) + 0.5)
        axis.set_xbound(min(xbounds) - 0.5, max(xbounds) + 0.5)
        axis.set_ylabel("Y Value")
        axis.set_xlabel("Time")
        axis.set_title(title)

    handles = [
        Patch(color=gt_color),
        Patch(color=pred_color),
        Patch(color=mapping_color),
        Patch(color="purple"),
    ]
    labels = ["Ground Truth", "Prediction", "Mapping", "Node Annotations"]
    ax[-1].legend(handles=handles, labels=labels, loc="center")
    ax[-1].set_axis_off()
    plt.tight_layout()
    fig.suptitle(suptitle, y=1.1)
    plt.show()


# %% [markdown]
# ## True Positive
# A true positive node is defined as a predicted node that matches to only one
# ground truth node. Additionally, the corresponding ground truth node cannot be
# matched to more than one predicted node. True positives are annotated on both
# the ground truth and the division graph.

# %% [markdown]
# ## False Positive
# A false positive node is a node on the predicted graph does not match to a
# node on the ground truth graph. False positives are annotated on the predicted
# graph.

# %%
plot_matched([ex_graphs.fp_edge_matched(1)], [{7: "FP", 8: "FP"}], "", [""])

# %% [markdown]
# ## False Negative
# A false negative node is a node on the ground truth graph that is not matched
# to a predicted node. False negatives are annotated on the ground truth graph.

# %%
plot_matched([ex_graphs.fn_node_matched(2)], [{3: "FN"}], "", [""])
