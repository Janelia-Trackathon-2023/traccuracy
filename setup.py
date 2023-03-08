from setuptools import setup
from Cython.Build import cythonize
import numpy
from setuptools import Extension


extension = Extension(
    "cell_tracking_metrics.matchers.compute_overlap",
    ["src/cell_tracking_metrics/matchers/compute_overlap.pyx"],
    include_dirs=[numpy.get_include()],
)

setup(ext_modules=cythonize([extension]))
