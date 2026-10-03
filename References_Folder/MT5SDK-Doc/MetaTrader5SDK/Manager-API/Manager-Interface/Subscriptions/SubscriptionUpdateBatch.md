[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionUpdateBatch

[Previous](SubscriptionUpdate.md) | [Next](SubscriptionUpdateBatchArray.md)

# IMTManagerAPI::SubscriptionUpdateBatch

Bulk change of user subscriptions in the server database.

C++
    
    
    MTAPIRES  IMTManagerAPI::SubscriptionUpdateBatch(
       IMTSubscriptionArray*  records,  // Array of subscriptions
       MTAPIRES*              results   // Array of results
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SubscriptionUpdateBatch(
       CIMTSubscriptionArray  records,  // Array of subscriptions
       MTRetCode[]            res       // Array of results
       )

### Parameters

**records**  
[in]Array of subscriptions. The key field for finding exiting records isIMTSubscription::ID.

**results**  
[out] an array with subscription changing results. The size of the 'results' array must not be less than that of 'records'.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates that all subscriptions have been updated. The [MT_RET_ERR_PARTIAL](../../../Return-Codes/Common-errors.md) response code means that only some of the subscriptions have been updated. Analyze the 'results' array for a detailed information on execution results. The result of update of each subscription from the 'records' array is added to 'results'. The result index corresponds to the subscription index in the source array.

### Note

When the method is called, it is NOT checked whether subscription change is allowed according to the [IMTConSubscription::ControlMode](../../../Configuration-Interfaces/Subscriptions/IMTConSubscription/ControlMode.md) parameter. Changes take place directly in the database.
