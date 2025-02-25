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


def plot_heatmap(df, name, ax):
    sns.heatmap(df, linewidths=1, vmin=0, vmax=100, cmap="copper", ax=ax)
    plt.xticks(rotation=45, ha="right")
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
        plot_heatmap(df, name, ax)
    plt.tight_layout()

    plt.savefig(f"{output_name}.png")
