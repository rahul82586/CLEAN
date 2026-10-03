[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Managers](../Managers.md) / ManagerGet

[Previous](ManagerNext.md) | [Next](../History-Synchronization.md)

# IMTServerAPI::ManagerGet

Gets a manager configuration with the specified login.
    
    
    MTAPIRES  IMTServerAPI::ManagerGet(
       const UINT64    login,       // Login of a manager
       IMTConManager*  manager      // An object of manager configuration
       )

### Parameters

**login**  
[in] The login of a manager.

**manager**  
[out] An object of manager configuration. The manager object must be first created using theIMTServerAPI::ManagerCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConManager::Login()](../../../../Configuration-Interfaces/Managers/IMTConManager/Login.md) value is used as the login.
