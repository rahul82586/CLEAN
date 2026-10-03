[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Plugins](../Plugins.md) / PluginParamCreate

[Previous](PluginModuleCreate.md) | [Next](PluginSubscribe.md)

# IMTAdminAPI::PluginParamCreate

Create an object of the plugin parameter.

C++
    
    
    IMTConParam*  IMTAdminAPI::PluginParamCreate()

.NET
    
    
    CIMTConParam  CIMTAdminAPI.PluginParamCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConParam](../../../../Configuration-Interfaces/Additional-Parameters/IMTConParam.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConParam::Release](../../../../Configuration-Interfaces/Additional-Parameters/IMTConParam/Release.md) method of this object.
