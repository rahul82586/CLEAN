[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / GroupNext

[Previous](GroupTotal.md) | [Next](SymbolAdd.md)

# IMTConSubscription::GroupNext

Get a group, for which the subscription is available, by index.

C++
    
    
    LPCWSTR  IMTConSubscription::GroupNext(
       const UINT   pos   // Group position
       )  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConSubscription.GroupNext(
       uint         pos,  // Group position
       )

### Parameters

**pos**  
[in] Group position in the list.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
