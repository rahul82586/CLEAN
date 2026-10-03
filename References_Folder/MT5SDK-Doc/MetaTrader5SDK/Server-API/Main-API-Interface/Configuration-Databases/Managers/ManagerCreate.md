[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Managers](../Managers.md) / ManagerCreate

[Previous](../Managers.md) | [Next](ManagerAccessCreate.md)

# IMTServerAPI::ManagerCreate

Create an object of manager configuration.
    
    
    IMTConManager*  IMTServerAPI::ManagerCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConManager](../../../../Configuration-Interfaces/Managers/IMTConManager.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTConManager::Release](../../../../Configuration-Interfaces/Managers/IMTConManager/Release.md) method of this object.
