[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionArray](../IMTSubscriptionArray.md) / Next

[Previous](Total.md) | [Next](Sort.md)

# IMTSubscriptionArray::Next

Get a subscription object by position.

C++
    
    
    IMTSubscription*  IMTSubscriptionArray::Next(
       const UINT  pos      // Subscription position
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTSubscription  CIMTSubscriptionArray.Next(
       uint        pos      // Subscription position
       )

### Parameters

**pos**  
[in] Position of a subscription in an array, starting at 0.

### Return Value

If successful, it returns a pointer to the subscription object at the specified array position. Otherwise, it returns NULL.

### Note

The lifetime of the returned object is controlled by the current array object. Thus, when deleting an array object, the returned pointer will be invalid.
