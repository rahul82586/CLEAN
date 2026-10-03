[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionSink](../IMTSubscriptionSink.md) / OnSubscriptionJoin

[Previous](OnSubscriptionDelete.md) | [Next](OnSubscriptionCancel.md)

# IMTSubscriptionSink::OnSubscriptionJoin

Subscribing event handler.

C++
    
    
    virtual void  IMTSubscriptionSink::OnSubscriptionDelete(
       const UINT64                   manager, // Manager
       const IMTUser*                 user,    // User
       const IMTConSubscription*      config,  // Subscription configuration
       const IMTSubscription*         record,  // Subscription description
       const IMTSubscriptionHistory*  history  // Subscription action description
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTSubscriptionSink.OnSubscriptionDelete(
       ulong                          manager, // Manager
       CIMTUser                       user,    // User
       CIMTConSubscription            config,  // Subscription configuration
       CIMTSubscription               record,  // Subscription description
       CIMTSubscriptionHistory        history  // Subscription action description
       )

### Parameters

**manager**  
[in] If a trader's subscription was added by a manager, the appropriate manager login will be specified in this field (IMTConManager::Login). Otherwise 0 is passed.

**user**  
[in]The object of the user, for whom the subscription is added.

**config**  
[in]The object of the subscription configurationadded for the user.

**record**  
[in]Subscription description.

**history**  
[in]Description of the actionperformed in relation to the subscription.

### Note

Unlike [IMTSubscriptionSink::OnSubscriptionAdd](OnSubscriptionAdd.md), this event is not called when a subscription is added to the database directly via the API by the [IMTServerAPI::SubscriptionAdd](../../../Server-API/Main-API-Interface/Subscriptions/SubscriptionAdd.md) method.
