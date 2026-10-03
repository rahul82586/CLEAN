[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionHistorySink](../IMTSubscriptionHistorySink.md) / OnSubscriptionHistoryUpdate

[Previous](OnSubscriptionHistoryAdd.md) | [Next](OnSubscriptionHistoryDelete.md)

# IMTSubscriptionHistorySink::OnSubscriptionHistoryUpdate

Subscription action change event handler.

C++
    
    
    virtual void  IMTSubscriptionHistorySink::OnSubscriptionHistoryUpdate(
       const IMTSubscriptionHistory*  subscription  // A pointer to the action object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTSubscriptionHistorySink.OnSubscriptionHistoryUpdate(
       CIMTSubscriptionHistory        subscription  // Action object
       )

### Parameters

**subscription**  
[in] A pointer to thesubscription action object.

### Note

The API calls this method to notify that a subscription action in a database has been updated.
