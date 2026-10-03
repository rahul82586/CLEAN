[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Plugins](../Plugins.md) / PluginModuleGet

[Previous](PluginModuleNext.md) | [Next](../Data-Feeds.md)

# IMTAdminAPI::PluginModuleGet

Get the plugin module configuration by the name.

C++
    
    
    MTAPIRES  IMTAdminAPI::PluginModuleGet(
       const UINT64         server_id,     // Plugin ID
       LPCWSTR              name,          // The name of the plugin module
       IMTConPluginModule*  module         // An object of a plugin configuration
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.PluginModuleGet(
       ulong                server_id,     // Plugin ID
       string               name,          // The name of the plugin module
       CIMTConPluginModule  module         // An object of a plugin configuration
       )

Python
    
    
    AdminAPI.PluginModuleGet(
       server_id,           # Plugin ID
       name                 # The name of the plugin module
       )

### Parameters

**server_id**  
[in] The identifier of the server for which we get the plugin module configuration. TheIMTConServer::Idvalue is used as the identifier.

**name**  
[in] Name of the plugin module. TheIMTConPluginModule::Module()value is used as the name..

**module**  
[out] The plugin module configuration object. The module object must be first created using theIMTAdminAPI::PluginModuleCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
