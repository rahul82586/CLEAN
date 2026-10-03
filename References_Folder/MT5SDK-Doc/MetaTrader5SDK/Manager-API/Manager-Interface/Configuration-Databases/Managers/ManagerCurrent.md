[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Managers](../Managers.md) / ManagerCurrent

[Previous](ManagerReportCreate.md) | [Next](../Subscriptions.md)

# IMTManagerAPI::ManagerCurrent

Get the configuration of the current manager account.

C++
    
    
    MTAPIRES  IMTManagerAPI::ManagerCurrent(
       IMTConManager*  manager      // Manager configuration object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.ManagerCurrent(
       CIMTConManager  manager      // Manager configuration object
       )

Python
    
    
    ManagerAPI.ManagerCurrent()

### Parameters

**manager**  
[out] An object of manager configuration. The 'manager' object must be previously created using theIMTManagerAPI::ManagerCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method returns the description of the manager account using which the Manager API application is currently [connected ](../../../Administrator-Interface/Connection-to-the-Server/Connect.md) to the server.
