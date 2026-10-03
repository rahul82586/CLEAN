[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionHistoryCreateArray

[Previous](SubscriptionHistoryCreate.md) | [Next](SubscriptionHistoryUpdate.md)

# IMTAdminAPI::SubscriptionHistoryCreateArray

Create an object of an array of subscription actions.

C++
    
    
    IMTSubscriptionHistoryArray*  IMTAdminAPI::SubscriptionHistoryCreateArray()

.NET
    
    
    CIMTSubscriptionHistoryArray  CIMTAdminAPI.SubscriptionHistoryCreateArray()

### Return Value

Returns a pointer to the created object that implements the [IMTSubscriptionHistoryArray](../../../Database-Interfaces/Subscriptions/IMTSubscriptionHistoryArray.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTSubscriptionHistoryArray::Release](../../../Database-Interfaces/Subscriptions/IMTSubscriptionHistoryArray/Release.md) method of this object.
