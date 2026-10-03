[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionHistorySubscribe

[Previous](SubscriptionHistoryCreateArray.md) | [Next](SubscriptionHistoryUnsubscribe.md)

# IMTServerAPI::SubscriptionHistorySubscribe

Subscribe to events and hooks associated with changes in the database of subscription actions.
    
    
    MTAPIRES  IMTServerAPI::SubscriptionHistorySubscribe(
       IMTSubscriptionHistorySink*  sink      // A pointer to the IMTSubscriptionHistorySink object
       )

### Parameters

**sink**  
[in] A pointer to the object implementing theIMTSubscriptionHistorySinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. The same [IMTSubscriptionHistorySink](../../../Database-Interfaces/Subscriptions/IMTSubscriptionHistorySink.md) interface cannot subscribe to an event twice. The [MT_RET_ERR_DUPLICATE](../../../Return-Codes/Common-errors.md) response code is returned in this case.
