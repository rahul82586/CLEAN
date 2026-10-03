[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Reports](../Reports.md) / ReportModuleGet

[Previous](ReportModuleNext.md) | [Next](../Mail-Servers.md)

# IMTAdminAPI::ReportModuleGet

Get a report module configuration by the name.

C++
    
    
    MTAPIRES  IMTAdminAPI::ReportModuleGet(
       const UINT64         server_id,     // Server ID
       LPCWSTR              name,          // The name of the report module
       IMTConReportModule*  module         // An object of the report module configuration
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.ReportModuleGet(
       ulong                server_id,     // Server ID
       string               name,          // The name of the report module
       CIMTConReportModule  module         // An object of the report module configuration
       )

Python
    
    
    AdminAPI.ReportModuleGet(
       server_id,           # Server ID
       name                 # The name of the report module
       )

### Parameters

**server_id**  
[in] The identifier of the server for which we get the report module configuration. TheIMTConServer::Idvalue is used as the identifier.

**name**  
[in] The name of a report module.

**module**  
[out] The report module configuration object. The module object must be first created using theIMTAdminAPI::ReportModuleCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConReportModule::Module()](../../../../Configuration-Interfaces/Reports/IMTConReportModule/Module.md) value is used as the name.
