[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Subscriptions](../Subscriptions.md) / SubscriptionCfgRequest

[Previous](SubscriptionCfgGetByID.md) | [Next](SubscriptionCfgRequestByID.md)

# IMTManagerAPI::SubscriptionCfgRequest

Request a subscription configuration from the server by its name.

C++
    
    
    MTAPIRES  IMTManagerAPI::SubscriptionCfgRequest(
       LPCWSTR              name,     // Configuration name
       IMTConSubscription*  config    // Subscription configuration object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SubscriptionCfgRequest(
       string               name,     // Configuration name
       CIMTConSubscription  config    // Subscription configuration object
       )

### Parameters

**name**  
[in] Configuration name. TheIMTConSubscription::Namevalue is used for the configuration name.

**config**  
[out] Subscription configuration object. The 'config' object must be previously created using theIMTManagerAPI::SubscriptionCfgCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
