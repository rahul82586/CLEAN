[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / SwapLong

[Previous](SwapMode.md) | [Next](SwapShort.md)

# IMTConSymbol::SwapLong

Get the swap size for long positions.

C++
    
    
    double  IMTConSymbol::SwapLong()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConSymbol.SwapLong()

Python (Manager API)
    
    
    MTConSymbol.SwapLong

### Return Value

The swap size for long positions.

### Note

Swap units depend on their calculation mode ([IMTConSymbol::SwapMode](SwapMode.md)).

# IMTConSymbol::SwapLong

Set the swap size for long positions.

C++
    
    
    MTAPIRES  IMTConSymbol::SwapLong(
       const double  swap      // Swap amount
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.SwapLong(
       double        swap      // Swap amount
       )

Python (Manager API)
    
    
    MTConSymbol.SwapLong

### Parameters

**swap**  
[in] The swap size for long positions.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Swap units depend on their calculation mode ([IMTConSymbol::SwapMode](SwapMode.md)).
