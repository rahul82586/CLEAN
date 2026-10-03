[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Subscriptions](../Subscriptions.md) / SubscriptionCfgUpdate

[Previous](SubscriptionCfgUnsubscribe.md) | [Next](SubscriptionCfgUpdateBatch.md)

# IMTAdminAPI::SubscriptionCfgUpdate

Add or update a subscription configuration.

C++
    
    
    MTAPIRES  IMTAdminAPI::SubscriptionCfgUpdate(
       IMTConSubscription*  config  // Subscription configuration object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.SubscriptionCfgUpdate(
       CIMTConSubscription  config  // Subscription configuration object
       )

### Parameters

**config**  
[in] Subscription configuration objectIMTConSubscription.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

When calling the method, a check is made whether the record already exists. If the record already exists, it is updated, otherwise a new entry is added. A key field for comparison is the configuration name [IMTConSubscription::Name()](../../../../Configuration-Interfaces/Subscriptions/IMTConSubscription/Name.md). When you try to add a completely identical record, no changes are made, and therefore the [IMTConSubscriptionSink::OnSubscriptionUpdate](../../../../Configuration-Interfaces/Subscriptions/IMTConSubscriptionSink/OnSubscriptionCfgUpdate.md) notification method is not called.
