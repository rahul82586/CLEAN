[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / TradeFlags

[Previous](PriceLimitMin.md) | [Next](OrderFlags.md)

# IMTConSymbol::TradeFlags

Get the trade flags of the symbol.

C++
    
    
    UINT64  IMTConSymbol::TradeFlags()  const

.NET (Gateway/Manager API)
    
    
    EnTradeFlags  CIMTConSymbol.TradeFlags()

Python (Manager API)
    
    
    MTConSymbol.TradeFlags

### Return Value

A value of the [IMTConSymbol::EnTradeFlags (#entradeflags)](Enumerations.md#entradeflags) enumeration.

# IMTConSymbol::TradeFlags

Set Get the trade flags of the symbol.

C++
    
    
    MTAPIRES  IMTConSymbol::TradeFlags(
       const UINT64  flags      // Flags of settings
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.TradeFlags(
       EnTradeFlags  flags      // Flags of settings
       )

Python (Manager API)
    
    
    MTConSymbol.TradeFlags

### Parameters

**flags**  
[in] To pass the trade flags, theIMTConSymbol::EnTradeFlagsenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
