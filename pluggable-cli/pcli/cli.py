"""Pluggable Command-line tool."""

import click

import pcli.plugin
from pcli.__meta__ import __version__


@click.group()
def cli():
    pass


@click.command()
def version():
    click.echo(__version__)


def main():
    """Command-line documentation."""
    pm = pcli.plugin._get_plugin_manager()

    # Build command-line
    cli.add_command(version)
    for cmd in pm.hook.pcli_get_commands():
        cli.add_command(cmd)

    # Run command root
    cli()


if __name__ == '__main__':
    main()