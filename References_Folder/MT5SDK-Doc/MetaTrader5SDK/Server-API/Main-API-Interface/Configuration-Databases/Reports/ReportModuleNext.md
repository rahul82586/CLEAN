[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Reports](../Reports.md) / ReportModuleNext

[Previous](ReportModuleTotal.md) | [Next](ReportModuleGet.md)

# IMTServerAPI::ReportModuleNext

Get a report module by the index.
    
    
    MTAPIRES  IMTServerAPI::ReportModuleNext(
       const UINT           pos,        // Position of the configuration
       IMTConReportModule*  module      // An object of the report module configuration
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**module**  
[out] The report module configuration object. The module object must be first created using theIMTServerAPI::ReportModuleCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies a report configuration with a specified index to the module object.
