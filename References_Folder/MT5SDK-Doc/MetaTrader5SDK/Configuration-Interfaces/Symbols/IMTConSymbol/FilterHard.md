[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / FilterHard

[Previous](FilterSoftTicks.md) | [Next](FilterHardTicks.md)

# IMTConSymbol::FilterHard

Get the hard level of price filtering.

C++
    
    
    UINT  IMTConSymbol::FilterHard()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSymbol.FilterHard()

Python (Manager API)
    
    
    MTConSymbol.FilterHard

### Return Value

The hard level of price filtering.

# IMTConSymbol::FilterHard

Set the hard level of price filtering.

C++
    
    
    MTAPIRES  IMTConSymbol::FilterHard(
       const UINT  filter      // Hard filtration level
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.FilterHard(
       uint        filter      // Hard filtration level
       )

Python (Manager API)
    
    
    MTConSymbol.FilterHard

### Parameters

**filter**  
[in] The hard level of price filtering.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
