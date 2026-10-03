[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Reports](../Reports.md) / ReportUpdateBatch

[Previous](ReportUpdate.md) | [Next](ReportDelete.md)

# IMTAdminAPI::ReportUpdateBatch

Add or edit multiple report configurations.

C++
    
    
    MTAPIRES  IMTAdminAPI::ReportUpdateBatch(
       IMTConReport**  configs,      // An array of configurations
       const UINT      config_total, // The number of configurations in the array
       MTAPIRES*       results       // An array of results
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.ReportUpdateBatch(
       CIMTConReport[] configs,      // An array of configurations
       MTRetCode[]     results       // An array of results
       )

Python
    
    
    AdminAPI.ReportUpdateBatch(
       configs         # An array of configurations
       )

### Parameters

**configs**  
[in] A pointer to an array of configurations which you want to add/update.

**config_total**  
[in] The number of configurations in the 'configs' array.

**results**  
[out] An array with the results of applying of each configuration change on the server.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned. The [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code is an indication of successful sending of changes to a server; results of applying the changes are passed in the 'results' parameter.

### Further Note

A configuration can only be added or updated from the applications that run on the main server. For all other applications, the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) is returned.
