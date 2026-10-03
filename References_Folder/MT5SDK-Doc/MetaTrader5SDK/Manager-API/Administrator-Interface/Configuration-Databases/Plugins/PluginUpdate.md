[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Plugins](../Plugins.md) / PluginUpdate

[Previous](PluginUnsubscribe.md) | [Next](PluginUpdateBatch.md)

# IMTAdminAPI::PluginUpdate

Add and update a plugin configuration.

C++
    
    
    MTAPIRES  IMTAdminAPI::PluginUpdate(
       IMTConPlugin*  plugin      // An object of a plugin configuration
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.PluginUpdate(
       CIMTConPlugin  plugin      // An object of a plugin configuration
       )

Python
    
    
    AdminAPI.PluginUpdate(
       plugin         # An object of a plugin configuration
       )

### Parameters

**plugin**  
[in] An object of plugin configuration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can be added or updated only from the applications that run on the main server. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned.
