[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionHistoryCreate

[Previous](SubscriptionRequestByLogins.md) | [Next](SubscriptionHistoryCreateArray.md)

# IMTAdminAPI::SubscriptionHistoryCreate

Create a subscription action object.

C++
    
    
    IMTSubscriptionHistory*  IMTAdminAPI::SubscriptionHistoryCreate()

.NET
    
    
    CIMTSubscriptionHistory  CIMTAdminAPI.SubscriptionHistoryCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTSubscriptionHistory](../../../Database-Interfaces/Subscriptions/IMTSubscriptionHistory.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTSubscriptionHistory::Release](../../../Database-Interfaces/Subscriptions/IMTSubscriptionHistory/Release.md) method of this object.
