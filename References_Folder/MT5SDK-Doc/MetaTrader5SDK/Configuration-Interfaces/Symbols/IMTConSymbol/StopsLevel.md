[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / StopsLevel

[Previous](ContractSize.md) | [Next](FreezeLevel.md)

# IMTConSymbol::StopsLevel

Get the price band, within which placing stop orders is not allowed.

C++
    
    
    INT  IMTConSymbol::StopsLevel()  const

.NET (Gateway/Manager API)
    
    
    int  CIMTConSymbol.StopsLevel()

Python (Manager API)
    
    
    MTConSymbol.StopsLevel

### Return Value

The price band from the current market price, inside which it is not allowed to place stop orders.

# IMTConSymbol::StopsLevel

Set the price band, within which placing stop orders is not allowed.
    
    
    MTAPIRES  IMTConSymbol::StopsLevel(
       const INT  level      // A band of stop orders
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.StopsLevel(
       int        level      // A band of stop orders
       )

Python (Manager API)
    
    
    MTConSymbol.StopsLevel

### Parameters

**level**  
[in] The price band from the current market price, within which it is not allowed to place stop orders.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
