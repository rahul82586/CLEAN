[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Reports](../Reports.md) / ReportCreate

[Previous](../Reports.md) | [Next](ReportCurrent.md)

# IMTReportAPI::ReportCreate

Create an object of the configuration of reports.
    
    
    virtual IMTConReport*  IMTReportAPI::ReportCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConReport](../../../../Configuration-Interfaces/Reports/IMTConReport.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTConReport::Release](../../../../Configuration-Interfaces/Reports/IMTConReport/Release.md) method of this object.
