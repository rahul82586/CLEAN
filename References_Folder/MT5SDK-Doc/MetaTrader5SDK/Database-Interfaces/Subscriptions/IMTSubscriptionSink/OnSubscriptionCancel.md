[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionSink](../IMTSubscriptionSink.md) / OnSubscriptionCancel

[Previous](OnSubscriptionJoin.md) | [Next](../IMTSubscriptionHistorySink.md)

# IMTSubscriptionSink::OnSubscriptionCancel

Unsubscribing event handler.

C++
    
    
    virtual void  IMTSubscriptionSink::OnSubscriptionCancel(
       const UINT64                   manager, // Manager
       const IMTUser*                 user,    // User
       const IMTConSubscription*      config,  // Subscription configuration
       const IMTSubscription*         record,  // Subscription description
       const IMTSubscriptionHistory*  history  // Subscription action description
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTSubscriptionSink.OnSubscriptionCancel(
       ulong                          manager, // Manager
       CIMTUser                       user,    // User
       CIMTConSubscription            config,  // Subscription configuration
       CIMTSubscription               record,  // Subscription description
       CIMTSubscriptionHistory        history  // Subscription action description
       )

### Parameters

**manager**  
[in] If a trader's subscription was canceled by a manager, the appropriate manager login will be specified in this field (IMTConManager::Login). Otherwise 0 is passed.

**user**  
[in]The object of the user, for whom the subscription is canceled.

**config**  
[in]The object of the subscription configurationcanceled for the user.

**record**  
[in]Subscription description.

**history**  
[in]Description of the actionperformed in relation to the subscription.

### Note

Unlike [IMTSubscriptionSink::OnSubscriptionDelete](OnSubscriptionAdd.md), this event is not called when a subscription is deleted directly from the database by the following API methods: [IMTServerAPI::SubscriptionDelete](../../../Server-API/Main-API-Interface/Subscriptions/SubscriptionDelete.md), [IMTAdminAPI::SubscriptionDelete](../../../Manager-API/Administrator-Interface/Subscriptions/SubscriptionDelete.md), [IMTManagerAPI::SubscriptionDelete](../../../Manager-API/Manager-Interface/Subscriptions/SubscriptionDelete.md).
