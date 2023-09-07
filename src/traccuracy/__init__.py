"""package description."""
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("traccuracy")
except PackageNotFoundError:
    __version__ = "uninstalled"

from ._run_metrics import run_metrics
from ._tracking_data import TrackingData
from ._tracking_graph import EdgeAttr, NodeAttr, TrackingGraph

__all__ = ["TrackingData", "TrackingGraph", "run_metrics",
           "NodeAttr", "EdgeAttr"]
