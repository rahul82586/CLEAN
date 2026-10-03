[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionArray](../IMTSubscriptionArray.md) / AddCopy

[Previous](Add.md) | [Next](Delete.md)

# IMTSubscriptionArray::AddCopy

Add a copy of a subscription object at the end of an array.

C++
    
    
    MTAPIRES  IMTSubscriptionArray::AddCopy(
       const IMTSubscription*        record   // Subscription to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSubscriptionArray.AddCopy(
       CIMTSubscription              record   // Subscription to be added
       )

### Parameters

**record**  
[in]Subscription object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates a copy of the 'record' object and places it at the end of the array.

# IMTSubscriptionArray::AddCopy

Add copies of subscription objects into an array.

C++
    
    
    MTAPIRES  IMTSubscriptionArray::AddCopy(
       const IMTSubscriptionArray*  array   // Array of subscriptions to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSubscriptionArray.AddCopy(
       CIMTSubscriptionArray        array   // Array of subscriptions to be added
       )

### Parameters

**array**  
[in] An object of the array of subscriptions.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates a copy of order objects belonging to the 'array' object, and inserts them at the end of the current array.
