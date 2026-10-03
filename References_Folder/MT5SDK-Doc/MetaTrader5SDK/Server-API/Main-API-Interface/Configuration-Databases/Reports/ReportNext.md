[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Reports](../Reports.md) / ReportNext

[Previous](ReportTotal.md) | [Next](ReportGet.md)

# IMTServerAPI::ReportNext

Get a report configuration by the index.
    
    
    MTAPIRES  IMTServerAPI::ReportNext(
       const UINT     pos,        // Position of the configuration
       IMTConReport*  report      // An object of report configuration
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**report**  
[out] An object of report configuration. The report object must be first created using theIMTServerAPI::ReportCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the configuration data of a report with a specified index to the report object.
