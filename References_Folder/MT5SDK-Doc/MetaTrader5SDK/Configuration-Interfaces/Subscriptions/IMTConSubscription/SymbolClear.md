[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / SymbolClear

[Previous](SymbolDelete.md) | [Next](SymbolShift.md)

# IMTConSubscription::SymbolClear

Clear the list of trading instruments available by subscription.

C++
    
    
    MTAPIRES  IMTConSubscription::SymbolClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.SymbolClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.

### Note

This method deletes all symbols from the list of symbols available by subscription.
