[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Reports](../Reports.md) / ReportGet

[Previous](ReportNext.md) | [Next](ReportModuleTotal.md)

# IMTServerAPI::ReportGet

Get a report configuration by the name.
    
    
    MTAPIRES  IMTServerAPI::ReportGet(
       LPCWSTR        name,       // Name of the configuration
       IMTConReport*  report      // An object of report configuration
       )

### Parameters

**name**  
[in] The name of the configuration.

**report**  
[out] An object of report configuration. The report object must be first created using theIMTServerAPI::ReportCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConReport::Name](../../../../Configuration-Interfaces/Reports/IMTConReport/Name.md) value is used as the name.

# IMTServerAPI::ReportGet

Get a report configuration by the name considering the server.
    
    
    MTAPIRES  IMTServerAPI::ReportGet(
       UINT64         server,     // Server ID
       LPCWSTR        name,       // Name of the configuration
       IMTConReport*  report      // An object of report configuration
       )

### Parameters

**server**  
[in] Identifier of the server the report configuration is created for.

**name**  
[in] The name of the configuration.

**report**  
[out] An object of report configuration. The report object must be first created using theIMTServerAPI::ReportCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConReport::Name](../../../../Configuration-Interfaces/Reports/IMTConReport/Name.md) value is used as the name.
