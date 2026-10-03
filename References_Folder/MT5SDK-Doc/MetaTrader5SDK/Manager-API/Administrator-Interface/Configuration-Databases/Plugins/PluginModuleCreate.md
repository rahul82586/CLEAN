[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Plugins](../Plugins.md) / PluginModuleCreate

[Previous](PluginCreate.md) | [Next](PluginParamCreate.md)

# IMTAdminAPI::PluginModuleCreate

Create an object of the plugin module configuration.

C++
    
    
    IMTConPluginModule*  IMTAdminAPI::PluginModuleCreate()

.NET
    
    
    CIMTConPluginModule  CIMTAdminAPI.PluginModuleCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConPluginModule](../../../../Configuration-Interfaces/Plugins/IMTConPluginModule.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTConPluginModule::Release](../../../../Configuration-Interfaces/Plugins/IMTConPluginModule/Release.md) of this object.
