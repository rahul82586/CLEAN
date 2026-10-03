[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Subscriptions](../Subscriptions.md) / SubscriptionCfgUpdateBatch

[Previous](SubscriptionCfgUpdate.md) | [Next](SubscriptionCfgDelete.md)

# IMTAdminAPI::SubscriptionCfgUpdateBatch

Add or edit multiple subscription configurations.

C++
    
    
    MTAPIRES  IMTAdminAPI::SubscriptionCfgUpdateBatch(
       IMTConSubscription**  configs,      // Array of settings
       const UINT            config_total, // Number of settings in the array
       MTAPIRES*             results       // Array of results
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.SubscriptionCfgUpdateBatch(
       CIMTConSubscription[] configs,      // Array of settings
       MTRetCode[]           results       // Array of results
       )

### Parameters

**configs**  
[in] A pointer to an array of configurations which you want to add/edit.

**config_total**  
[in] The number of configurations in the 'configs' array.

**results**  
[out] An array with the results of each configuration applying on the server.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned. The [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code is an indication of successful change sending to a server; the results of applying the changes are passed in the 'results' parameter.

### Note

A configuration can only be added or updated from the applications running on the main server. For all other applications, the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) is returned.
