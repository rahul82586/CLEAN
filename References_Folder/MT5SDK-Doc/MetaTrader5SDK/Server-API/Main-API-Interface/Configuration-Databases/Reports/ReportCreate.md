[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Reports](../Reports.md) / ReportCreate

[Previous](../Reports.md) | [Next](ReportModuleCreate.md)

# IMTServerAPI::ReportCreate

Create an object of the configuration of reports.
    
    
    IMTConReport*  IMTServerAPI::ReportCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConReport](../../../../Configuration-Interfaces/Reports/IMTConReport.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTConReport::Release](../../../../Configuration-Interfaces/Reports/IMTConReport/Release.md) method of this object.
