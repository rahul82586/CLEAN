[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Reports](../Reports.md) / ReportModuleCreate

[Previous](ReportCreate.md) | [Next](ReportParamCreate.md)

# IMTAdminAPI::ReportModuleCreate

Create an object of configuration of a report module.

C++
    
    
    IMTConReportModule*  IMTAdminAPI::ReportModuleCreate()

.NET
    
    
    CIMTConReportModule  CIMTAdminAPI.ReportModuleCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConReportModule](../../../../Configuration-Interfaces/Reports/IMTConReportModule.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTConReportModule::Release](../../../../Configuration-Interfaces/Reports/IMTConReportModule/Release.md) method of this object.
