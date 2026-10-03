[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Subscriptions](../Subscriptions.md) / SubscriptionCreateArray

[Previous](SubscriptionCreate.md) | [Next](SubscriptionExist.md)

# IMTReportAPI::SubscriptionCreateArray

Create an object of the subscriptions array.
    
    
    IMTSubscriptionArray*  IMTReportAPI::SubscriptionCreateArray()

### Return Value

Returns a pointer to the created object that implements the [IMTSubscriptionArray](../../../Database-Interfaces/Subscriptions/IMTSubscriptionArray.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTSubscriptionArray::Release](../../../Database-Interfaces/Subscriptions/IMTSubscriptionArray/Release.md) method of this object.
