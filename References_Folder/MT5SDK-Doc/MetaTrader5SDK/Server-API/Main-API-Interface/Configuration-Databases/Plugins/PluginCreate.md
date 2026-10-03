[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Plugins](../Plugins.md) / PluginCreate

[Previous](../Plugins.md) | [Next](PluginModuleCreate.md)

# IMTServerAPI::PluginCreate

Create an object of the plugin configuration.
    
    
    IMTConPlugin*  IMTServerAPI::PluginCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConPlugin](../../../../Configuration-Interfaces/Plugins/IMTConPlugin.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTConPlugin::Release](../../../../Configuration-Interfaces/Plugins/IMTConPlugin/Release.md) method of this object.
