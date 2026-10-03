[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Plugins](../Plugins.md) / PluginModuleGet

[Previous](PluginModuleNext.md) | [Next](../Data-Feeds.md)

# IMTServerAPI::PluginModuleGet

Get the plugin module configuration by the name.
    
    
    MTAPIRES  IMTServerAPI::PluginModuleGet(
       LPCWSTR              name,       // The name of the module
       IMTConPluginModule*  module      // An object of the plugin module configuration
       )

### Parameters

**name**  
[in] The name of a plugin module.

**module**  
[out] The plugin module configuration object. The module object must be first created using theIMTServerAPI::PluginModuleCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConPluginModule::Name](../../../../Configuration-Interfaces/Plugins/IMTConPluginModule/Name.md) value is used as the name.

# IMTServerAPI::PluginModuleGet

Get the plugin module configuration by the name considering the server.
    
    
    MTAPIRES  IMTServerAPI::PluginModuleGet(
       UINT64               server,     // Server ID
       LPCWSTR              name,       // The name of the module
       IMTConPluginModule*  module      // An object of the plugin module configuration
       )

### Parameters

**server**  
[in] Identifier of the server the configuration of plugin module is created for.

**name**  
[in] The name of a plugin module.

**module**  
[out] The plugin module configuration object. The module object must be first created using theIMTServerAPI::PluginModuleCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConPluginModule::Name](../../../../Configuration-Interfaces/Plugins/IMTConPluginModule/Name.md) value is used as the name.
