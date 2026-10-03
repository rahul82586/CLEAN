[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionSink](../IMTSubscriptionSink.md) / OnSubscriptionUpdate

[Previous](OnSubscriptionAdd.md) | [Next](OnSubscriptionDelete.md)

# IMTSubscriptionSink::OnSubscriptionUpdate

Subscription change event handler.

C++
    
    
    virtual void  IMTSubscriptionSink::OnSubscriptionUpdate(
       const IMTSubscription*  subscription  // A pointer to the subscription object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTSubscriptionSink.OnSubscriptionUpdate(
       CIMTSubscription        subscription  // Subscription object
       )

### Parameters

**subscription**  
[in] A pointer to thesubscription object.

### Note

The API calls this method to notify that a subscription has been updated.
