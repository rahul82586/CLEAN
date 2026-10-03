[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Reports](../Reports.md) / ReportNext

[Previous](ReportTotal.md) | [Next](ReportGet.md)

# IMTAdminAPI::ReportNext

Get a report configuration by the index.

C++
    
    
    MTAPIRES  IMTAdminAPI::ReportNext(
       const UINT     pos,        // Position of the configuration
       IMTConReport*  report      // An object of report configuration
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.ReportNext(
       uint           pos,        // Position of the configuration
       CIMTConReport  report      // An object of report configuration
       )

Python
    
    
    AdminAPI.ReportNext(
       pos,           # Position of the configuration
       report         # An object of report configuration
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**report**  
[out] An object of report configuration. The report object must be first created using theIMTAdminAPI::ReportCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the configuration data of a report with a specified index to the report object.
