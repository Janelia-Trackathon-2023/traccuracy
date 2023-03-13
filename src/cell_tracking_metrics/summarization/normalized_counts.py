from .metrics import Metrics


class NormalizedCounts(Metrics):
    """Normalize the track and division counts by a given value.

    Currently supports:
        'gt_edges' - the number of ground truth edges
    """
    def __init__(self, track_events, ground_truth, normalize_by="gt_edges"):
        super().__init__(track_events, ground_truth=ground_truth)
        self.normalize_by = normalize_by
        if self.normalize_by == 'gt_edges':
            self.denom = len(self.ground_truth.edges())
        else:
            raise ValueError(f"List of supported values for normalize_by: ['gt_edges']. Got {self.normalize_by}.") 

    def compute_metrics(self):
        metrics =  self.compute_division_metrics()
        for attr in vars(self.track_events):
            if attr == "division_counts":
                continue
            value = self.track_events[attr]
            if value is not None:
                metrics[attr] = value / self.denom
        return metrics
    
    def compute_division_metrics(self):
        metrics = {}
        for frame_buffer, division_events in self.track_events.division_counts:
            for attr in vars(division_events):
                value = self.track_events[attr]
                if value is not None:
                    metrics[attr + f"_{frame_buffer}"] = value / self.denom
        return metrics