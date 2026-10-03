[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / FilterSoftTicks

[Previous](FilterSoft.md) | [Next](FilterHard.md)

# IMTConSymbol::FilterSoftTicks

Get the current value of the ticks counter for the soft filtering.

C++
    
    
    UINT  IMTConSymbol::FilterSoftTicks()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSymbol.FilterSoftTicks()

Python (Manager API)
    
    
    MTConSymbol.FilterSoftTicks

### Return Value

The current value of the ticks counter for the soft filtering.

# IMTConSymbol::FilterSoftTicks

Set the value of the ticks counter for the soft filtering.

C++
    
    
    MTAPIRES  IMTConSymbol::FilterSoftTicks(
       const UINT  ticks      // The value of the ticks counter
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.FilterSoftTicks(
       uint        ticks      // The value of the ticks counter
       )

Python (Manager API)
    
    
    MTConSymbol.FilterSoftTicks

### Parameters

**ticks**  
[in] The value of the ticks counter for the soft filtering.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
