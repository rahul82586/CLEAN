[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Reports](../Reports.md) / ReportCurrent

[Previous](ReportCreate.md) | [Next](../Common.md)

# IMTReportAPI::ReportCurrent

Get the configuration of the report that is currently being generated.
    
    
    MTAPIRES  IMTReportAPI::ReportCurrent(
       IMTConReport*  report      // An object of report configuration
       )

### Parameters

**report**  
[out] An object of report configuration. The report object must be first created using theIMTReportAPI::ReportCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
