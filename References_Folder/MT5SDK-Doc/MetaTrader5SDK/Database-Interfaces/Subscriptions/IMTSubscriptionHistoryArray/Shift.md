[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionHistoryArray](../IMTSubscriptionHistoryArray.md) / Shift

[Previous](UpdateCopy.md) | [Next](Total.md)

# IMTSubscriptionHistoryArray::Shift

Change the position of a subscription action in an array.

C++
    
    
    MTAPIRES  IMTSubscriptionHistoryArray::Shift(
       const UINT  pos,       // Action position
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTSubscriptionHistoryArray.Shift(
       uint        pos,       // Action position
       int         shift      // Shift
       )

### Parameters

**pos**  
[in] Position of a subscription action in an array, starting at 0.

**shift**  
[in] The shift of the action relative to its current position. A negative value means shift towards the array beginning, while a positive value means shift towards its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
