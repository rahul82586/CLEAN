[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Managers](../Managers.md) / ManagerUpdate

[Previous](ManagerUnsubscribe.md) | [Next](ManagerUpdateBatch.md)

# IMTAdminAPI::ManagerUpdate

Adds or updates a manager configuration.

C++
    
    
    MTAPIRES  IMTAdminAPI::ManagerUpdate(
       IMTConManager*  manager      // An object of manager configuration
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.ManagerUpdate(
       CIMTConManager  manager      // An object of manager configuration
       )

Python
    
    
    AdminAPI.ManagerUpdate(
       manager         # An object of manager configuration
       )

### Parameters

**manager**  
[in] An object of manager configuration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/API.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can be added or updated only from the applications that run on the main server. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned.
