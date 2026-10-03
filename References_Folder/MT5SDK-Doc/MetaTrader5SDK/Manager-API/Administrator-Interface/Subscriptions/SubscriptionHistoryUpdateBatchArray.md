[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionHistoryUpdateBatchArray

[Previous](SubscriptionHistoryUpdateBatch.md) | [Next](SubscriptionHistoryDelete.md)

# IMTAdminAPI::SubscriptionHistoryUpdateBatchArray

Bulk change of user subscription actions in the server database.

C++
    
    
    MTAPIRES  IMTAdminAPI::SubscriptionHistoryUpdateBatchArray(
       IMTSubscriptionHistory**   records,  // Array of actions
       MTAPIRES*                  results   // Array of results
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.SubscriptionHistoryUpdateBatchArray(
       CIMTSubscriptionHistory[]  records,  // Array of actions
       MTRetCode[]                res       // Array of results
       )

### Parameters

**records**  
[in] A pointer to an array ofsubscription actions. The key field for finding exiting records isIMTSubscriptionHistory::ID.

**results**  
[out] An array with action editing results. The size of the 'results' array must not be less than that of 'records'.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code means that all specified actions have been updated. The [MT_RET_ERR_PARTIAL](../../../Return-Codes/Common-errors.md) response code means that only some of the actions have been updated. Analyze the 'results' array for a detailed information on execution results. The result of update of each subscription action from the 'records' array is added to 'results'. The index of a result corresponds to the index of a subscription in the source array.

### Note

An action can only be edited from the applications connected to the trade server, on which the action has been created. For all other applications, the response code [MT_RET_ERR_NOTMAIN](../../../Return-Codes/API.md) is returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) is returned.
