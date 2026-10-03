[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Plugins](../Plugins.md) / PluginNext

[Previous](PluginTotal.md) | [Next](PluginGet.md)

# IMTManagerAPI::PluginNext

Get the plugin configuration by the index.

C++
    
    
    MTAPIRES  IMTManagerAPI::PluginNext(
       const UINT     pos,        // Position of the configuration
       IMTConPlugin*  plugin      // An object of a plugin configuration
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.PluginNext(
       uint           pos,        // Position of the configuration
       CIMTConPlugin  plugin      // An object of a plugin configuration
       )

Python
    
    
    ManagerAPI.PluginNext(
       pos            # Position of the configuration
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**plugin**  
[out] An object of plugin configuration. The created object must be deleted by calling theIMTManagerAPI::PluginCreatemethod of this object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the configuration data of a plugin with a specified index to the plugin object.
