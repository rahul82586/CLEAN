[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / SwapMode

[Previous](MarginHedgedDefault.md) | [Next](SwapModeDefault.md)

# IMTConGroupSymbol::SwapMode

Get the swap calculation mode for a certain symbol for the group.

C++
    
    
    UINT  IMTConGroupSymbol::SwapMode()  const

.NET (Gateway/Manager API)
    
    
    EnSwapMode  CIMTConGroupSymbol.SwapMode()

Python (Manager API)
    
    
    MTConGroupSymbol.SwapMode

### Return Value

One of the values of the [IMTConSymbol::EnSwapMode (#enswapmode)](../../Symbols/IMTConSymbol/Enumerations.md#enswapmode) enumeration.

# IMTConGroupSymbol::SwapMode

Set the swap calculation mode for a certain symbol for the group.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::SwapMode(
       const UINT  mode      // Swap calculation mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.SwapMode(
       EnSwapMode  mode      // Swap calculation mode
       )

Python (Manager API)
    
    
    MTConGroupSymbol.SwapMode

### Parameters

**mode**  
[in] To pass the swap calculation mode, theIMTConSymbol::EnSwapModeenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

To use basic swap settings for the group, you should specify default values for all parameters, including SwapMode, SwapLong, SwapShort, Swap3Day and SwapYearDays. Thus, setting a default value for SwapMode alone is not enough.
