[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / TickValue

[Previous](SpreadDiffBalance.md) | [Next](TickSize.md)

# IMTConSymbol::TickValue

Get the price of one tick of a symbol.

C++
    
    
    double  IMTConSymbol::TickValue()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConSymbol.TickValue()

Python (Manager API)
    
    
    MTConSymbol.TickValue

### Return Value

Symbol tick price.

# IMTConSymbol::TickValue

Set the price of one tick of a symbol.

C++
    
    
    MTAPIRES  IMTConSymbol::TickValue(
       const double  value      // Tick price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.TickValue(
       double        value      // Tick price
       )

Python (Manager API)
    
    
    MTConSymbol.TickValue

### Parameters

**value**  
[in] Symbol tick price.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
