[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / NetServerDelete

[Previous](NetServerUpdateBatch.md) | [Next](NetServerDeleteBatch.md)

# IMTAdminAPI::NetServerDelete

Delete a server configuration by the index.

C++
    
    
    MTAPIRES  IMTAdminAPI::NetServerDelete(
       const UINT  pos      // Position of the configuration
       )

.NET
    
    
    MTRetCodes  CIMTAdminAPI.NetServerDelete(
       uint        pos      // Position of the configuration
       )

Python
    
    
    AdminAPI.NetServerDelete(
       pos         # Position of the configuration
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can be deleted only from the applications that run on the main server. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) will be returned.
