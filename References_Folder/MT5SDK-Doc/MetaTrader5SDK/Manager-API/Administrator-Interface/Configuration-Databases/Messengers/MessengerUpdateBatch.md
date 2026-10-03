[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Messengers](../Messengers.md) / MessengerUpdateBatch

[Previous](MessengerUpdate.md) | [Next](MessengerDelete.md)

# IMTAdminAPI::MessengerUpdateBatch

Add or edit multiple messenger configurations.

C++
    
    
    MTAPIRES  IMTAdminAPI::MessengerUpdateBatch(
       IMTConMessenger**  configs,      // Array of configurations
       const UINT         config_total, // Number of configurations in the array
       MTAPIRES*          results       // Array of results
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.MessengerUpdateBatch(
       CIMTConMessenger[] configs,      // Array of configurations
       MTRetCode[]        results       // Array of results
       )

Python
    
    
    AdminAPI.MessengerUpdateBatch(
       configs            # Array of configurations
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
