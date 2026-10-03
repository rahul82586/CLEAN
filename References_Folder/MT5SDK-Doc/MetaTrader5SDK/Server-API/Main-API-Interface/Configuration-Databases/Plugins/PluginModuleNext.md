[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Plugins](../Plugins.md) / PluginModuleNext

[Previous](PluginModuleTotal.md) | [Next](PluginModuleGet.md)

# IMTServerAPI::PluginModuleNext

Get a plugin module by the index.
    
    
    MTAPIRES  IMTServerAPI::PluginModuleNext(
       const UINT           pos,        // Position of the configuration
       IMTConPluginModule*  module      // An object of the plugin module configuration
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**module**  
[out] The plugin module configuration object. The module object must be first created using theIMTServerAPI::PluginModuleCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies a plugin configuration with a specified index to the module object.
