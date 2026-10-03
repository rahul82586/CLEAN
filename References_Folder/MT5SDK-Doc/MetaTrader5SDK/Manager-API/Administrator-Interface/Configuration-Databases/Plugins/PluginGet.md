[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Plugins](../Plugins.md) / PluginGet

[Previous](PluginNext.md) | [Next](PluginModuleTotal.md)

# IMTAdminAPI::PluginGet

Get the plugin configuration by the name.

C++
    
    
    MTAPIRES  IMTAdminAPI::PluginGet(
       const UINT64   server_id,     // Server ID
       LPCWSTR        name,          // Plugin configuration name
       IMTConPlugin*  plugin         // An object of a plugin configuration
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.PluginGet(
       ulong          server_id,     // Server ID
       string         name,          // Plugin configuration name
       CIMTConPlugin  plugin         // An object of a plugin configuration
       )

Python
    
    
    AdminAPI.PluginGet(
       server_id,     # Server ID
       name           # Plugin configuration name
       )

### Parameters

**server_id**  
[in] The identifier of the server for which we get the plugin configuration. TheIMTConServer::Idvalue is used as the identifier.

**name**  
[in] Name of the plugin configuration. TheIMTConPlugin::Namevalue is used as the name.

**plugin**  
[out] An object of plugin configuration. The object must first be created using theIMTAdminAPI::PluginCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies parameters of the specified plugin configuration to the plugin object.
