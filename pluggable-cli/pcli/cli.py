"""Pluggable Command-line tool."""

import itertools

import click
import pcli
import pcli.plugin


@click.group()
def cli():
    """Pluggable Command-line example application."""
    pass


@click.command()
def version():
    """Print CLI version."""
    click.echo("Pluggable CLI v{}".format(pcli.__version__))


def main():
    """Command-line documentation."""
    pm = pcli.plugin._get_plugin_manager()

    # Build command-line
    cli.add_command(version)
    commands = pm.hook.pcli_get_commands()
    for cmd in itertools.chain(*commands):
        cli.add_command(cmd)

    # Run command root
    cli()


if __name__ == '__main__':
    main()
