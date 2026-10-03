[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Managers](../Managers.md) / ManagerGet

[Previous](ManagerNext.md) | [Next](../Gateways.md)

# IMTReportAPI::ManagerGet

Gets a manager configuration with the specified login.
    
    
    MTAPIRES  IMTReportAPI::ManagerGet(
       const UINT64    login,       // Login of a manager
       IMTConManager*  manager      // An object of manager configuration
       )

### Parameters

**login**  
[in] The login of a manager.

**manager**  
[out] An object of manager configuration. The manager object must be first created using theIMTReportAPI::ManagerCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConManager::Login()](../../../../Configuration-Interfaces/Managers/IMTConManager/Login.md) value is used as the login.
