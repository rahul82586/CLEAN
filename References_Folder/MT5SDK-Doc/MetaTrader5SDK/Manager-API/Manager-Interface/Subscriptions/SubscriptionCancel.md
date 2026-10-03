[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionCancel

[Previous](SubscriptionJoinBatch.md) | [Next](SubscriptionCancelBatch.md)

# IMTManagerAPI::SubscriptionCancel

Cancel a subscription for a user.

C++
    
    
    MTAPIRES  IMTManagerAPI::SubscriptionCancel(
       const UINT64             login,         // User
       const UINT64             subscription,  // Subscription configuration ID
       IMTSubscription*         record,        // Subscription description
       IMTSubscriptionHistory*  history        // Description of a subscription action
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTManagerAPI.SubscriptionCancel(
       ulong                    login,         // User
       ulong                    subscription,  // Subscription configuration ID
       CIMTSubscription         record,        // Subscription description
       CIMTSubscriptionHistory  history        // Description of a subscription action
       )

### Parameters

**login**  
[in]The login of the user, for whom the subscription is canceled.

**subscription**  
[in]ID of subscription configurationto be canceled.

**record**  
[out]Description of the canceled subscription.

**history**  
[out]Description of the actionwhich was performed to cancel the subscription.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

When the method is called, it is checked whether unsubscription is allowed according to the [IMTConSubscription::ControlMode](../../../Configuration-Interfaces/Subscriptions/IMTConSubscription/ControlMode.md) parameter.
