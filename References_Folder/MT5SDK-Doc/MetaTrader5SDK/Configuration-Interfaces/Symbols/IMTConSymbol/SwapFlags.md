[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / SwapFlags

[Previous](SwapYearDays.md) | [Next](SwapRateSunday.md)

# IMTConSymbol::SwapFlags

Get additional swap settings.

C++
    
    
    UINT  IMTConSymbol::SwapFlags()  const

.NET (Gateway/Manager API)
    
    
    EnSwapFlags  CIMTConSymbol.SwapFlags()

Python (Manager API)
    
    
    MTConSymbol.SwapFlags

### Return Value

The [IMTConSymbol::EnSwapFlags (#enswapflags)](Enumerations.md#enswapflags) enumeration is used to pass the settings.

# IMTConSymbol::SwapFlags

Set additional swap settings.

C++
    
    
    MTAPIRES  IMTConSymbol::SwapFlags(
       const UINT    flags      // Settings flags
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.SwapFlags(
       EnSwapFlags   flags      // Settings flags
       )

Python (Manager API)
    
    
    MTConSymbol.SwapFlags

### Parameters

**flags**  
[in] TheIMTConSymbol::EnSwapFlagsenumeration is used to pass the settings.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, a response code describing the error is returned.
