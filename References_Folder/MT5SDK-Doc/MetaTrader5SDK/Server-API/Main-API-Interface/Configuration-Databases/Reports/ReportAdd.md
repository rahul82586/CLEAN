[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Reports](../Reports.md) / ReportAdd

[Previous](ReportUnsubscribe.md) | [Next](ReportDelete.md)

# IMTServerAPI::ReportAdd

Add or update a report configuration.
    
    
    MTAPIRES  IMTServerAPI::ReportAdd(
       IMTConReport*  report      // An object of report configuration
       )

### Parameters

**report**  
[in] An object of report configuration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

When calling the method, a check is made whether the entry already exists. If the entry already exists, it is updated, otherwise a new entry is added. A key field for comparison is the name of the configuration [IMTConReport::Name()](../../../../Configuration-Interfaces/Reports/IMTConReport/Name.md). When you try to add a completely identical record, no changes are made, and therefore the [IMTConReportSink::OnReportUpdate](../../../../Configuration-Interfaces/Reports/IMTConReportSink/OnReportUpdate.md) notification method is not called.
