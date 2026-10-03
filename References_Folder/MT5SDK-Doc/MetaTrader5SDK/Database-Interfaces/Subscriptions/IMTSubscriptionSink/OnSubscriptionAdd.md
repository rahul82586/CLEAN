[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionSink](../IMTSubscriptionSink.md) / OnSubscriptionAdd

[Previous](../IMTSubscriptionSink.md) | [Next](OnSubscriptionUpdate.md)

# IMTSubscriptionSink::OnSubscriptionAdd

Event handler for adding a subscription to the database.

C++
    
    
    virtual void  IMTSubscriptionSink::OnSubscriptionAdd(
       const IMTSubscription*  subscription  // A pointer to the subscription object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTSubscriptionSink.OnSubscriptionAdd(
       CIMTSubscription        subscription  // Subscription object
       )

### Parameters

**subscription**  
[in] A pointer to thesubscription object.

### Note

The API calls this method to notify that a new subscription has been added to the database: when a subscription has been started by a manager, a trader or via the API ([IMTServerAPI::SubscriptionJoin](../../../Server-API/Main-API-Interface/Subscriptions/SubscriptionJoin.md), [IMTAdminAPI::SubscriptionJoin](../../../Manager-API/Administrator-Interface/Subscriptions/SubscriptionJoin.md), [IMTManagerAPI::SubscriptionJoin](../../../Manager-API/Manager-Interface/Subscriptions/SubscriptionJoin.md)), as well as when a subscription has been added directly to the database via the API method [IMTServerAPI::SubscriptionAdd](../../../Server-API/Main-API-Interface/Subscriptions/SubscriptionAdd.md).
