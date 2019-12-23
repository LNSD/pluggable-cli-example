"""Pluggable Command-line tool example plugin."""

import click

import pcli.plugin


@click.command()
def workflow():
    click.echo("Workflow command")


@pcli.plugin.hookimpl
def pcli_get_commands():
    """Get a list of commands.

    :return: List of commands
    """
    return [workflow]
