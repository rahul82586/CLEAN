[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Subscriptions](../Subscriptions.md) / SubscriptionCfgSubscribe

[Previous](SubscriptionCfgNewsCreate.md) | [Next](SubscriptionCfgUnsubscribe.md)

# IMTAdminAPI::SubscriptionCfgSubscribe

Subscribe to events and hooks associated with subscription configurations.

C++
    
    
    MTAPIRES  IMTAdminAPI::SubscriptionCfgSubscribe(
       IMTConSubscriptionSink*  sink   // A pointer to the IMTConSubscriptionSink object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.SubscriptionCfgSubscribe(
       CIMTConSubscriptionSink  sink   // The IMTConSubscriptionSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConSubscriptionSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.

### Note

Subscribing to events is thread safe. The same [IMTConSubscriptionSink](../../../../Configuration-Interfaces/Subscriptions/IMTConSubscriptionSink.md) interface cannot subscribe to an event twice. The [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) response code is returned in this case.
