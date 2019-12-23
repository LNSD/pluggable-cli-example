"""Invoke task runner."""

import sys

import invoke
import shutil


# COMMON ########################################

@invoke.task(help={"no-dev": "Skip development dependencies."})
def install(c, no_dev=False):
    """Install all dependencies."""
    options = []
    if no_dev:
        options += ["--no-dev"]
    options = " ".join(options)
    c.run("poetry install {}".format(options))


@invoke.task
def clean(c):
    """Clean temporary files"""
    raise NotImplementedError


# LINT ##########################################

@invoke.task(help={"ignore-e501": "Ignore 'Line too long (E501) error'."})
def lint_style(c, ignore_e501=False):
    """PEP8 code style check."""
    options = []
    if ignore_e501:
        options += ["--ignore=E501"]
    options = " ".join(options)
    c.run("poetry run flake8 {} pcli".format(options))


@invoke.task
def lint_types(c):
    """MYPY static types check."""
    options = []
    if sys.version_info <= (2, 7):
        options += ["--py2"]
    options = " ".join(options)
    c.run("poetry run mypy {} pcli".format(options))


@invoke.task
def lint_docs(c):
    """Pydocstyle documentation style check."""
    c.run("poetry run pydocstyle pcli")


# TEST ##########################################

@invoke.task(help={
    "no-cov": "Disable coverage.",
    "tox": "Run test against all python versions (tox)"
})
def test(c, no_cov=False, tox=False):
    """Run unit tests."""
    if tox:
        c.run("tox")
        return

    options = []
    if no_cov:
        options += ["--no-cov"]
    options = " ".join(options)
    c.run("poetry run pytest {} tests".format(options))


# DOCS ##########################################

@invoke.task
def docs_build(c):
    """Build module documentation."""
    c.run("sphinx-build docs docs/_build")


@invoke.task
def docs_clean(c):
    """Clean generated documentation."""
    shutil.rmtree("docs/_build", ignore_errors=True)
