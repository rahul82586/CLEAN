[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / SymbolUpdate

[Previous](SymbolAdd.md) | [Next](SymbolDelete.md)

# IMTConSubscription::SymbolUpdate

Update a trading instrument in the list of symbols available by subscription.

C++
    
    
    MTAPIRES  IMTConSubscription::SymbolUpdate(
       const UINT                       pos,       // Symbol position
       const IMTConSubscriptionSymbol*  symbol     // Symbol object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.SymbolUpdate(
       uint                             pos,       // Symbol position
       CIMTConSubscriptionSymbol        symbol     // Symbol object
       )

### Parameters

**pos**  
[in] Position of a condition in the list, starting at 0.

**symbol**  
[in] Symbol objectIMTConSubscriptionSymbol.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
