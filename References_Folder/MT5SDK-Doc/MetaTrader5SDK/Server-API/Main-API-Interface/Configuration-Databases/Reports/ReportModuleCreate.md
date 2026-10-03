[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Reports](../Reports.md) / ReportModuleCreate

[Previous](ReportCreate.md) | [Next](ReportParamCreate.md)

# IMTServerAPI::ReportModuleCreate

Create an object of configuration of a report module.
    
    
    IMTConReportModule*  IMTServerAPI::ReportModuleCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConReportModule](../../../../Configuration-Interfaces/Reports/IMTConReportModule.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTConReportModule::Release](../../../../Configuration-Interfaces/Reports/IMTConReportModule/Release.md) method of this object.
