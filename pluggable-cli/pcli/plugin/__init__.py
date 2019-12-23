"""TODO Documentation."""

import pluggy
import pcli.plugin.hookspec


#: Marker to be imported and used in plugins (and for own implementations)
hookimpl = pluggy.HookimplMarker("pcli")


def _get_plugin_manager():
    """Get plugin manager."""
    pm = pluggy.PluginManager("pcli")
    pm.add_hookspecs(hookspec)
    pm.load_setuptools_entrypoints("pcli")
    return pm
