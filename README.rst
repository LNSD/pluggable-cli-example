=====================
Pluggable CLI Example
=====================

This is a proof of concept project that uses `Pluggy
<https://pluggy.readthedocs.io/en/stable/>`_  together with `Click
<https://click.palletsprojects.com/en/7.x/>`_  to make a CLI
application extendable through plugins mechanism.

This project is based on `Poetry <https://python-poetry.org/>`_, a python
packaging and dependency management tool.

Demo
----

1. Install dependencies (host and plugin). Activate a virtualenv if desired.

.. code-block::

   $ poetry install

2. Run the CLI app:

.. code-block::

   $ (.venv) pcli --help

.. code-block::

   Usage: pcli [OPTIONS] COMMAND [ARGS]...

     Pluggable Command-line example application.

   Options:
     --help  Show this message and exit.

   Commands:
     version   Print CLI version.
     workflow  Command group coming from the pluggable-cli-plugin.


.. code-block::

   $ (.venv) pcli workflow --help

.. code-block::

   Usage: pcli workflow [OPTIONS] COMMAND [ARGS]...

     Command group coming from the pluggable-cli-plugin.

   Options:
     --help  Show this message and exit.

   Commands:
     branch   Branch example command.
     clone    Clone example command.
     fetch    Clone example command.
     version  Version example command.


Project structure
-----------------

This example project is composed by two sub-projects:

* ``pluggable-cli:`` The host package.
* ``pluggable-cli-plugin:`` A simple example plugin package.

Development tasks
-----------------

Both packages come with a list of preconfigured `Invoke <http://docs.pyinvoke.org/en/stable/>`_ tasks.

.. code-block::

   $ invoke --list
   Available tasks:

     clean        Clean temporary files
     docs-build   Build module documentation.
     docs-clean   Clean generated documentation.
     install      Install all dependencies.
     lint-docs    Pydocstyle documentation style check.
     lint-style   PEP8 code style check.
     lint-types   MYPY static types check.
     test         Run unit tests.
