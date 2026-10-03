[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / SwapLong

[Previous](SwapModeDefault.md) | [Next](SwapLongDefault.md)

# IMTConGroupSymbol::SwapLong

Get the long position swap for a symbol for the group.

C++
    
    
    double  IMTConGroupSymbol::SwapLong()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConGroupSymbol.SwapLong()

Python (Manager API)
    
    
    MTConGroupSymbol.SwapLong

### Return Value

The long position swap for a symbol for the group.

### Note

Swap units depend on their calculation mode.

# IMTConGroupSymbol::SwapLong

Set the long position swap for a symbol for the group.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::SwapLong(
       const double  swap      // Swap amount
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.SwapLong(
       double        swap      // Swap amount
       )

Python (Manager API)
    
    
    MTConGroupSymbol.SwapLong

### Parameters

**swap**  
[in] The long position swap for a symbol for the group.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Swap units depend on their calculation mode.
