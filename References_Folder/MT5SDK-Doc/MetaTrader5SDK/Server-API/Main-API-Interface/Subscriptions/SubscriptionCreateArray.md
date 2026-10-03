[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionCreateArray

[Previous](SubscriptionCreate.md) | [Next](SubscriptionSubscribe.md)

# IMTServerAPI::SubscriptionCreateArray

Create an object of the subscriptions array.
    
    
    IMTSubscriptionArray*  IMTServerAPI::SubscriptionCreateArray()

### Return Value

Returns a pointer to the created object that implements the [IMTSubscriptionArray](../../../Database-Interfaces/Subscriptions/IMTSubscriptionArray.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTSubscriptionArray::Release](../../../Database-Interfaces/Subscriptions/IMTSubscriptionArray/Release.md) method of this object.
