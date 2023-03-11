"""package description."""
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("cell_tracking_metrics")
except PackageNotFoundError:
    __version__ = "uninstalled"

__author__ = "Track Gals"
__email__ = "draga.doncilapop1@monash.edu"


all = ["TrackingData", "TrackingGraph"]
