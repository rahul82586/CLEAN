[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Managers](../Managers.md) / ManagerCreate

[Previous](../Managers.md) | [Next](ManagerAccessCreate.md)

# IMTReportAPI::ManagerCreate

Create an object of manager configuration.
    
    
    IMTConManager*  IMTReportAPI::ManagerCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConManager](../../../../Configuration-Interfaces/Managers/IMTConManager.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTConManager::Release](../../../../Configuration-Interfaces/Managers/IMTConManager/Release.md) method of this object.
