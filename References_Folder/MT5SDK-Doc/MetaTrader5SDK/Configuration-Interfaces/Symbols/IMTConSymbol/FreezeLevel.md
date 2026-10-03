[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / FreezeLevel

[Previous](StopsLevel.md) | [Next](QuotesTimeout.md)

# IMTConSymbol::FreezeLevel

Get the price band, within which it is not allowed to modify orders and positions.

C++
    
    
    INT  IMTConSymbol::FreezeLevel()  const

.NET (Gateway/Manager API)
    
    
    int  CIMTConSymbol.FreezeLevel()

Python (Manager API)
    
    
    MTConSymbol.FreezeLevel

### Return Value

The price band, within which it is not allowed to modify orders and positions.

# IMTConSymbol::FreezeLevel

Set the price band, within which it is not allowed to modify orders and positions.

C++
    
    
    MTAPIRES  IMTConSymbol::FreezeLevel(
       const INT  level      // The price band
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.FreezeLevel(
       int        level      // The price band
       )

Python (Manager API)
    
    
    MTConSymbol.FreezeLevel

### Parameters

**level**  
[in] The price band, within which it is not allowed to modify orders and positions.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
