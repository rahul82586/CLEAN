[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Plugins](../Plugins.md) / PluginDelete

[Previous](PluginUpdateBatch.md) | [Next](PluginDeleteBatch.md)

# IMTAdminAPI::PluginDelete

Delete a plugin configuration by the name.

C++
    
    
    MTAPIRES  IMTAdminAPI::PluginDelete(
       const UINT64  server_id,     // Server ID
       LPCWSTR       name           // Plugin configuration name
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.PluginDelete(
       ulong         server_id,     // Server ID
       string        name           // Plugin configuration name
       )

Python
    
    
    AdminAPI.PluginDelete(
       server_id,    # Server ID
       name          # Plugin configuration name
       )

### Parameters

**server_id**  
[in] The identifier of the server for which we delete the plugin configuration. TheIMTConServer::Idvalue is used as the identifier.

**name**  
[in] Name of the plugin configuration. TheIMTConPlugin::Namevalue is used as the name.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can be deleted only when connecting to the main server. In all other cases the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) will be returned.

# IMTAdminAPI::PluginDelete

Deleting a plugin configuration by the index.

C++
    
    
    MTAPIRES  IMTAdminAPI::PluginDelete(
       const UINT  pos      // Position of the configuration
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.PluginDelete(
       uint        pos      // Position of the configuration
       )

Python
    
    
    AdminAPI.PluginDelete(
       pos         # Position of the configuration
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can be deleted only from the applications that run on the main server. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) will be returned.
