[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionDeleteBatch

[Previous](SubscriptionDelete.md) | [Next](SubscriptionRequest.md)

# IMTManagerAPI::SubscriptionDeleteBatch

Delete a user subscription from the server database.
    
    
    MTAPIRES  IMTManagerAPI::SubscriptionDeleteBatch(
       const UINT64*   ids,           // Array of IDs
       const UINT      ids_total,     // Number of IDs in the array
       MTAPIRES*       results        // Array of results
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SubscriptionDeleteBatch(
       ulong[]         ids,           // Array of IDs
       MTRetCode[]     retcodes       // Array of results
       )

### Parameters

**ids**  
[in] A pointer to an array of IDs of subscriptions which you want to delete. TheIMTSubscription::IDvalue is used as the identifier.

**ids_total**  
[in] The number of identifiers in the 'ids' array.

**results**  
[out] an array with subscription deletion results. The size of the 'results' array must not be less than that of 'ids'.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates that all subscriptions have been deleted. The [MT_RET_ERR_PARTIAL](../../../Return-Codes/Common-errors.md) response code means that only some of the subscriptions have been deleted. Analyze the 'results' array for a detailed information on execution results. The result of deletion of each subscription from the 'ids' array is added to 'results'. The result index corresponds to the id index in the source array.

### Note

When the method is called, it is NOT checked whether subscription deletion is allowed according to the [IMTConSubscription::ControlMode](../../../Configuration-Interfaces/Subscriptions/IMTConSubscription/ControlMode.md) parameter. Changes take place directly in the database.
