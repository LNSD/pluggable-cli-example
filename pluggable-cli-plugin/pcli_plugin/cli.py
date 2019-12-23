"""Pluggable Command-line tool example plugin."""

import click

import pcli.plugin


@click.group()
def workflow():
    """Command group coming from the pluggable-cli-plugin."""
    click.echo("Workflow command")


@pcli.plugin.hookimpl
def pcli_get_commands():
    """Get a list of commands.

    :return: List of commands
    """
    return [v for v in globals().values()
            if isinstance(v, click.core.BaseCommand)]
