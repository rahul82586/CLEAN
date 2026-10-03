[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Plugins](../Plugins.md) / PluginNext

[Previous](PluginTotal.md) | [Next](PluginGet.md)

# IMTAdminAPI::PluginNext

Get the plugin configuration by the index.

C++
    
    
    MTAPIRES  IMTAdminAPI::PluginNext(
       const UINT     pos,        // Position of the configuration
       IMTConPlugin*  plugin      // An object of a plugin configuration
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.PluginNext(
       uint           pos,        // Position of the configuration
       CIMTConPlugin  plugin      // An object of a plugin configuration
       )

Python
    
    
    AdminAPI.PluginNext(
       pos            # Position of the configuration
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**plugin**  
[out] An object of plugin configuration. The plugin object must be first created using theIMTAdminAPI::PluginCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the configuration data of a plugin with a specified index to the plugin object.
