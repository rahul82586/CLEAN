[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / SymbolAdd

[Previous](GroupNext.md) | [Next](SymbolUpdate.md)

# IMTConSubscription::SymbolAdd

Add a trading instrument to the list of symbols available by subscription.

C++
    
    
    MTAPIRES  IMTConSubscription::SymbolAdd(
       IMTConSubscriptionSymbol*  symbol    // Symbol object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.SymbolAdd(
       CIMTConSubscriptionSymbol  symbol    // Symbol object
       )

### Parameters

**symbol**  
[in] Symbol objectIMTConSubscriptionSymbol.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
