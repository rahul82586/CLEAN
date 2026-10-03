[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionHistorySink](../IMTSubscriptionHistorySink.md) / OnSubscriptionHistoryDelete

[Previous](OnSubscriptionHistoryUpdate.md) | [Next](../../Geo-Services.md)

# IMTSubscriptionHistorySink::OnSubscriptionHistoryDelete

Event handler for deleting a subscription action from the database.

C++
    
    
    virtual void  IMTSubscriptionHistorySink::OnSubscriptionHistoryDelete(
       const IMTSubscriptionHistory*  subscription  // A pointer to the action object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTSubscriptionHistorySink.OnSubscriptionHistoryDelete(
       CIMTSubscriptionHistory        subscription  // Action object
       )

### Parameters

**subscription**  
[in] A pointer to thesubscription action object.

### Note

The API calls this method to notify that a subscription action has been deleted from the database.
