# traccuracy

[![License](https://img.shields.io/pypi/l/traccuracy.svg?color=green)](https://github.com/Janelia-Trackathon-2023/traccuracy/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/traccuracy.svg?color=green)](https://pypi.org/project/traccuracy)
[![Python Version](https://img.shields.io/pypi/pyversions/traccuracy.svg?color=green)](https://python.org)
[![CI](https://github.com/Janelia-Trackathon-2023/traccuracy/actions/workflows/ci.yml/badge.svg)](https://github.com/Janelia-Trackathon-2023/traccuracy/actions/workflows/ci.yml)
[![Documentation Status](https://readthedocs.org/projects/traccuracy/badge/?version=latest)](https://traccuracy.readthedocs.io/en/latest/?badge=latest)


`traccuracy` provides a suite of benchmarking functions that can be used to evaluate tracking solutions against ground truth annotations. It includes the standard metrics that are calculated by the [Cell Tracking Challenge](http://celltrackingchallenge.net/evaluation-methodology/).

Learn more in the [documentation](https://traccuracy.readthedocs.io/en/latest/).

## Installation
`pip install traccuracy`

## Development
For local development, clone the repo and install in editable mode.
```
git clone https://github.com/Janelia-Trackathon-2023/traccuracy.git
cd traccuracy
pip install -e .[dev]
```

### Testing
Install testing requirements
```
pip install -e .[test]
```
Run tests
```
python -m pytest tests
```
### Style
We utilize `pre-commit` with black (formatting) and ruff (linting). If you would like to run `pre-commit` locally:
```
pip install -e .[dev]
pre-commit install
```
Alternatively [pre-commit.ci](https://pre-commit.ci/), will run and commit changes on any open PRs.

### Releases
In order to deploy a new version, tag the commit with a version number and push it to github. This will trigger a github action that will build and deploy to PyPI. (see the "deploy" step in workflows/ci.yml). The version number is determined automatically based on the tag.
```
git tag -a v0.1.0 -m v0.1.0
git push --follow-tags
```

### Documentation
Documentation is built with Sphinx using `sphinx-autoapi` to automatically generate API documentation at build time. Docs are hosted on ReadTheDocs and build automatically after each push to main. Documentation can be built locally by running the following:
```
# Install docs requirements
pip install -e .[docs]
# Run the build
sphinx-build docs/source docs/_build
```

You can view the documentation by opening `docs/_build/index.html` in your browser.