[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionCreate

[Previous](../Subscriptions.md) | [Next](SubscriptionCreateArray.md)

# IMTServerAPI::SubscriptionCreate

Create a subscription object.
    
    
    IMTSubscription*  IMTServerAPI::SubscriptionCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTSubscription](../../../Database-Interfaces/Subscriptions/IMTSubscription.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTSubscription::Release](../../../Database-Interfaces/Subscriptions/IMTSubscription/Release.md) method of this object.
