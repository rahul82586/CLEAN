[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / GroupShift

[Previous](GroupClear.md) | [Next](GroupTotal.md)

# IMTConSubscription::GroupShift

Shift a country for which the subscription is available.

C++
    
    
    MTAPIRES  IMTConSubscription::GroupShift(
       const UINT  pos,       // Group position
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.GroupShift(
       uint        pos,       // Group position
       int         shift      // Shift
       )

### Parameters

**pos**  
[in] Position of the group in the list, starting with 0.

**shift**  
[in] Shift of a group relative to its current position. A negative value means shift towards the top of the list, a positive value shifts towards the end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
