"""This submodule implements routines for Track Purity (TP) and Target Effectiveness (TE) scores.

Definitions (Bise et al., 2011; Chen, 2021; Fukai et al., 2022):

- TE for a single ground truth track T^g_j is calculated by finding the predicted track T^p_k that overlaps with T^g_j in the largest number of the frames and then dividing the overlap frame counts by the total frame counts for T^g_j. The TE for the total dataset is calculated as the mean of TEs for all ground truth tracks, weighted by the length of the tracks.

- TP is defined analogously, with T^g_j and T^p_j being swapped in the definition.
"""

from typing import TYPE_CHECKING
from typing import Dict
from typing import Optional
from typing import Sequence

import networkx as nx
import numpy as np
import pandas as pd

from ._base import Metric

if TYPE_CHECKING:
    from ._base import Matched

class TrackOverlapMetrics(Metric):
    supports_many_to_one = True
    
    def __init__(self, matched_data: "Matched"):
        super().__init__(matched_data)

    def compute(self):
            
        self.data.gt_graph
        
        # requires tracklets that also have the splitting and merging edges
        gt_tree = nx.from_edgelist(order_edges(true_edges), create_using=nx.DiGraph)
        pred_tree = nx.from_edgelist(
            order_edges(predicted_edges), create_using=nx.DiGraph
        )
        gt_track_df, gt_split_df, _gt_merge_df = convert_tree_to_dataframe(gt_tree)
        pred_track_df, pred_split_df, _pred_merge_df = convert_tree_to_dataframe(
            pred_tree
        )
        gt_track_df = gt_track_df.reset_index()
        pred_track_df = pred_track_df.reset_index()

        gt_track_df = _add_split_edges(gt_track_df, gt_split_df)
        pred_track_df = _add_split_edges(pred_track_df, pred_split_df)
        
        # edgess are a list of edges, grouped by the tracks
        gt_edgess = _df_to_edges(gt_track_df)
        pred_edgess = _df_to_edges(pred_track_df)
        
        # filter out edges that are not in the include_frames and exclude_true_edges
        filter_edges = (
            lambda e: e[0][0] in include_frames and e not in exclude_true_edges
        )
        pred_edgess = [
            [e for e in edges if filter_edges(e)] for edges in pred_edgess
        ]
        gt_edgess = [[e for e in edges if filter_edges(e)] for edges in gt_edgess]
        
        # calculate track purity and target effectiveness
        track_purity = _calc_overlap_score(pred_edgess, gt_edgess)
        target_effectiveness = _calc_overlap_score(gt_edgess, pred_edgess)
        return {
            "track_purity": track_purity,
            "target_effectiveness": target_effectiveness,
        }

def _calc_overlap_score(reference_edgess, overlap_edgess):
    correct_count = 0
    for reference_edges in reference_edgess:
        overlaps = [
            len(set(reference_edges) & set(overlap_edges))
            for overlap_edges in overlap_edgess
        ]
        max_overlap = max(overlaps)
        correct_count += max_overlap
    total_count = sum([len(reference_edges) for reference_edges in reference_edgess])
    return correct_count / total_count if total_count > 0 else -1


