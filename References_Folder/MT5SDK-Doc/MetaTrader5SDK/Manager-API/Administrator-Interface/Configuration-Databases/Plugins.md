[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Configuration Databases](../Configuration-Databases.md) / Plugins

[Previous](Network/TLSCertificateNext.md) | [Next](Plugins/PluginCreate.md)

# Configuration of Plugins

Functions allow managing plugin configurations, as well subscribe and unsubscribe from events associated with their change.

The following functions for managing plugins are available:

Function | Purpose  
---|---  
[PluginCreate](Plugins/PluginCreate.md) | Create an object of the plugin configuration.  
[PluginModuleCreate](Plugins/PluginModuleCreate.md) | Create an object of the plugin module configuration.  
[PluginParamCreate](Plugins/PluginParamCreate.md) | Create an object of the plugin parameter.  
[PluginSubscribe](Plugins/PluginSubscribe.md) | Subscribe to events associated with the configuration of plugins.  
[PluginUnsubscribe](Plugins/PluginUnsubscribe.md) | Unsubscribe from events associated with the configuration of plugins.  
[PluginUpdate](Plugins/PluginUpdate.md) | Add and update a plugin configuration.  
[PluginUpdateBatch](Plugins/PluginUpdateBatch.md) | Add or edit multiple plugin configurations.  
[PluginDelete](Plugins/PluginDelete.md) | Delete a plugin configuration by the name or index.  
[PluginDeleteBatch](Plugins/PluginDeleteBatch.md) | Delete multiple plugin configurations.  
[PluginShift](Plugins/PluginShift.md) | Changes the position of a plugin configuration in the list.  
[PluginTotal](Plugins/PluginTotal.md) | The total number of plugin configurations available in the platform.  
[PluginNext](Plugins/PluginNext.md) | Get the plugin configuration by the index.  
[PluginGet](Plugins/PluginGet.md) | Get the plugin configuration by the name.  
[PluginModuleTotal](Plugins/PluginModuleTotal.md) | The total number of configurations of plugin modules (DLL files) available in the platform.  
[PluginModuleNext](Plugins/PluginModuleNext.md) | Get a plugin module by the index.  
[PluginModuleGet](Plugins/PluginModuleGet.md) | Get the plugin module configuration by the name.  
  
When working via the manager interface ([IMTManagerAPI](../../Manager-Interface/Configuration-Databases/Plugins.md)) the application only has access to the plugins, in which the "Configurable by managers" option is enabled ([IMTConPlugin::PLUGIN_FLAG_MAN_CONFIG (#enpluginflags)](../../../Configuration-Interfaces/Plugins/IMTConPlugin/Enumerations.md#enpluginflags)). In addition:

  * When connecting to the main trade server, the application only has access to the plugins, which are installed on the same server or on the history server ([IMTConPlugin::Server](../../../Configuration-Interfaces/Plugins/IMTConPlugin/Server.md)).
  * When connecting to a regular trading server, the application can only access the plugins which are installed in the same server.



During operation via the administrator interface (IMTAdminAPI), the following plugins are available to the application:

  * When connected to the main trade server: all plugins within the platform.
  * When connected to a regular trading server: all plugins installed in the same server or on the history server.



> In order to be able to manage plugin configurations, the [IMTConManager::RIGHT_CFG_PLUGINS (#enmanagerrights)](../../../Configuration-Interfaces/Managers/IMTConManager/Enumerations.md#enmanagerrights) permission must be enabled for the manager account which is used by the Manager API application.
