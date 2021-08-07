# Python Exercism

[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/roghu/python-exercism/Tests)](https://github.com/roghu/python-exercism/actions)
[![Codecov](https://img.shields.io/codecov/c/github/roghu/python-exercism)](https://app.codecov.io/gh/roghu/python-exercism)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Solutions to [exercism](https://github.com/exercism/python).

## Python Versions

* 3.9

## Tests

To run everything:

```bash
nox
```

To run test:

```bash
nox -s tests

# Get coverage info
nox -s coverage
```

## Flake8

To run:

```bash
nox -s flake8
```

## Mypy

To run:

```bash
nox -s typing
```

## License

MIT LICENSE
