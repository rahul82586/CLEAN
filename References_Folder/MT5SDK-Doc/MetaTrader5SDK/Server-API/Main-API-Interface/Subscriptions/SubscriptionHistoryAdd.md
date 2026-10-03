[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionHistoryAdd

[Previous](SubscriptionHistoryUnsubscribe.md) | [Next](SubscriptionHistoryUpdate.md)

# IMTServerAPI::SubscriptionHistoryAdd

Add a user subscription action to the server database.
    
    
    MTAPIRES  IMTServerAPI::SubscriptionHistoryAdd(
       IMTSubscriptionHistory*         record        // Action description
       )

### Parameters

**record**  
[in]Subscription action description. The key field for finding an exiting record isIMTSubscriptionHistory::ID.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned. For example, if the specified subscription does not exist, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) will be returned.
