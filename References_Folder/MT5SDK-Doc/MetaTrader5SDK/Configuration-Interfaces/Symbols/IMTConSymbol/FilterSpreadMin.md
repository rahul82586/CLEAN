[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / FilterSpreadMin

[Previous](FilterSpreadMax.md) | [Next](FilterGap.md)

# IMTConSymbol::FilterSpreadMin

Get the minimum allowed spread value.

C++
    
    
    UINT  IMTConSymbol::FilterSpreadMin()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSymbol.FilterSpreadMin()

Python (Manager API)
    
    
    MTConSymbol.FilterSpreadMin

### Return Value

The minimum allowed spread.

# IMTConSymbol::FilterSpreadMin

Set the minimum allowed spread value.

C++
    
    
    MTAPIRES  IMTConSymbol::FilterSpreadMin(
       const UINT  spread      // The minimum allowed spread
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.FilterSpreadMin(
       uint        spread      // The minimum allowed spread
       )

Python (Manager API)
    
    
    MTConSymbol.FilterSpreadMin

### Parameters

**spread**  
[in] The minimum allowed spread.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
