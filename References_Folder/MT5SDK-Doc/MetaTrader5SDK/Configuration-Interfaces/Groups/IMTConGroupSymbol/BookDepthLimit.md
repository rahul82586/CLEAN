[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / BookDepthLimit

[Previous](PermissionsFlags.md) | [Next](../IMTConGroupArray.md)

# IMTConSymbol::BookDepthLimit

Get a limit on the number of orders in the Market Depth window displayed for this particular group.

C++
    
    
    UINT  IMTConSymbol::BookDepthLimit()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSymbol.BookDepthLimit()

Python (Manager API)
    
    
    MTConSymbol.BookDepthLimit

### Return Value

The number of orders in the Market Depth window allowed for this group. The value of 0 means that the depth limit corresponds to appropriate symbol settings ([IMTConSymbol::TickBookDepth](../../Symbols/IMTConSymbol/TickBookDepth.md)).

# IMTConSymbol::BookDepthLimit

Set a limit on the number of orders in the Market Depth window displayed for this particular group.

C++
    
    
    MTAPIRES  IMTConSymbol::BookDepthLimit(
       const UINT  depth      // Depth value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.BookDepthLimit(
       uint        depth      // Depth value
       )

Python (Manager API)
    
    
    MTConSymbol.BookDepthLimit

### Parameters

**depth**  
[in] The number of orders in the Market Depth window allowed for this group. The value of 0 means that the depth limit corresponds to appropriate symbol settings (IMTConSymbol::TickBookDepth).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
