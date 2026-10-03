[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Subscriptions](../Subscriptions.md) / SubscriptionCfgGetByID

[Previous](SubscriptionCfgGet.md) | [Next](../Floating-Margin.md)

# IMTServerAPI::SubscriptionCfgGetByID

Get a subscription configuration by ID.
    
    
    MTAPIRES  IMTServerAPI::SubscriptionCfgGetByID(
       const UINT64         id,       // Configuration ID
       IMTConSubscription*  config    // Subscription configuration object
       )

### Parameters

**id**  
[in] Configuration ID. TheIMTConSubscription::IDvalue is used for the identifier.

**config**  
[out] Subscription configuration object. The 'config' object must be previously created using theIMTServerAPI::SubscriptionCfgCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
