"""package description."""
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("traccuracy")
except PackageNotFoundError:
    __version__ = "uninstalled"

__author__ = "Track Gals"
__email__ = "draga.doncilapop1@monash.edu"

from .tracking_data import TrackingData
from .tracking_graph import TrackingGraph

__all__ = ["TrackingData", "TrackingGraph"]
