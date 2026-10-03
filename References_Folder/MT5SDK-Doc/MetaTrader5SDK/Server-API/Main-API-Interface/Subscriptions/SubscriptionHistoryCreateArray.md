[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionHistoryCreateArray

[Previous](SubscriptionHistoryCreate.md) | [Next](SubscriptionHistorySubscribe.md)

# IMTServerAPI::SubscriptionHistoryCreateArray

Create an object of an array of subscription actions.
    
    
    IMTSubscriptionHistoryArray*  IMTServerAPI::SubscriptionHistoryCreateArray()

### Return Value

Returns a pointer to the created object that implements the [IMTSubscriptionHistoryArray](../../../Database-Interfaces/Subscriptions/IMTSubscriptionHistoryArray.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTSubscriptionHistoryArray::Release](../../../Database-Interfaces/Subscriptions/IMTSubscriptionHistoryArray/Release.md) method of this object.
