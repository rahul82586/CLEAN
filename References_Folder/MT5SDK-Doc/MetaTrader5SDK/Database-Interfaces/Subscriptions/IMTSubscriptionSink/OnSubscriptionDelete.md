[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionSink](../IMTSubscriptionSink.md) / OnSubscriptionDelete

[Previous](OnSubscriptionUpdate.md) | [Next](OnSubscriptionJoin.md)

# IMTSubscriptionSink::OnSubscriptionDelete

Event handler for deleting a subscription from the database.

C++
    
    
    virtual void  IMTSubscriptionSink::OnSubscriptionDelete(
       const IMTSubscription*  subscription  // A pointer to the subscription object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTSubscriptionSink.OnSubscriptionDelete(
       CIMTSubscription        subscription  // Subscription object
       )

### Parameters

**subscription**  
[in] A pointer to thesubscription object.

### Note

The API calls this method to notify that a subscription has been deleted from the database: unsubscribed by a manager, a trader or via API ([IMTServerAPI::SubscriptionCancel](../../../Server-API/Main-API-Interface/Subscriptions/SubscriptionCancel.md), [IMTAdminAPI::SubscriptionCancel](../../../Manager-API/Administrator-Interface/Subscriptions/SubscriptionCancel.md), [IMTManagerAPI::SubscriptionCancel](../../../Manager-API/Manager-Interface/Subscriptions/SubscriptionCancel.md)), as well as when a subscription is directly deleted from the database via the API ([IMTServerAPI::SubscriptionDelete](../../../Server-API/Main-API-Interface/Subscriptions/SubscriptionDelete.md), [IMTAdminAPI::SubscriptionDelete](../../../Manager-API/Administrator-Interface/Subscriptions/SubscriptionDelete.md), [IMTManagerAPI::SubscriptionDelete](../../../Manager-API/Manager-Interface/Subscriptions/SubscriptionDelete.md)).
