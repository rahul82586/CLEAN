[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / FilterDiscard

[Previous](FilterHardTicks.md) | [Next](FilterSpreadMax.md)

# IMTConSymbol::FilterDiscard

Get the discard level of price filtering.

C++
    
    
    UINT  IMTConSymbol::FilterDiscard()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSymbol.FilterDiscard()

Python (Manager API)
    
    
    MTConSymbol.FilterDiscard

### Return Value

The discard level of price filtering.

# IMTConSymbol::FilterDiscard

Set the discard level of price filtering.

C++
    
    
    MTAPIRES  IMTConSymbol::FilterDiscard(
       const UINT  ticks      // The discard filtration level
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.FilterDiscard(
       uint        ticks      // The discard filtration level
       )

Python (Manager API)
    
    
    MTConSymbol.FilterDiscard

### Parameters

**ticks**  
[in] The discard level of price filtering.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
