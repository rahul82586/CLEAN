[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Managers](../Managers.md) / ManagerReportCreate

[Previous](ManagerAccessCreate.md) | [Next](ManagerCurrent.md)

# IMTManagerAPI::ManagerReportCreate

Create an object for the manager's permission to access the report.

C++
    
    
    IMTConManagerReport*  IMTManagerAPI::ManagerReportCreate()

.NET
    
    
    CIMTConManagerReport  CIMTManagerAPI.ManagerReportCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTConManagerReport](../../../../Configuration-Interfaces/Managers/IMTConManagerReport.md) interface. In case of failure, NULL is returned.

### Note

The created object must be destroyed by calling the [IMTConManagerReport::Release](../../../../Configuration-Interfaces/Managers/IMTConManagerReport/Release.md) method of this object.
