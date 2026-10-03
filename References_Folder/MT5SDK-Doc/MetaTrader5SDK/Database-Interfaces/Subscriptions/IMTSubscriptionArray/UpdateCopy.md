[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionArray](../IMTSubscriptionArray.md) / UpdateCopy

[Previous](Update.md) | [Next](Shift.md)

# IMTSubscriptionArray::UpdateCopy

Change a subscription at the specified position of an array by copying the parameters of a passed subscription object.

C++
    
    
    MTAPIRES  IMTSubscriptionArray::UpdateCopy(
       const UINT              pos,    // Position
       const IMTSubscription*  record  // Subscription object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSubscriptionArray.UpdateCopy(
       uint                    pos,    // Position
       CIMTSubscription        record  // Subscription object
       )

### Parameters

**pos**  
[in] Position of a subscription in an array, starting at 0.

**record**  
[in]Subscription object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.

### Note

This method copies the 'record' object parameters to the subscription object at the specified position in the array.
