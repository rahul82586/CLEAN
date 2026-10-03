[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionCreateArray

[Previous](SubscriptionCreate.md) | [Next](SubscriptionJoin.md)

# IMTManagerAPI::SubscriptionCreateArray

Create an object of the subscriptions array.

C++
    
    
    IMTSubscriptionArray*  IMTManagerAPI::SubscriptionCreateArray()

.NET
    
    
    CIMTSubscriptionArray  CIMTManagerAPI.SubscriptionCreateArray()

### Return Value

Returns a pointer to the created object that implements the [IMTSubscriptionArray](../../../Database-Interfaces/Subscriptions/IMTSubscriptionArray.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTSubscriptionArray::Release](../../../Database-Interfaces/Subscriptions/IMTSubscriptionArray/Release.md) method of this object.
