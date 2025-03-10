# ---
# jupyter:
#   jupytext:
#     custom_cell_magics: kql
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: motile-tracker
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Matching Test Cases

# %% [markdown]
# To facilitate testing, we have provided a suite of canonical
# examples that cover the basic scenarios that can occur in matching. Here we describe
# them and show visualizations of each case.
#
# Matchers should test all the matching cases, either by matching the segmentations
# or using points extracted from them. The segmentation examples are generated by
# functions in the `tests/examples/` directory, and there is a function provided to
# extract centroid nodes from the segmentations for testing point-based matchers.
#
# Note: for visualization purposes, the center node locations only show one decimal place
# of precision.

# %% nbsphinx="hidden"
import sys

sys.path.append("../../../tests")

# %%
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch

import examples.segs as ex_segs

# %% [markdown]
#
# Each example that is illustrated here in 2D is also implemented in 3d.


# %% nbsphinx="hidden"
def plot_one(seg, axis, colors):
    colormap = ListedColormap(colors)
    axis.imshow(seg, cmap=colormap, vmax=5, origin="lower")
    axis.set_xlabel("x")
    axis.set_ylabel("y")
    axis.set_xticks([])
    axis.set_yticks([])

    nodes = ex_segs.nodes_from_segmentation(seg, frame=0)
    x = [attrs["x"] for _id, attrs in nodes.items()]
    y = [attrs["y"] for _id, attrs in nodes.items()]
    axis.scatter(x, y, color="white")

    for xval, yval in zip(x, y):
        axis.annotate(
            f" ({xval:.1f},\n {yval:.1f})",
            xy=(xval, yval),
            textcoords="data",
            color="white",
        )


def plot_pair(gt, pred, title):
    max_label = np.max([gt, pred])
    colors = ["black", "red", "blue", "green", "purple"]
    fig, ax = plt.subplots(1, 2, figsize=(6, 4))
    plot_one(gt, ax[0], colors)
    ax[0].set_title("Ground Truth")
    plot_one(pred, ax[1], colors)
    ax[1].set_title("Predicted")

    handles = [Patch(color=colors[i]) for i in range(1, max_label + 1)]
    labels = [str(i) for i in range(1, max_label + 1)]
    ax[1].legend(handles=handles, labels=labels, title="Label IDs", loc="upper right")
    fig.suptitle(title, y=0.9)
    fig.tight_layout()


# %%
plot_pair(*ex_segs.good_segmentation_2d(), "Good Segmentation")

# %%
plot_pair(*ex_segs.false_positive_segmentation_2d(), "False Positive")

# %%
plot_pair(*ex_segs.false_negative_segmentation_2d(), "False Negative")

# %%
plot_pair(*ex_segs.oversegmentation_2d(), "Oversegmentation")

# %%
plot_pair(*ex_segs.undersegmentation_2d(), "Undersegmentation")

# %%
plot_pair(*ex_segs.no_overlap_2d(), "No Overlap")

# %%
plot_pair(*ex_segs.multicell_2d(), "Multiple cells")

# %%

# %%
