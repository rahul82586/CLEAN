[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionHistoryCreate

[Previous](SubscriptionGetByLogins.md) | [Next](SubscriptionHistoryCreateArray.md)

# IMTServerAPI::SubscriptionHistoryCreate

Create a subscription action object.
    
    
    IMTSubscriptionHistory*  IMTServerAPI::SubscriptionHistoryCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTSubscriptionHistory](../../../Database-Interfaces/Subscriptions/IMTSubscriptionHistory.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTSubscriptionHistory::Release](../../../Database-Interfaces/Subscriptions/IMTSubscriptionHistory/Release.md) method of this object.
