[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionHistoryDeleteBatch

[Previous](SubscriptionHistoryDelete.md) | [Next](SubscriptionHistoryRequest.md)

# IMTManagerAPI::SubscriptionHistoryDeleteBatch

Delete a batch of user subscription actions from the server database.
    
    
    MTAPIRES  IMTManagerAPI::SubscriptionHistoryDeleteBatch(
       const UINT64*   ids,           // Array of IDs
       const UINT      ids_total,     // The number of IDs in the array
       MTAPIRES*       results        // Array of results
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SubscriptionHistoryDeleteBatch(
       ulong[]         ids,           // Array of IDs
       MTRetCode[]     retcodes       // Array of results
       )

### Parameters

**ids**  
[in] A pointer to an array of IDs of subscription actions which you want to delete. TheIMTSubscriptionHistory::IDvalue is used for the identifier.

**ids_total**  
[in] The number of identifiers in the 'ids' array.

**results**  
[out] An array with action deletion results. The size of the 'results' array must not be less than that of 'ids'.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates that all actions have been deleted. The [MT_RET_ERR_PARTIAL](../../../Return-Codes/Common-errors.md) response code means that only some of the actions have been deleted. Analyze the 'results' array for a detailed information on execution results. The result of deletion of each action from the 'ids' array is added to 'results'. The result index corresponds to the action index in the source array.

### Note

An action can only be deleted from the applications connected to the trade server, on which the action has been created. For all other applications, the response code [MT_RET_ERR_NOTMAIN](../../../Return-Codes/API.md) is returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) is returned.
