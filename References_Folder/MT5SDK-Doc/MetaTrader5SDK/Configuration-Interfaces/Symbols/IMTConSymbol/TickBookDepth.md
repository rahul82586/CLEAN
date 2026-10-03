[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / TickBookDepth

[Previous](TickFlags.md) | [Next](FilterSoft.md)

# IMTConSymbol::TickBookDepth

Get the range of the Depth of Market set for the symbol.

C++
    
    
    UINT  IMTConSymbol::TickBookDepth()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSymbol.TickBookDepth()

Python (Manager API)
    
    
    MTConSymbol.TickBookDepth

### Return Value

The range of the Depth of Market set for the symbol.

# IMTConSymbol::TickBookDepth

Set the range of the Depth of Market.

C++
    
    
    MTAPIRES  IMTConSymbol::TickBookDepth(
       const UINT  depth      // Range of DOM
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.TickBookDepth(
       uint        depth      // Range of DOM
       )

Python (Manager API)
    
    
    MTConSymbol.TickBookDepth

### Parameters

**depth**  
[in] The range of the Depth of Market in both directions - for buy and sell requests.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
