# traccuracy: Evaluate Cell Tracking Solutions

[![License](https://img.shields.io/pypi/l/traccuracy.svg?color=green)](https://github.com/Janelia-Trackathon-2023/traccuracy/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/traccuracy.svg?color=green)](https://pypi.org/project/traccuracy)
[![Python Version](https://img.shields.io/pypi/pyversions/traccuracy.svg?color=green)](https://python.org)
[![CI](https://github.com/Janelia-Trackathon-2023/traccuracy/actions/workflows/ci.yml/badge.svg)](https://github.com/Janelia-Trackathon-2023/traccuracy/actions/workflows/ci.yml)
[![Documentation Status](https://readthedocs.org/projects/traccuracy/badge/?version=latest)](https://traccuracy.readthedocs.io/en/latest/?badge=latest)


`traccuracy` provides a suite of benchmarking functions that can be used to evaluate cell
tracking solutions against ground truth annotations. The goal of this library is to provide a convenient way to run rigorous evaluation and to document and consolidate the wide variety of
metrics used in the field.

`traccuracy` can compute a comprehensive set of metrics for evaluating the cell linking and division performance, and can compute biologically meaningful metrics such as number of correctly reconstructed lineages over N frames and cell cycle length accuracy. As matching ground truth and
predicted lineages is a crucial step for performing evaluation, `traccuracy` includes
a number of algorithms for matching ground truth and predicted lineages, both with
and without segmentation masks.

Learn more in the [documentation](https://traccuracy.readthedocs.io/en/latest/).

## Installation
`pip install traccuracy`
