[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionSubscribe

[Previous](SubscriptionCreateArray.md) | [Next](SubscriptionUnsubscribe.md)

# IMTServerAPI::SubscriptionSubscribe

Subscribe to events and hooks associated with changes in the subscriptions database.
    
    
    MTAPIRES  IMTServerAPI::SubscriptionSubscribe(
       IMTSubscriptionSink*  sink      // A pointer to the IMTSubscriptionSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTSubscriptionSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.

### Note

Subscribing to events is thread safe. The same [IMTSubscriptionSink](../../../Database-Interfaces/Subscriptions/IMTSubscriptionSink.md) interface cannot subscribe to an event twice. The [MT_RET_ERR_DUPLICATE](../../../Return-Codes/Common-errors.md) response code is returned in this case.
