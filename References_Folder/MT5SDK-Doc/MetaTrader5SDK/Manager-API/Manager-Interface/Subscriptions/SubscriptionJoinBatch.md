[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionJoinBatch

[Previous](SubscriptionJoin.md) | [Next](SubscriptionCancel.md)

# IMTManagerAPI::SubscriptionJoinBatch

Bulk adding of subscriptions for users.

C++
    
    
    MTAPIRES  IMTManagerAPI::SubscriptionJoinBatch(
       const UINT64*                 logins,        // Array of users
       const UINT64*                 subscriptions, // Array of configuration IDs
       const UINT                    total,         // Number
       MTAPIRES*                     results        // Array of results
       IMTSubscriptionArray*         records,       // Description of subscriptions
       IMTSubscriptionHistoryArray*  history        // Description of subscription actions
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTManagerAPI.SubscriptionJoinBatch(
       ulong[]                       logins,        // Array of users
       ulong[]                       subscriptions, // Array of configuration IDs
       MTRetCode[]                   results,       // Array of results
       CIMTSubscriptionArray         records,       // Description of subscriptions
       CIMTSubscriptionHistoryArray  history        // Description of subscription actions
       )

### Parameters

**logins**  
[in] An array ofuser loginsfor which the subscriptions are added. The array size must match the array of the 'subscriptions' array.

**subscriptions**  
[in] An array ofIDs of subscription configurationswhich are added. The array size must match the array of the 'logins' array.

**total**  
[in] The number of logins/subscriptions.

**results**  
[out] an array with subscription adding results. The size of the 'results' array must not be less than that of 'logins'.

**records**  
[out] An array ofdescriptions of created subscriptions.

**history**  
[out] An array ofdescriptions of actionswhich were performed to create subscriptions

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates that all orders have been updated. The [MT_RET_ERR_PARTIAL](../../../Return-Codes/Common-errors.md) response code means that only some of the subscriptions have been added. Analyze the 'results' array for a detailed information on execution results. The result of adding of each subscription from the 'subscriptions' array is added to 'results'. The result index corresponds to the subscription index in the source array.

### Note

When the method is called, it is checked whether subscription adding is allowed according to the [IMTConSubscription::ControlMode](../../../Configuration-Interfaces/Subscriptions/IMTConSubscription/ControlMode.md) parameter. If necessary, the subscription cost is debited from the corresponding account. Thus, subscribing by this method is similar to how a trader subscribes.
