"""package description."""
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("traccuracy")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "uninstalled"

from ._tracking_graph import EdgeAttr, NodeAttr, TrackingGraph

# must go after TrackingGraph to avoid circular imports
from ._run_metrics import run_metrics  # isort:skip

__all__ = ["TrackingGraph", "run_metrics", "NodeAttr", "EdgeAttr"]
