[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Managers](../Managers.md) / ManagerGet

[Previous](ManagerNext.md) | [Next](ManagerCurrent.md)

# IMTAdminAPI::ManagerGet

Gets a manager configuration with the specified login.

C++
    
    
    MTAPIRES  IMTAdminAPI::ManagerGet(
       const UINT64    login,       // Login of a manager
       IMTConManager*  manager      // An object of manager configuration
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.ManagerGet(
       ulong           login,       // Login of a manager
       CIMTConManager  manager      // An object of manager configuration
       )

Python
    
    
    AdminAPI.ManagerGet(
       login           # Login of a manager
       )

### Parameters

**login**  
[in] The login of a manager.

**manager**  
[out] An object of manager configuration. The manager object must be first created using theIMTAdminAPI::ManagerCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConManager::Login()](../../../../Configuration-Interfaces/Managers/IMTConManager/Login.md) value is used as the login.
