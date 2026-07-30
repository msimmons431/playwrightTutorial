import nox

# Define which folders/files to target
TARGET_CODE = ["src", "tests", "noxfile.py"]

@nox.session(python=["3.10", "3.11", "3.12"])
def lint(session: nox.Session) -> None:
    """Run isort to fix imports, then run pylint to analyze code."""
    # Install dependencies in the isolated environment
    session.install("isort", "pylint")
    
    # 1. Run isort to automatically fix and sort import formatting
    session.run("isort", *TARGET_CODE)
    
    # 2. Run pylint to report bugs and style issues (does not auto-fix)
    session.run("pylint", *TARGET_CODE)

