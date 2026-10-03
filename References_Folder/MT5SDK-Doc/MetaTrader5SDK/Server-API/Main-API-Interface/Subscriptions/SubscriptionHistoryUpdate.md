[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionHistoryUpdate

[Previous](SubscriptionHistoryAdd.md) | [Next](SubscriptionHistoryDelete.md)

# IMTServerAPI::SubscriptionHistoryUpdate

Edit a user subscription action in the server database.
    
    
    MTAPIRES  IMTServerAPI::SubscriptionHistoryUpdate(
       IMTSubscriptionHistory*         record        // Action description
       )

### Parameters

**record**  
[in]Subscription action description. The key field for finding an exiting record isIMTSubscriptionHistory::ID.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned. For example, if the specified subscription does not exist, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) will be returned.

### Note

An action can only be edited from the plugins running on the same trade server where the action was created. For all other applications, the response code [MT_RET_ERR_NOTMAIN](../../../Return-Codes/API.md) is returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) is returned.
