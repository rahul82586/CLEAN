[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / MarginInitial

[Previous](MarginFlags.md) | [Next](MarginMaintenance.md)

# IMTConSymbol::MarginInitial

Get the size of the initial margin.

C++
    
    
    double  IMTConSymbol::MarginInitial()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConSymbol.MarginInitial()

Python (Manager API)
    
    
    MTConSymbol.MarginInitial

### Return Value

The size of the initial margin.

# IMTConSymbol::MarginInitial

Set the size of the initial margin.

C++
    
    
    MTAPIRES  IMTConSymbol::MarginInitial(
       const double  margin      // Initial margin
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.MarginInitial(
       double        margin      // Initial margin
       )

Python (Manager API)
    
    
    MTConSymbol.MarginInitial

### Parameters

**margin**  
[in] The size of the initial margin.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
