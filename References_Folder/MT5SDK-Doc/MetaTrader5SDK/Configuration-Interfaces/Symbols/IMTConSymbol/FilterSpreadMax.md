[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / FilterSpreadMax

[Previous](FilterDiscard.md) | [Next](FilterSpreadMin.md)

# IMTConSymbol::FilterSpreadMax

Get the maximum allowed spread value.

C++
    
    
    UINT  IMTConSymbol::FilterSpreadMax()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSymbol.FilterSpreadMax()

Python (Manager API)
    
    
    MTConSymbol.FilterSpreadMax

### Return Value

The maximum allowed spread value.

# IMTConSymbol::FilterSpreadMax

Set the maximum allowed spread value.

C++
    
    
    MTAPIRES  IMTConSymbol::FilterSpreadMax(
       const UINT  spread      // The maximum allowed spread
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.FilterSpreadMax(
       uint        spread      // The maximum allowed spread
       )

Python (Manager API)
    
    
    MTConSymbol.FilterSpreadMax

### Parameters

**spread**  
[in] The maximum allowed spread.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
