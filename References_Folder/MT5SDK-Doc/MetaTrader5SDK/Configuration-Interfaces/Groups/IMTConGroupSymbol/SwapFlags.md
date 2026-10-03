[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / SwapFlags

[Previous](SwapYearDaysDefault.md) | [Next](SwapFlagsDefault.md)

# IMTConGroupSymbol::SwapFlags

Get additional symbol swap settings for the given group.

C++
    
    
    UINT  IMTConGroupSymbol::SwapFlags()  const

.NET (Gateway/Manager API)
    
    
    EnSwapFlags  CIMTConGroupSymbol.SwapFlags()

Python (Manager API)
    
    
    MTConGroupSymbol.SwapFlags

### Return Value

The [IMTConSymbol::EnSwapFlags (#enswapflags)](../../Symbols/IMTConSymbol/Enumerations.md#enswapflags) enumeration is used to pass the settings.

# IMTConGroupSymbol::SwapFlags

Set additional symbol swap settings for the given group.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::SwapFlags(
       const UINT    flags      // Settings flags
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.SwapFlags(
       EnSwapFlags   flags      // Settings flags
       )

Python (Manager API)
    
    
    MTConGroupSymbol.SwapFlags

### Parameters

**flags**  
[in] TheIMTConSymbol::EnSwapFlagsenumeration is used to pass the settings.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, a response code describing the error is returned.
