[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / FilterGap

[Previous](FilterSpreadMin.md) | [Next](FilterGapTicks.md)

# IMTConSymbol::FilterGap

Get the difference between the previous and the next quote, starting from which a gap is considered to be formed.

C++
    
    
    UINT  IMTConSymbol::FilterGap()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSymbol.FilterGap()

Python (Manager API)
    
    
    MTConSymbol.FilterGap

### Return Value

The difference between the previous and the next quote, starting from which a gap is considered to be formed.

# IMTConSymbol::FilterGap

Set the the difference between the previous and the next quote, starting from which a gap is considered to be formed.

C++
    
    
    MTAPIRES  IMTConSymbol::FilterGap(
       const UINT  ticks       // Gap level
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.FilterGap(
       uint        ticks       // Gap level
       )

Python (Manager API)
    
    
    MTConSymbol.FilterGap

### Parameters

**filter**  
[in] The difference between the previous and the next quote, starting from which a gap is considered to be formed.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
