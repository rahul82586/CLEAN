[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Managers](../Managers.md) / ManagerAccessCreate

[Previous](ManagerCreate.md) | [Next](ManagerReportCreate.md)

# IMTReportAPI::ManagerAccessCreate

Create an object of configuration of an access list by IP addresses for a manager.
    
    
    IMTConManagerAccess*  IMTReportAPI::ManagerAccessCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConManagerAccess](../../../../Configuration-Interfaces/Managers/IMTConManagerAccess.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTConManagerAccess::Release](../../../../Configuration-Interfaces/Managers/IMTConManagerAccess/Release.md) method of this object.
