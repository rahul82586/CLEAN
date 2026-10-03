[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionArray](../IMTSubscriptionArray.md) / Shift

[Previous](UpdateCopy.md) | [Next](Total.md)

# IMTSubscriptionArray::Shift

Change the position of a subscription in an array.

C++
    
    
    MTAPIRES  IMTSubscriptionArray::Shift(
       const UINT  pos,       // Subscription position
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSubscriptionArray.Shift(
       uint        pos,       // Subscription position
       int         shift      // Shift
       )

### Parameters

**pos**  
[in] Position of a subscription in an array, starting at 0.

**shift**  
[in] Shift of a subscription relative to its current position. A negative value means shift towards the array beginning, while a positive value means shift towards its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
