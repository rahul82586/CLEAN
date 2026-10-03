[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Configuration Databases](../Configuration-Databases.md) / Plugins

[Previous](Spreads/SpreadNext.md) | [Next](Plugins/PluginCreate.md)

# Configuration of Plugins

Functions described in this section allow managing plugin configurations. The following functions for managing plugins are available:

Function | Purpose  
---|---  
[PluginCreate](Plugins/PluginCreate.md) | Create an object of the plugin configuration.  
[PluginModuleCreate](Plugins/PluginModuleCreate.md) | Create an object of the plugin module configuration.  
[PluginParamCreate](Plugins/PluginParamCreate.md) | Create an object of the plugin parameter.  
[PluginUpdate](Plugins/PluginUpdate.md) | Update a plugin configuration.  
[PluginTotal](Plugins/PluginTotal.md) | The total number of plugin configurations available on the trade server.  
[PluginNext](Plugins/PluginNext.md) | Get the plugin configuration by the index.  
[PluginGet](Plugins/PluginGet.md) | Get the plugin configuration by the name.  
  
When working via the manager interface (IMTManagerAPI) the application only has access to the plugins, in which the "Configurable by managers" option is enabled ([IMTConPlugin::PLUGIN_FLAG_MAN_CONFIG (#enpluginflags)](../../../Configuration-Interfaces/Plugins/IMTConPlugin/Enumerations.md#enpluginflags)). In addition:

  * When connecting to the main trade server, the application only has access to the plugins, which are installed on the same server or on the history server ([IMTConPlugin::Server](../../../Configuration-Interfaces/Plugins/IMTConPlugin/Server.md)).
  * When connecting to a regular trading server, the application can only access the plugins which are installed in the same server.



During operation via the administrator interface ([IMTAdminAPI](../../Administrator-Interface/Configuration-Databases/Plugins.md)), the following plugins are available to the application:

  * When connected to the main trade server: all plugins within the platform.
  * When connected to a regular trading server: all plugins installed in the same server or on the history server.



> To manage plugin configurations, the pumping mode [IMTManagerAPI::PUMP_MODE_PLUGINS](../Connection-to-the-Server/Pumping-Modes.md) must be enabled for the Manager API application. Also, the [IMTConPlugin::PLUGIN_FLAG_MAN_CONFIG (#enpluginflags)](../../../Configuration-Interfaces/Plugins/IMTConPlugin/Enumerations.md#enpluginflags) flag must be enabled for the plugin and the [IMTConManager::RIGHT_CFG_PLUGINS (#enmanagerrights)](../../../Configuration-Interfaces/Managers/IMTConManager/Enumerations.md#enmanagerrights) permission must be enabled for the manager account.
