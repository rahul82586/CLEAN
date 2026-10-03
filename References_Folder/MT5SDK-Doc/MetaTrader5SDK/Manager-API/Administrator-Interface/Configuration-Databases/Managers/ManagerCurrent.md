[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Managers](../Managers.md) / ManagerCurrent

[Previous](ManagerGet.md) | [Next](../History-Synchronization.md)

# IMTAdminAPI::ManagerCurrent

Get the configuration of the current manager account.

C++
    
    
    MTAPIRES  IMTAdminAPI::ManagerCurrent(
       IMTConManager*  manager      // Manager configuration object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.ManagerCurrent(
       CIMTConManager  manager      // Manager configuration object
       )

Python
    
    
    AdminAPI.ManagerCurrent(
       manager         # Manager configuration object
       )

### Parameters

**manager**  
[out] An object of manager configuration. The 'manager' object must be previously created using theIMTAdminAPI::ManagerCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method returns the description of the manager account using which the Manager API application is currently [connected ](../../Connection-to-the-Server/Connect.md) to the server.
