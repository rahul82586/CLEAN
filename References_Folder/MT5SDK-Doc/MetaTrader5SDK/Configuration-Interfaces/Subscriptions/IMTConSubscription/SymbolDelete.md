[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / SymbolDelete

[Previous](SymbolUpdate.md) | [Next](SymbolClear.md)

# IMTConSubscription::SymbolDelete

Delete a trading instrument from the list of symbols available by subscription.

C++
    
    
    MTAPIRES  IMTConSubscription::SymbolDelete(
       const UINT  pos      // Symbol position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.SymbolDelete(
       uint        pos      // symbol position
       )

### Parameters

**pos**  
[in] Position of the symbol in the list, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
