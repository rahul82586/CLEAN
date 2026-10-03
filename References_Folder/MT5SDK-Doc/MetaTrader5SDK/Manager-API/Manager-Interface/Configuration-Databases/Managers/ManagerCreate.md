[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Managers](../Managers.md) / ManagerCreate

[Previous](../Managers.md) | [Next](ManagerAccessCreate.md)

# IMTManagerAPI::ManagerCreate

Create a manager configuration object.

C++
    
    
    IMTConManager*  IMTManagerAPI::ManagerCreate()

.NET
    
    
    CIMTConManager  CIMTManagerAPI.ManagerCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConManager](../../../../Configuration-Interfaces/Managers/IMTConManager.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTConManager::Release](../../../../Configuration-Interfaces/Managers/IMTConManager/Release.md) method of this object.
