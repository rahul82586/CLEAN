[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionUnsubscribe

[Previous](SubscriptionSubscribe.md) | [Next](SubscriptionJoin.md)

# IMTServerAPI::SubscriptionUnsubscribe

Unsubscribe from events and hooks associated with changes in the subscriptions database.
    
    
    MTAPIRES  IMTServerAPI::SubscriptionUnsubscribe(
       IMTSubscriptionSink*  sink      // A pointer to the IMTSubscriptionSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTSubscriptionSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTServerAPI::SubscriptionSubscribe](SubscriptionSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) error is returned.
