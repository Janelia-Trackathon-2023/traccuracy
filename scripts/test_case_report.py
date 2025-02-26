import glob
import json
import os
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import pytest
import seaborn as sns

ROOT_DIR = Path(__file__).resolve().parents[1]
SKIP_FILES = ["__", "base", "compute_overlap"]
SKIP_FUNCTIONS = [
    "basic_graph",
    "get_division_graphs",
    "basic_division",
    "basic_division_t0",
    "basic_division_t1",
    "basic_division_t2",
    "longer_division",
    "",
    "make_one_cell_2d",
    "make_split_cell_2d",
    "make_one_cell_3d",
    "make_split_cell_3d",
    "nodes_from_segmentation",
    "sphere",
]
GROUPS = {
    "track_errors": {
        "one-to-one": [
            "empty_gt",
            "empty_pred",
            "good_matched",
            "fn_node_matched",
            "fn_edge_matched",
            "fp_node_matched",
            "fp_edge_matched",
            "crossover_edge",
        ],
        # one gt to many pred
        "one-to-many": ["node_one_to_two", "edge_one_to_two"],
        # one pred to many gt
        "many to one": ["node_two_to_one", "edge_two_to_one"],
        "divisions": [
            "empty_pred_div",
            "empty_gt_div",
            "good_div",
            "fp_div",
            "one_child",
            "no_children",
            "wrong_child",
            "wrong_children",
        ],
        "shifted divisions": [
            "div_1early_end",
            "div_1early_mid",
            "div_2early_end",
            "div_2early_mid",
            "div_1late_end",
            "div_1late_mid",
            "div_2late_end",
            "div_2late_mid",
            "div_shift_min_match",
            "div_shift_bad_match_pred",
            "div_shift_bad_match_daughter",
        ],
    },
    "matchers": {
        "2d": [
            "good_segmentation_2d",
            "false_negative_segmentation_2d",
            "false_positive_segmentation_2d",
            "oversegmentation_2d",
            "undersegmentation_2d",
            "no_overlap_2d",
            "multicell_2d",
        ],
        "3d": [
            "good_segmentation_3d",
            "false_negative_segmentation_3d",
            "false_positive_segmentation_3d",
            "oversegmentation_3d",
            "undersegmentation_3d",
            "no_overlap_3d",
            "multicell_3d",
        ],
    },
}


def run_coverage(test_target, ex_module):
    test_dir = f"{ROOT_DIR}/tests/{test_target}"
    files = os.listdir(test_dir)

    for file in files:
        # Skip init and any testing of base class
        if not all(skip not in file for skip in SKIP_FILES):
            continue
        args = [
            "--cov-report",
            f"json:{test_target}-{os.path.basename(file)[:-3]}.json",
            f"{test_dir}/{file}",
            "--cov",
            f"tests.examples.{ex_module}",
        ]
        print(args)
        pytest.main(args)


def get_stats_from_json(json_path):
    with open(json_path) as f:
        data = json.load(f)

    target_file = next(iter(data["files"].keys()))
    rows, stats = [], []
    for fxn, d in data["files"][target_file]["functions"].items():
        # Skip functions that are utilities
        if fxn in SKIP_FUNCTIONS:
            continue
        rows.append(fxn)
        stats.append(d["summary"]["percent_covered"])

    colname = json_path.split("-")[-1][5:-5]

    df = pd.DataFrame({"functions": rows, colname: stats})
    df = df.set_index("functions")
    return df


def get_stats_df(target_key):
    files = glob.glob(f"{target_key}-*.json")
    dfs = []
    for f in files:
        dfs.append(get_stats_from_json(f))

    # Concatenate to single dataframe
    df = dfs[0].join(dfs[1])
    for sdf in dfs[2:]:
        df = df.join(sdf)

    return df


def plot_heatmap(df, name, ax, groups):
    # Add empty columns for spacing/grouping
    for group in groups.keys():
        df.loc[group] = [None] * len(df.columns)

    sort = []
    for group, fxns in groups.items():
        sort.append(group)
        sort.extend(fxns)

    # Check for any ungrouped functions
    ungrouped = df.drop(sort)
    if len(ungrouped) > 0:
        df.loc["Ungrouped"] = [None] * len(df.columns)
        sort.append("Ungrouped")
        sort.extend(ungrouped.index)

    sns.heatmap(
        df.loc[sort], linewidths=1, vmin=0, vmax=100, cmap="copper", ax=ax, cbar=False
    )
    ax.set_title(name)


if __name__ == "__main__":
    output_name = sys.argv[1]
    param_sets = [("track_errors", "graphs"), ("matchers", "segs")]

    dfs, maxcols, maxrows = [], [], []
    for name, target_mod in param_sets:
        run_coverage(name, target_mod)
        df = get_stats_df(name)
        dfs.append(df)
        maxcols.append(len(df.columns))
        maxrows.append(len(df))

    # Figsize params are really rough estimates to avoid hardcoded values
    fig, axes = plt.subplots(
        1,
        len(param_sets),
        figsize=(len(param_sets) * max(maxcols) * 2, max(maxrows) / 4),
    )
    for df, (name, _), ax in zip(dfs, param_sets, axes):
        plot_heatmap(df, name, ax, GROUPS[name])

    plt.tight_layout()
    plt.savefig(f"{output_name}.png")
