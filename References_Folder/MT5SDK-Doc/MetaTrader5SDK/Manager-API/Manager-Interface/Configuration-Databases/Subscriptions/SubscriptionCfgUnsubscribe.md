[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Subscriptions](../Subscriptions.md) / SubscriptionCfgUnsubscribe

[Previous](SubscriptionCfgSubscribe.md) | [Next](SubscriptionCfgTotal.md)

# IMTManagerAPI::SubscriptionCfgUnsubscribe

Unsubscribe from events and hooks associated with subscription configurations.

C++
    
    
    MTAPIRES  IMTManagerAPI::SubscriptionCfgUnsubscribe(
       IMTConSubscriptionSink*  sink   // A pointer to the IMTConSubscriptionSink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SubscriptionCfgUnsubscribe(
       CIMTConSubscriptionSink  sink   // The IMTConSubscriptionSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConSubscriptionSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method is paired with [IMTManagerAPI::SubscriptionCfgSubscribe](SubscriptionCfgSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
