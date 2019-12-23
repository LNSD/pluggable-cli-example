"""TODO Documentation."""

import pluggy

hookspec = pluggy.HookspecMarker("pcli")


@hookspec
def pcli_get_commands():
    """Get a list of commands.

    :return: List of commands
    """

