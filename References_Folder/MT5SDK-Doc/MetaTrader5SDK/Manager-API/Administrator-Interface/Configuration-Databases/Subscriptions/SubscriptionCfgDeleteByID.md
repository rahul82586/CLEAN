[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Subscriptions](../Subscriptions.md) / SubscriptionCfgDeleteByID

[Previous](SubscriptionCfgDelete.md) | [Next](SubscriptionCfgDeleteBatch.md)

# IMTAdminAPI::SubscriptionCfgDeleteByID

Delete a subscription configuration by internal ID.

C++
    
    
    MTAPIRES  IMTAdminAPI::SubscriptionCfgDeleteByID(
       const UINT64  id   // Configuration ID
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.SubscriptionCfgDeleteByID(
       ulong         id   // Configuration ID
       )

### Parameters

**id**  
[in] Configuration ID. TheIMTConSubscription::IDvalue is used for the identifier.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can only be deleted from the applications that run on the main server. For all other plugins, the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) is returned.
