[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionHistorySink](../IMTSubscriptionHistorySink.md) / OnSubscriptionHistoryAdd

[Previous](../IMTSubscriptionHistorySink.md) | [Next](OnSubscriptionHistoryUpdate.md)

# IMTSubscriptionHistorySink::OnSubscriptionHistoryAdd

Event handler for adding a subscription action to the database.

C++
    
    
    virtual void  IMTSubscriptionHistorySink::OnSubscriptionHistoryAdd(
       const IMTSubscriptionHistory*  subscription  // A pointer to the action object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTSubscriptionHistorySink.OnSubscriptionHistoryAdd(
       CIMTSubscriptionHistory        subscription  // Action object
       )

### Parameters

**subscription**  
[in] A pointer to thesubscription action object.

### Note

The API calls this method to notify that a new subscription action has been added to the database.
