[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Subscriptions](../Subscriptions.md) / SubscriptionCfgGetByID

[Previous](SubscriptionCfgGet.md) | [Next](../../Clients.md)

# IMTAdminAPI::SubscriptionCfgGetByID

Get a subscription configuration by ID.

C++
    
    
    MTAPIRES  IMTAdminAPI::SubscriptionCfgGetByID(
       const UINT64         id,       // Configuration ID
       IMTConSubscription*  config    // Subscription configuration object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.SubscriptionCfgGetByID(
       uint                 id,       // Configuration ID
       CIMTConSubscription  config    // Subscription configuration object
       )

### Parameters

**id**  
[in] Configuration ID. TheIMTConSubscription::IDvalue is used for the identifier.

**config**  
[out] Subscription configuration object. The 'config' object must be previously created using theIMTAdminAPI::SubscriptionCfgCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
