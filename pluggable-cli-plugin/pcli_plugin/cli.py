"""Pluggable Command-line tool example plugin."""

import click

import pcli.plugin
import pcli_plugin


@click.group()
def workflow():
    """Command group coming from the pluggable-cli-plugin."""
    pass


@click.command()
def version():
    """Version example command."""
    click.echo("PCLI Example plugin v{}".format(pcli_plugin.__version__))


@click.command()
def clone():
    """Clone example command."""
    click.echo("Clone command")


@click.command()
def fetch():
    """Clone example command."""
    click.echo("Fetch command")


@click.command()
def branch():
    """Branch example command."""
    click.echo("Branch command")


workflow.add_command(version)
workflow.add_command(clone)
workflow.add_command(fetch)
workflow.add_command(branch)


@pcli.plugin.hookimpl
def pcli_get_commands():
    """Get a list of commands.

    :return: List of commands
    """
    return [workflow]
