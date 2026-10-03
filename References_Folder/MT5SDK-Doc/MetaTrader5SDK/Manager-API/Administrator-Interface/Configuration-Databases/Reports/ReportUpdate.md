[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Reports](../Reports.md) / ReportUpdate

[Previous](ReportUnsubscribe.md) | [Next](ReportUpdateBatch.md)

# IMTAdminAPI::ReportUpdate

Add or update a report configuration.

C++
    
    
    MTAPIRES  IMTAdminAPI::ReportUpdate(
       IMTConReport*  report      // An object of report configuration
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.ReportUpdate(
       CIMTConReport  report      // An object of report configuration
       )

Python
    
    
    AdminAPI.ReportUpdate(
       report         # An object of report configuration
       )

### Parameters

**report**  
[in] An object of report configuration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can be added or updated only from the applications that run on the main server. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned.
