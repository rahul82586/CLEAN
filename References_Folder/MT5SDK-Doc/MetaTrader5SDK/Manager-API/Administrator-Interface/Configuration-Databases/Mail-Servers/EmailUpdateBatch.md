[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Mail Servers](../Mail-Servers.md) / EmailUpdateBatch

[Previous](EmailUpdate.md) | [Next](EmailDelete.md)

# IMTAdminAPI::EmailUpdateBatch

Add or edit multiple mail server configurations.

C++
    
    
    MTAPIRES  IMTAdminAPI::EmailUpdateBatch(
       IMTConEmail**   configs,      // Array of configurations
       const UINT      config_total, // Number of configuration in the array
       MTAPIRES*       results       // Array of results
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.EmailUpdateBatch(
       CIMTConEmail[]  configs,      // Array of settings
       MTRetCode[]     results       // Array of results
       )

Python
    
    
    AdminAPI.EmailUpdateBatch(
       configs         // Array of settings
       )

### Parameters

**configs**  
[in] A pointer to an array of configurations which you want to add/update.

**config_total**  
[in] The number of configurations in the 'configs' array.

**results**  
[out] An array with the results of each configuration applying on the server.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned. The [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code is an indication of successful change sending to a server; change applying results are passed in the 'results' parameter.

### Note

A configuration can only be added or updated from the applications running on the main server. For all other applications, the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) is returned.
