import nox


@nox.session
def tests(session: nox.Session) -> None:
    session.run("pip", "install", "-r", "requirements.txt")
    session.run("pytest", "-n", "2")


@nox.session
def flake8(session: nox.Session) -> None:
    session.run("pip", "install", "-r", "requirements.txt")
    session.run("pytest", "-n", "2", "--flake8")


@nox.session
def typing(session: nox.Session) -> None:
    session.run("pip", "install", "-r", "requirements.txt")
    session.run("pytest", "-n", "2", "--mypy")


@nox.session
def coverage(session: nox.Session) -> None:
    session.run("pip", "install", "-r", "requirements.txt")
    session.run("pytest", "-n", "2", "--cov", "src/")
    session.run("coverage", "xml")
    session.run("coverage", "report", "--show-missing")
