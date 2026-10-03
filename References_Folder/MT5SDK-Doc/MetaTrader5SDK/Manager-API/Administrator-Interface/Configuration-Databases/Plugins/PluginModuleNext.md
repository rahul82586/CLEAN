[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Plugins](../Plugins.md) / PluginModuleNext

[Previous](PluginModuleTotal.md) | [Next](PluginModuleGet.md)

# IMTAdminAPI::PluginModuleNext

Get a plugin module by the index.

C++
    
    
    MTAPIRES  IMTAdminAPI::PluginModuleNext(
       const UINT           pos,        // Position of the configuration
       IMTConPluginModule*  module      // An object of the plugin module configuration
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.PluginModuleNext(
       uint                 pos,        // Position of the configuration
       CIMTConPluginModule  module      // An object of the plugin module configuration
       )

Python
    
    
    AdminAPI.PluginModuleNext(
       pos        # Position of the configuration
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**module**  
[out] The plugin module configuration object. The module object must be first created using theIMTAdminAPI::PluginModuleCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies a plugin configuration with a specified index to the module object.
