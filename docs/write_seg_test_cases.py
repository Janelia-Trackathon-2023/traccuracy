import sys

sys.path.append("../tests/examples")
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from example_segmentations import (
    false_negative_segmentation_2d,
    false_positive_segmentation_2d,
    good_segmentation_2d,
    oversegmentation_2d,
    undersegmentation_2d,
)
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch


def save_pair(gt, pred, outpath, title):
    max_label = np.max([gt, pred])
    colors = ["black", "red", "blue", "green"]
    colormap = ListedColormap(colors)
    fig, ax = plt.subplots(1, 2, figsize=(6, 4))
    ax[0].imshow(gt, cmap=colormap, vmax=4)
    ax[0].set_title("Ground Truth")
    # ax[0].set_axis_off()
    ax[1].imshow(pred, cmap=colormap, vmax=4)
    ax[1].set_title("Predicted")

    handles = [Patch(color=colors[i]) for i in range(1, max_label + 1)]
    labels = [str(i) for i in range(1, max_label + 1)]
    ax[1].legend(handles=handles, labels=labels, title="Label IDs", loc="upper right")
    fig.suptitle(title)
    fig.tight_layout()
    fig.savefig(outpath)


if __name__ == "__main__":
    two_d_examples = {
        "Good Segmentation": good_segmentation_2d(),
        "False Positive": false_positive_segmentation_2d(),
        "False Negative": false_negative_segmentation_2d(),
        "Oversegmentation": oversegmentation_2d(),
        "Undersegmentation": undersegmentation_2d(),
    }
    outdir = Path("source/test_cases/segmentation/2d")
    print(outdir.exists())
    for name, arrs in two_d_examples.items():
        outpath = outdir / f"{name}.svg"
        gt, pred = arrs
        save_pair(gt, pred, outpath, name)
