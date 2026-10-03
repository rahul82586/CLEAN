[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / GroupDelete

[Previous](GroupUpdateBatch.md) | [Next](GroupDeleteBatch.md)

# IMTAdminAPI::GroupDelete

Delete a group configuration by the name.

C++
    
    
    MTAPIRES  IMTAdminAPI::GroupDelete(
       LPCWSTR  name      // Name of the configuration
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.GroupDelete(
       string   name      // Name of the configuration
       )

Python
    
    
    AdminAPI.GroupDelete(
       name     # Name of the configuration
       )

### Parameters

**name**  
[in] The name of the configuration to delete.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can be deleted only from the applications that run on the main server. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) will be returned.

# IMTAdminAPI::GroupDelete

Deletes a group configuration by the index.

C++
    
    
    MTAPIRES  IMTAdminAPI::GroupDelete(
       const UINT  pos      // Position of the configuration
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.GroupDelete(
       uint        pos      // Position of the configuration
       )

Python
    
    
    AdminAPI.GroupDelete(
       pos         # Position of the configuration
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can be deleted only from the applications that run on the main server. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) will be returned.
