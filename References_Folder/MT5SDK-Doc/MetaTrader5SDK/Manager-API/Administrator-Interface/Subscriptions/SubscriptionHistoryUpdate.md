[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionHistoryUpdate

[Previous](SubscriptionHistoryCreateArray.md) | [Next](SubscriptionHistoryUpdateBatch.md)

# IMTAdminAPI::SubscriptionHistoryUpdate

Edit a user subscription action in the server database.

C++
    
    
    MTAPIRES  IMTAdminAPI::SubscriptionHistoryUpdate(
       IMTSubscriptionHistory*         record        // Action description
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAdminAPI.SubscriptionHistoryUpdate(
       CIMTSubscriptionHistory         record        // Action description
       )

### Parameters

**record**  
[in]Subscription action description. The key field for finding an exiting record isIMTSubscriptionHistory::ID.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned. For example, if the specified subscription does not exist, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) will be returned.

### Note

An action can only be edited from the applications connected to the trade server, on which the action has been created. For all other applications, the response code [MT_RET_ERR_NOTMAIN](../../../Return-Codes/API.md) is returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) is returned.
