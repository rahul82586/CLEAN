[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Managers](../Managers.md) / ManagerAdd

[Previous](ManagerUnsubscribe.md) | [Next](ManagerDelete.md)

# IMTServerAPI::ManagerAdd

Adds or updates a manager configuration.
    
    
    MTAPIRES  IMTServerAPI::ManagerAdd(
       IMTConManager*  manager      // An object of manager configuration
       )

### Parameters

**manager**  
[in] An object of manager configuration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/API.md) response code. Otherwise, an error code will be returned.

### Note

When calling the method, a check is made whether the entry already exists. If the entry already exists, it is updated, otherwise a new entry is added. A key field for comparison is the login of a manager [IMTConManager::Login()](../../../../Configuration-Interfaces/Managers/IMTConManager/Login.md). When you try to add a completely identical record, no changes are made, and therefore the [IMTConManagerSink::OnManagerUpdate](../../../../Configuration-Interfaces/Managers/IMTConManagerSink/OnManagerUpdate.md) notification method is not called.
