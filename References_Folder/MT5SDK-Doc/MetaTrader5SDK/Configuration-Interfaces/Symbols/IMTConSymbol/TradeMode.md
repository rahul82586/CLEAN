[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / TradeMode

[Previous](SubscriptionsDelay.md) | [Next](CalcMode.md)

# IMTConSymbol::TradeMode

Get the current symbol trading mode.

C++
    
    
    UINT  IMTConSymbol::TradeMode()  const

.NET (Gateway/Manager API)
    
    
    EnTradeMode  CIMTConSymbol.TradeMode()

Python (Manager API)
    
    
    MTConSymbol.TradeMode

### Return Value

One of the values of the [IMTConSymbol::EnTradeMode (#entrademode)](Enumerations.md#entrademode) mode.

# IMTConSymbol::TradeMode

Set the current symbol trading mode.

C++
    
    
    MTAPIRES  IMTConSymbol::TradeMode(
       const UINT  mode      // Trading mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.TradeMode(
       EnTradeMode mode      // Trading mode
       )

Python (Manager API)
    
    
    MTConSymbol.TradeMode

### Parameters

**mode**  
[in] To pass the trading mode, theIMTConSymbol::EnTradeModeenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
