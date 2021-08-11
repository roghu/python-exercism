import os

import nox

os.environ.update({"PDM_IGNORE_SAVED_PYTHON": "1"})

nox.options.reuse_existing_virtualenvs = True
nox.options.stop_on_first_error = True


@nox.session
def tests(session: nox.Session) -> None:
    session.run("pdm", "install", "-ds", "test", external=True)
    session.run("pytest", "-n", "2")


@nox.session
def flake8(session: nox.Session) -> None:
    session.run("pdm", "install", "-ds", "test", external=True)
    session.run("pdm", "install", "-ds", "flake8", external=True)
    session.run("pytest", "-n", "2", "--flake8")


@nox.session
def typing(session: nox.Session) -> None:
    session.run("pdm", "install", "-ds", "test", external=True)
    session.run("pdm", "install", "-ds", "typing", external=True)
    session.run("pytest", "-n", "2", "--mypy")


@nox.session
def coverage(session: nox.Session) -> None:
    session.run("pdm", "install", "-ds", "test", external=True)
    session.run("pytest", "-n", "2", "--cov", "src/")
    session.run("coverage", "xml")
    session.run("coverage", "report", "--show-missing")
