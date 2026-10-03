[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionCancelBatch

[Previous](SubscriptionCancel.md) | [Next](SubscriptionUpdate.md)

# IMTAdminAPI::SubscriptionCancelBatch

Bulk canceling of user subscriptions.

C++
    
    
    MTAPIRES  IMTAdminAPI::SubscriptionCancelBatch(
       const UINT64*                 logins,        // Array of users
       const UINT64*                 subscriptions, // Array of configuration IDs
       const UINT                    total,         // Number
       MTAPIRES*                     results,       // Array of results
       IMTSubscriptionArray*         records,       // Description of subscriptions
       IMTSubscriptionHistoryArray*  history        // Description of subscription actions
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAdminAPI.SubscriptionCancelBatch(
       ulong[]                       logins,        // Array of users
       ulong[]                       subscriptions, // Array of configuration IDs
       MTRetCode[]                   results,       // Array of results
       CIMTSubscriptionArray         records,       // Description of subscriptions
       CIMTSubscriptionHistoryArray  history        // Description of subscription actions
       )

### Parameters

**logins**  
[in] An array ofuser loginsfor which the subscriptions are canceled. The array size must match the array of the 'subscriptions' array.

**subscriptions**  
[in] An array ofIDs of subscription configurationswhich are canceled. The array size must match the array of the 'logins' array.

**total**  
[in] The number of logins/subscriptions.

**results**  
[out] an array with subscription canceling results. The size of the 'results' array must not be less than that of 'logins'.

**records**  
[out] An array ofdescriptions of canceled subscriptions.

**history**  
[out] An array ofdescriptions of actionswhich were performed to canceled subscriptions

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates that all orders have been updated. The [MT_RET_ERR_PARTIAL](../../../Return-Codes/Common-errors.md) response code means that only some of the subscriptions have been added. To obtain further details, you can check subscription statuses in the returned 'records' array ([IMTSubscription::Status](../../../Database-Interfaces/Subscriptions/IMTSubscription/Status.md)).

### Note

When the method is called, it is checked whether unsubscription is allowed according to the [IMTConSubscription::ControlMode](../../../Configuration-Interfaces/Subscriptions/IMTConSubscription/ControlMode.md) parameter.
