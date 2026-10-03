[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionArray](../IMTSubscriptionArray.md) / Delete

[Previous](AddCopy.md) | [Next](Detach.md)

# IMTSubscriptionArray::Delete

Delete a subscription object by position.

C++
    
    
    MTAPIRES  IMTSubscriptionArray::Delete(
       const UINT  pos      // Subscription position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSubscriptionArray.Delete(
       uint        pos      // Subscription position
       )

### Parameters

**pos**  
[in] Position of a subscription in an array, starting at 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The deleted object will be automatically released by [IMTSubscription::Release](../IMTSubscription/Release.md) call.
