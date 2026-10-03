[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Plugins](../Plugins.md) / PluginModuleCreate

[Previous](PluginCreate.md) | [Next](PluginParamCreate.md)

# IMTServerAPI::PluginModuleCreate

Create an object of the plugin module configuration.
    
    
    IMTConPluginModule*  IMTServerAPI::PluginModuleCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConPluginModule](../../../../Configuration-Interfaces/Plugins/IMTConPluginModule.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMConPluginModule::Release](../../../../Configuration-Interfaces/Plugins/IMTConPluginModule/Release.md) method of this object.
