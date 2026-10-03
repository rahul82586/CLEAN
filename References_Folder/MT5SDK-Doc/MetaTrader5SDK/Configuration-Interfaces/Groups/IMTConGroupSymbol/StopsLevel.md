[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / StopsLevel

[Previous](SpreadDiffBalanceDefault.md) | [Next](StopsLevelDefault.md)

# IMTConGroupSymbol::StopsLevel

Get the price band, within which the group is not allowed to place stop orders for a symbol.

C++
    
    
    INT  IMTConGroupSymbol::StopsLevel()  const

.NET (Gateway/Manager API)
    
    
    int  CIMTConGroupSymbol.StopsLevel()

Python (Manager API)
    
    
    MTConGroupSymbol.StopsLevel

### Return Value

The price band from the current market price, inside which it is not allowed to place stop orders for the group.

# IMTConGroupSymbol::StopsLevel

Set the price band, within which the group is not allowed to place stop orders for a symbol.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::StopsLevel(
       const INT  level      // A band of stop orders
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.StopsLevel(
       int        level      // A band of stop orders
       )

Python (Manager API)
    
    
    MTConGroupSymbol.StopsLevel

### Parameters

**level**  
[in] The price band from the current market price, within which it is not allowed to place stop orders for the group.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
