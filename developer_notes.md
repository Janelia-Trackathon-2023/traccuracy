# Traccuracy Developer Notes

## Development
For local development, clone the repo and install in editable mode.
```
git clone https://github.com/Janelia-Trackathon-2023/traccuracy.git
cd traccuracy
pip install -e ".[dev]"
```

### Testing
Install testing requirements
```
pip install -e ".[test]"
```
Run tests
```
python -m pytest tests
```
### Style
We utilize `pre-commit` with black (formatting) and ruff (linting). If you would like to run `pre-commit` locally:
```
pip install -e ".[dev]"
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
pip install -e ".[docs]"
# Run the build
sphinx-build docs/source docs/_build
```

Note that running documentation locally requires Pandoc to be installed as well - https://pandoc.org/installing.html.

You can view the documentation by opening `docs/_build/index.html` in your browser.