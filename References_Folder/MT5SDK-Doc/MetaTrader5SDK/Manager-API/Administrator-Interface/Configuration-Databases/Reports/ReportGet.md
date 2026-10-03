[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Reports](../Reports.md) / ReportGet

[Previous](ReportNext.md) | [Next](ReportModuleTotal.md)

# IMTAdminAPI::ReportGet

Get a report configuration by the name.

C++
    
    
    MTAPIRES  IMTAdminAPI::ReportGet(
       const UINT64   server_id,     // Server ID
       LPCWSTR        name,          // Report configuration name
       IMTConReport*  report         // An object of report configuration
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.ReportGet(
       ulong          server_id,     // Server ID
       string         name,          // Report configuration name
       CIMTConReport  report         // An object of report configuration
       )

Python
    
    
    AdminAPI.ReportGet(
       server_id,     # Server ID
       name           # Report configuration name
       )

### Parameters

**server_id**  
[in] The identifier of the server for which we get the report configuration. TheIMTConServer::Idvalue is used as the identifier.

**name**  
[in] Name of the report configuration. TheIMTConReport::Namevalue is used as the name..

**report**  
[out] An object of report configuration. The object must first be created using theIMTAdminAPI::ReportCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies parameters of the specified report configuration to the report object.
