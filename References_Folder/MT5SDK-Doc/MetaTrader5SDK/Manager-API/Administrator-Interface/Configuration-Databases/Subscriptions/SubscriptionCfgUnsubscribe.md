[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Subscriptions](../Subscriptions.md) / SubscriptionCfgUnsubscribe

[Previous](SubscriptionCfgSubscribe.md) | [Next](SubscriptionCfgUpdate.md)

# IMTAdminAPI::SubscriptionCfgUnsubscribe

Unsubscribe from events and hooks associated with subscription configurations.

C++
    
    
    MTAPIRES  IMTAdminAPI::SubscriptionCfgUnsubscribe(
       IMTConSubscriptionSink*  sink   // A pointer to the IMTConSubscriptionSink object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.SubscriptionCfgUnsubscribe(
       CIMTConSubscriptionSink  sink   // The IMTConSubscriptionSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConSubscriptionSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method is paired with [IMTAdminAPI::SubscriptionCfgSubscribe](SubscriptionCfgSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
