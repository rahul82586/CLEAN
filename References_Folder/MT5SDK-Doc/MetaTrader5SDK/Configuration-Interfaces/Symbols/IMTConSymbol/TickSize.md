[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / TickSize

[Previous](TickValue.md) | [Next](ContractSize.md)

# IMTConSymbol::TickSize

Get the size of one tick of a symbol.

C++
    
    
    double  IMTConSymbol::TickSize()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConSymbol.TickSize()

Python (Manager API)
    
    
    MTConSymbol.TickSize

### Return Value

Symbol tick size.

# IMTConSymbol::TickSize

Set the size of one tick of a symbol.

C++
    
    
    MTAPIRES  IMTConSymbol::TickSize(
       const double  size      // Symbol tick size
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.TickSize(
       double        size      // Symbol tick size
       )

Python (Manager API)
    
    
    MTConSymbol.TickSize

### Parameters

**size**  
[in] Symbol tick size.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
