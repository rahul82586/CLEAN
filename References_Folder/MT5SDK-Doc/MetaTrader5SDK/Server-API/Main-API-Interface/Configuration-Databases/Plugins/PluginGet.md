[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Plugins](../Plugins.md) / PluginGet

[Previous](PluginNext.md) | [Next](PluginModuleTotal.md)

# IMTServerAPI::PluginGet

Get the plugin configuration by the name.
    
    
    MTAPIRES  IMTServerAPI::PluginGet(
       LPCWSTR        name,       // Name of the configuration
       IMTConPlugin*  plugin      // An object of a plugin configuration
       )

### Parameters

**name**  
[in] The name of the configuration.

**plugin**  
[out] An object of plugin configuration. The plugin object must be first created using theIMTServerAPI::PluginCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConPlugin::Name()](../../../../Configuration-Interfaces/Plugins/IMTConPlugin/Name.md) value is used as the name.

This method allows getting plugin configurations created for the server where the plugin is running.

# IMTServerAPI::PluginGet

Get the plugin configuration by the name considering the server.
    
    
    MTAPIRES  IMTServerAPI::PluginGet(
       UINT64         server,     // Server ID
       LPCWSTR        name,       // Name of the configuration
       IMTConPlugin*  plugin      // An object of a plugin configuration
       )

### Parameters

**server**  
[in] Identifier of the server the plugin configuration is created for.

**name**  
[in] The name of the configuration.

**plugin**  
[out] An object of plugin configuration. The plugin object must be first created using theIMTServerAPI::PluginCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConPlugin::Name()](../../../../Configuration-Interfaces/Plugins/IMTConPlugin/Name.md) value is used as the name.
