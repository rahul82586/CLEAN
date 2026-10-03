[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / SwapShort

[Previous](SwapLongDefault.md) | [Next](SwapShortDefault.md)

# IMTConGroupSymbol::SwapShort

Get the short position swap for a symbol for the group.

C++
    
    
    double  IMTConGroupSymbol::SwapShort()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConGroupSymbol.SwapShort()

Python (Manager API)
    
    
    MTConGroupSymbol.SwapShort

### Return Value

The short position swap for a symbol for the group.

### Note

Swap units depend on their calculation mode.

# IMTConGroupSymbol::SwapShort

Sets the short position swap on a symbol for the group.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::SwapShort(
       const double  swap      // Swap amount
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.SwapShort(
       double        swap      // Swap amount
       )

Python (Manager API)
    
    
    MTConGroupSymbol.SwapShort

### Parameters

**swap**  
[in] The short position swap for a symbol for the group.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Swap units depend on their calculation mode.
