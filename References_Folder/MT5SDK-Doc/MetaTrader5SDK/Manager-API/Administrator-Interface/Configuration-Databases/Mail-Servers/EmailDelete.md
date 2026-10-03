[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Mail Servers](../Mail-Servers.md) / EmailDelete

[Previous](EmailUpdateBatch.md) | [Next](EmailDeleteBatch.md)

# IMTAdminAPI::EmailDelete

Delete a mail server configuration by name.

C++
    
    
    MTAPIRES  IMTAdminAPI::EmailDelete(
       LPCWSTR  name      // Configuration name
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.EmailDelete(
       string   name      // Configuration name
       )

Python
    
    
    AdminAPI.EmailDelete(
       name     # Configuration name
       )

### Parameters

**name**  
[in] The name of the configuration to delete.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can only be deleted from the applications that run on the main server. For all other plugins the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) is returned.

# IMTAdminAPI::EmailDelete

Delete a mail server configuration by index.

C++
    
    
    MTAPIRES  IMTAdminAPI::EmailDelete(
       const UINT  pos      // Configuration position
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.EmailDelete(
       uint        pos      // Configuration index
       )

Python
    
    
    AdminAPI.EmailDelete(
       pos         # Configuration index
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can only be deleted from the applications that run on the main server. For all other plugins the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) is returned.
