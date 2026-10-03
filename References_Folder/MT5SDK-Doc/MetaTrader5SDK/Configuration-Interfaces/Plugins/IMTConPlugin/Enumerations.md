[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Plugins](../../Plugins.md) / [IMTConPlugin](../IMTConPlugin.md) / Enumerations

[Previous](../IMTConPlugin.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConPlugin](../IMTConPlugin.md) class contains the following enumerations:

<a id="enpluginmode"></a>
## IMTConPlugin::EnPluginMode (#enpluginmode)

Modes of plugin operation are listed in IMTConPlugin::EnPluginMode.

ID | Value | Description  
PLUGIN_DISABLED | 0 | The plugin is disabled.  
PLUGIN_ENABLED | 1 | The plugin is enabled.  
PLUGIN_FIRST |  | Beginning of enumeration. It corresponds to PLUGIN_DISABLED.  
PLUGIN_LAST |  | End of enumeration. It corresponds to PLUGIN_ENABLED.  
  
This enumeration is used in the [IMTConPlugin::Mode](Mode.md) method.

<a id="enpluginflags"></a>
## IMTConPlugin::EnPluginFlags (#enpluginflags)

Flags of plugin operation are listed in IMTConPlugin::EnPluginFlags.

ID | Value | Description  
PLUGIN_FLAG_MAN_CONFIG | 1 | The plugin can be set up using the manager terminal. To be able to set up a plugin, a manager account must have the [IMTConManager::RIGHT_CFG_PLUGINS (#enmanagerrights)](../../Managers/IMTConManager/Enumerations.md#enmanagerrights) permission granted. Additionally for the Manager API application, the [IMTManagerAPI:PUMP_MODE_PLUGINS](../../../Manager-API/Manager-Interface/Connection-to-the-Server/Pumping-Modes.md) mode of pumping must be enabled.  
PLUGIN_FLAG_PROFILING | 2 | After enabling the profiling, the server will start gathering and writing to the journal the statistics on the processing of hooks and event handlers in the plugin: current state, number of calls, minimal, maximal and average time of processing as well as time of the last call. It is not recommended to keep this parameter enabled, as profiling decreases the plugin performance. More information about profiling is given in the "Administration \ Plugins" section of the MetaTrader 5 Administrator user guide.  
PLUGIN_NONE | 0 | Beginning of enumeration. It corresponds to the absence of flags.  
PLUGIN_ALL |  | End of enumeration. All flags are enabled.  
  
This enumeration is used in the [IMTConPlugin::Flags](Flags.md) method.
