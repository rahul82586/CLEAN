[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / SwapShort

[Previous](SwapLong.md) | [Next](Swap3Day.md)

# IMTConSymbol::SwapShort

Get the swap size for short positions.

C++
    
    
    double  IMTConSymbol::SwapShort()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConSymbol.SwapShort()

Python (Manager API)
    
    
    MTConSymbol.SwapShort

### Return Value

The swap size for short positions.

### Note

Swap units depend on their calculation mode ([IMTConSymbol::SwapMode](SwapMode.md)).

# IMTConSymbol::SwapShort

Set the swap size for short positions.

C++
    
    
    MTAPIRES  IMTConSymbol::SwapShort(
       const double  swap      // Swap amount
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.SwapShort(
       double        swap      // Swap amount
       )

Python (Manager API)
    
    
    MTConSymbol.SwapShort

### Parameters

**swap**  
[in] The swap size for short positions.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Swap units depend on their calculation mode ([IMTConSymbol::SwapMode](SwapMode.md)).
