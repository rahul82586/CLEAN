[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionHistoryArray](../IMTSubscriptionHistoryArray.md) / Next

[Previous](Total.md) | [Next](Sort.md)

# IMTSubscriptionHistoryArray::Next

Get a subscription action object by position.

C++
    
    
    IMTSubscriptionHistory*  IMTSubscriptionHistoryArray::Next(
       const UINT  pos      // Action position
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTSubscriptionHistory  CIMTSubscriptionHistoryArray.Next(
       uint        pos      // Action position
       )

### Parameters

**pos**  
[in] Position of a subscription action in an array, starting at 0.

### Return Value

If successful, it returns a pointer to the action object at the specified array position. Otherwise, it returns NULL.

### Note

The lifetime of the returned object is controlled by the current array object. Thus, when deleting an array object, the returned pointer will be invalid.
