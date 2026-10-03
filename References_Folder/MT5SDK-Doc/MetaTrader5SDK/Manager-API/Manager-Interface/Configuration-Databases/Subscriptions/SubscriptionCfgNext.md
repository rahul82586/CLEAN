[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Subscriptions](../Subscriptions.md) / SubscriptionCfgNext

[Previous](SubscriptionCfgTotal.md) | [Next](SubscriptionCfgGet.md)

# IMTManagerAPI::SubscriptionCfgNext

Get a subscription configuration by index.

C++
    
    
    MTAPIRES  IMTManagerAPI::SubscriptionCfgNext(
       const UINT           pos,      // Configuration position
       IMTConSubscription*  config    // Subscription configuration object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SubscriptionCfgNext(
       uint                 pos,      // Configuration position
       CIMTConSubscription  config    // Subscription configuration object
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**config**  
[out] Subscription configuration object. The 'config' object must be previously created using theIMTManagerAPI::SubscriptionCfgCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the subscription configuration with a specified index to the 'config' object.
