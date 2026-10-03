[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / NetServerUpdate

[Previous](NetServerRestart.md) | [Next](NetServerUpdateBatch.md)

# IMTAdminAPI::NetServerUpdate

Add and update a server configuration.

C++
    
    
    MTAPIRES  IMTAdminAPI::NetServerUpdate(
       IMTConServer*  config      // Server configuration object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.NetServerUpdate(
       CIMTConServer  config      // Server configuration object
       )

Python
    
    
    AdminAPI.NetServerUpdate(
       server         # Server configuration object
       )

### Parameters

**config**  
[in] The server configuration object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can be added or updated only from the applications that run on the main server. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned.
