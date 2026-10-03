[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionHistoryUnsubscribe

[Previous](SubscriptionHistorySubscribe.md) | [Next](SubscriptionHistoryAdd.md)

# IMTServerAPI::SubscriptionHistoryUnsubscribe

Unsubscribe from events and hooks associated with changes in the database of subscription actions.
    
    
    MTAPIRES  IMTServerAPI::SubscriptionHistoryUnsubscribe(
       IMTSubscriptionHistorySink*  sink      // A pointer to the IMTSubscriptionHistorySink object
       )

### Parameters

**sink**  
[in] A pointer to the object implementing theIMTSubscriptionHistorySinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTServerAPI::SubscriptionHistorySubscribe](SubscriptionHistorySubscribe.md). If an attempt is made to unsubscribe from the interface that has not been previously subscribed to, the [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) error is returned.
