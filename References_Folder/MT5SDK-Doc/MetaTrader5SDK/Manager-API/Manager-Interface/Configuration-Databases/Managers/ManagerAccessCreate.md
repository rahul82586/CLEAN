[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Managers](../Managers.md) / ManagerAccessCreate

[Previous](ManagerCreate.md) | [Next](ManagerReportCreate.md)

# IMTManagerAPI::ManagerAccessCreate

Create an object of access list configuration by IP addresses for a manager.

C++
    
    
    IMTConManagerAccess*  IMTManagerAPI::ManagerAccessCreate()

.NET
    
    
    CIMTConManagerAccess  CIMTManagerAPI.ManagerAccessCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTConManagerAccess](../../../../Configuration-Interfaces/Managers/IMTConManagerAccess.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTConManagerAccess::Release](../../../../Configuration-Interfaces/Managers/IMTConManagerAccess/Release.md) method of this object.
