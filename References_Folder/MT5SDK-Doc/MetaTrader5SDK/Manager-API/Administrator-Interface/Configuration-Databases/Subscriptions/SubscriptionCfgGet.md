[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Subscriptions](../Subscriptions.md) / SubscriptionCfgGet

[Previous](SubscriptionCfgNext.md) | [Next](SubscriptionCfgGetByID.md)

# IMTAdminAPI::SubscriptionCfgGet

Get a subscription configuration by name.

C++
    
    
    MTAPIRES  IMTAdminAPI::SubscriptionCfgGet(
       LPCWSTR              name,     // Configuration name
       IMTConSubscription*  config    // Subscription configuration object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.SubscriptionCfgGet(
       string               name,     // Configuration name
       CIMTConSubscription  config    // Subscription configuration object
       )

### Parameters

**name**  
[in] Configuration name. TheIMTConSubscription::Namevalue is used for the configuration name.

**config**  
[out] Subscription configuration object. The 'config' object must be previously created using theIMTAdminAPI::SubscriptionCfgCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
