[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Reports](../Reports.md) / ReportCreate

[Previous](../Reports.md) | [Next](ReportModuleCreate.md)

# IMTAdminAPI::ReportCreate

Create an object of the configuration of reports.

C++
    
    
    IMTConReport*  IMTAdminAPI::ReportCreate()

.NET
    
    
    CIMTConReport  CIMTAdminAPI.ReportCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConReport](../../../../Configuration-Interfaces/Reports/IMTConReport.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTConReport::Release](../../../../Configuration-Interfaces/Reports/IMTConReport/Release.md) method of this object.
