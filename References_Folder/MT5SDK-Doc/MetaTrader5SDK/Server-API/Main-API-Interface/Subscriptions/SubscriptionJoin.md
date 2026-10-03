[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionJoin

[Previous](SubscriptionUnsubscribe.md) | [Next](SubscriptionCancel.md)

# IMTServerAPI::SubscriptionJoin

Add a subscription for a user.
    
    
    MTAPIRES  IMTServerAPI::SubscriptionJoin(
       const UINT64             login,         // User
       const UINT64             subscription,  // Subscription configuration ID
       IMTSubscription*         record,        // Subscription description
       IMTSubscriptionHistory*  history        // Description of a subscription action
       )

### Parameters

**login**  
[in]The login of the user, for whom the subscription is added.

**subscription**  
[in]ID of subscription configurationto be added.

**record**  
[out]Description of the created subscription.

**history**  
[out]Description of the actionwhich was performed to create the subscription.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

When the method is called, it is checked whether subscription adding is allowed according to the [IMTConSubscription::ControlMode](../../../Configuration-Interfaces/Subscriptions/IMTConSubscription/ControlMode.md) parameter. If necessary, the subscription cost is debited from the corresponding account. Thus, subscribing by this method is similar to how a trader subscribes.
