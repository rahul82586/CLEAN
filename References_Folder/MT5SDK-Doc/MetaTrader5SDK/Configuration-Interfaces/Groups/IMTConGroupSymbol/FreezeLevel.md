[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / FreezeLevel

[Previous](StopsLevelDefault.md) | [Next](FreezeLevelDefault.md)

# IMTConGroupSymbol::FreezeLevel

Get the price band, within which it is not allowed to modify orders and positions for the group.

C++
    
    
    INT  IMTConGroupSymbol::FreezeLevel()  const

.NET (Gateway/Manager API)
    
    
    int  CIMTConGroupSymbol.FreezeLevel()

Python (Manager API)
    
    
    MTConGroupSymbol.FreezeLevel

### Return Value

The price band, within which it is not allowed to modify orders and positions for the group.

# IMTConGroupSymbol::FreezeLevel

Set the price band, within which it is not allowed to modify orders and positions for the group.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::FreezeLevel(
       const INT  level      // Price band with modification prohibited
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.FreezeLevel(
       int        level      // Price band with modification prohibited
       )

Python (Manager API)
    
    
    MTConGroupSymbol.FreezeLevel

### Parameters

**level**  
[in] The price band, within which it is not allowed to change orders and positions for the group.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
