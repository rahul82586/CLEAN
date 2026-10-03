[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / SymbolNext

[Previous](SymbolTotal.md) | [Next](NewsAdd.md)

# IMTConSubscription::SymbolNext

Get a trading instrument available by subscription, by index.

C++
    
    
    MTAPIRES  IMTConSubscription::SymbolNext(
       const UINT                 pos,       // Symbol position
       IMTConSubscriptionSymbol*  symbol     // Symbol object
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSubscription.SymbolNext(
       uint                       pos,       // Symbol position
       CIMTConSubscriptionSymbol  symbol     // Symbol object
       )

### Parameters

**pos**  
[in] Position of the symbol in the list, starting with 0.

**symbol**  
[out] Symbol objectIMTConSubscriptionSymbol. The 'symbol' object must be pre-created by theIMTServerAPI::SubscriptionCfgSymbolCreate,IMTManagerAPI::SubscriptionCfgSymbolCreateorIMTAdminAPI::SubscriptionCfgSymbolCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred corresponding to the response code.
