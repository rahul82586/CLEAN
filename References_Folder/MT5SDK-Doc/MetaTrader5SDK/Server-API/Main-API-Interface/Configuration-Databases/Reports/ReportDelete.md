[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Reports](../Reports.md) / ReportDelete

[Previous](ReportAdd.md) | [Next](ReportShift.md)

# IMTServerAPI::ReportDelete

Delete a report configuration by the name.
    
    
    MTAPIRES  IMTServerAPI::ReportDelete(
       LPCWSTR  name      // Name of the configuration
       )

### Parameters

**name**  
[in] The name of the configuration to delete.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can be deleted only from the plugins that run on the main server. For all other plugins the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) will be returned.

# IMTServerAPI::ReportDelete

Delete a report configuration by the name considering the server.
    
    
    MTAPIRES  IMTServerAPI::ReportDelete(
       UINT64   server,   // Server ID
       LPCWSTR  name      // Name of the configuration
       )

### Parameters

**server**  
[in] Identifier of the server the report configuration is created for.

**name**  
[in] The name of the configuration to delete.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can be deleted only from the plugins that run on the main server. For all other plugins the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) will be returned.

# IMTServerAPI::ReportDelete

Delete a report configuration by the index.
    
    
    virtual MTAPIRES  ReportDelete(
       const UINT  pos      // Position of the configuration
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can be deleted only from the plugins that run on the main server. For all other plugins the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) will be returned.
