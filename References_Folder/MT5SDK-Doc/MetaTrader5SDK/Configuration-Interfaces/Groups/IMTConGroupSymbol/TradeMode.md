[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / TradeMode

[Previous](Path.md) | [Next](TradeModeDefault.md)

# IMTConGroupSymbol::TradeMode

Get the symbol trading mode for the group.

C++
    
    
    UINT  IMTConGroupSymbol::TradeMode()  const

.NET (Gateway/Manager API)
    
    
    EnTradeMode  CIMTConGroupSymbol.TradeMode()

Python (Manager API)
    
    
    MTConGroupSymbol.TradeMode

### Return Value

One of the values of the [IMTConSymbol::EnTradeMode (#entrademode)](../../Symbols/IMTConSymbol/Enumerations.md#entrademode) mode.

# IMTConGroupSymbol::TradeMode

Set the symbol trading mode for the group.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::TradeMode(
       const UINT   mode     // Trading mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.TradeMode(
       EnTradeMode  mode     // Trading mode
       )

Python (Manager API)
    
    
    MTConGroupSymbol.TradeMode

### Parameters

**mode**  
[in] To pass the trading mode, theIMTConSymbol::EnTradeModeenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
