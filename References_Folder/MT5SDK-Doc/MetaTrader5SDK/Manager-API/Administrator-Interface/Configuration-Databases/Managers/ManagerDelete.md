[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Managers](../Managers.md) / ManagerDelete

[Previous](ManagerUpdateBatch.md) | [Next](ManagerDeleteBatch.md)

# IMTAdminAPI::ManagerDelete

Deletes a manager configuration by the index.

C++
    
    
    MTAPIRES  IMTAdminAPI::ManagerDelete(
       const UINT  pos      // Position of the configuration
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.ManagerDelete(
       uint        pos      // Position of the configuration
       )

Python
    
    
    AdminAPI.ManagerDelete(
       pos         # Position of the configuration
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can be deleted only from the applications that run on the main server. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) will be returned.
