# Python Exercism

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/roghu/python-exercism/Tests)
![Codecov](https://img.shields.io/codecov/c/github/roghu/python-exercism)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Solutions to [exercism](https://github.com/exercism/python).

## Python Versions

* 3.9

## Requirements

* [Poetry](https://python-poetry.org)

## Install Packages

```bash
poetry install
```

## Tests

To run unit tests:

```bash
poetry run tox
```

### Flake8

To run:

```bash
poetry run tox -e flake8
```

### Mypy

To run:

```bash
poetry run tox -e typing
```

### All Tests

```bash
poetry run tox -e ALL
```


## License

MIT LICENSE
