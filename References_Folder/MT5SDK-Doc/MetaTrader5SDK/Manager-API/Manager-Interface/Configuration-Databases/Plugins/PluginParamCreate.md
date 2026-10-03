[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Plugins](../Plugins.md) / PluginParamCreate

[Previous](PluginModuleCreate.md) | [Next](PluginUpdate.md)

# IMTManagerAPI::PluginParamCreate

Create an object of the plugin parameter.

C++
    
    
    IMTConParam*  IMTManagerAPI::PluginParamCreate()

.NET
    
    
    CIMTConParam  CIMTManagerAPI.PluginParamCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConParam](../../../../Configuration-Interfaces/Additional-Parameters/IMTConParam.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConParam::Release](../../../../Configuration-Interfaces/Additional-Parameters/IMTConParam/Release.md) method of this object.
