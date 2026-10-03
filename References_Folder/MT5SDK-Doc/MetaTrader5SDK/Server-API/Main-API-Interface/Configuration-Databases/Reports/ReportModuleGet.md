[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Reports](../Reports.md) / ReportModuleGet

[Previous](ReportModuleNext.md) | [Next](../Mail-Servers.md)

# IMTServerAPI::ReportModuleGet

Get a report module configuration by the name.
    
    
    MTAPIRES  IMTServerAPI::ReportModuleGet(
       LPCWSTR              name,       // The name of the report module
       IMTConReportModule*  module      // An object of the report module configuration
       )

### Parameters

**name**  
[in] The name of a report module.

**module**  
[out] The report module configuration object. The module object must be first created using theIMTServerAPI::ReportModuleCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The module object must be first created using the [IMTConReportModule::Module](../../../../Configuration-Interfaces/Reports/IMTConReportModule/Module.md) method.

# IMTServerAPI::ReportModuleGet

Get a report module configuration by the name considering the server.
    
    
    MTAPIRES  IMTServerAPI::ReportModuleGet(
       UINT64               server,     // Server ID
       LPCWSTR              name,       // The name of the report module
       IMTConReportModule*  module      // An object of the report module configuration
       )

### Parameters

**server**  
[in] Identifier of the server the report module configuration is created for.

**name**  
[in] The name of a report module.

**module**  
[out] The report module configuration object. The module object must be first created using theIMTServerAPI::ReportModuleCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The module object must be first created using the [IMTConReportModule::Module](../../../../Configuration-Interfaces/Reports/IMTConReportModule/Module.md) method.
