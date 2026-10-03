[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / NewsDelete

[Previous](NewsUpdate.md) | [Next](NewsClear.md)

# IMTConSubscription::NewsDelete

Delete a news category from the news list available by subscription.

C++
    
    
    MTAPIRES  IMTConSubscription::NewsDelete(
       const UINT  pos      // News setting position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.SymbolDelete(
       uint        pos      // News setting position
       )

### Parameters

**pos**  
[in] Position of a news setting in the list, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
