[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / NewsShift

[Previous](NewsClear.md) | [Next](NewsTotal.md)

# IMTConSubscription::NewsShift

Shift a news category in the list in subscription settings.

C++
    
    
    MTAPIRES  IMTConSubscription::NewsShift(
       const UINT  pos,       // News configuration position
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.NewsShift(
       uint        pos,       // News configuration position
       int         shift      // Shift
       )

### Parameters

**pos**  
[in] Position of a news setting in the list, starting with 0.

**shift**  
[in] News setting shift relative to its current position. A negative value means shift towards the top of the list, a positive value shifts towards the end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
