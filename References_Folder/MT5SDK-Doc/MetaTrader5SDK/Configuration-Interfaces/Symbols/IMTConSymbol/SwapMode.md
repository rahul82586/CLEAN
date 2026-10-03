[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / SwapMode

[Previous](MarginRateLiquidity.md) | [Next](SwapLong.md)

# IMTConSymbol::SwapMode

Get the swap calculation mode for a symbol.

C++
    
    
    UINT  IMTConSymbol::SwapMode()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSymbol.SwapMode()

Python (Manager API)
    
    
    MTConSymbol.SwapMode

### Return Value

One of the values of the [IMTConSymbol::EnSwapMode (#enswapmode)](Enumerations.md#enswapmode) enumeration.

### Note

The swap size is specified using the [IMTConSymbol::SwapLong](SwapLong.md) and [IMTConSymbol::SwapShort](SwapShort.md) methods.

# IMTConSymbol::SwapMode

Set the swap calculation mode.

C++
    
    
    MTAPIRES  IMTConSymbol::SwapMode(
       const UINT  mode      // Swap mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.SwapMode(
       uint        mode      // Swap mode
       )

Python (Manager API)
    
    
    MTConSymbol.SwapMode

### Parameters

**mode**  
[in] To pass the swap calculation mode, theIMTConSymbol::EnSwapModeenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The swap size is specified using the [IMTConSymbol::SwapLong](SwapLong.md) and [IMTConSymbol::SwapShort](SwapShort.md) methods.
