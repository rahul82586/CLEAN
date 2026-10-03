[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Subscriptions](../Subscriptions.md) / SubscriptionCfgRequestByID

[Previous](SubscriptionCfgRequest.md) | [Next](../../Selected-Symbols.md)

# IMTManagerAPI::SubscriptionCfgRequestByID

Request a subscription configuration from the server by its ID.

C++
    
    
    MTAPIRES  IMTManagerAPI::SubscriptionCfgRequestByID(
       const UINT64         id,       // Configuration ID
       IMTConSubscription*  config    // Subscription configuration object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SubscriptionCfgRequestByID(
       uint                 id,       // Configuration ID
       CIMTConSubscription  config    // Subscription configuration object
       )

### Parameters

**id**  
[in] Configuration ID. TheIMTConSubscription::IDvalue is used for the identifier.

**config**  
[out] Subscription configuration object. The 'config' object must be previously created using theIMTManagerAPI::SubscriptionCfgCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
