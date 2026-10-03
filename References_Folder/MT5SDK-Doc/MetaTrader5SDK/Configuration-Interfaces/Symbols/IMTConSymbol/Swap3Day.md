[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / Swap3Day

[Previous](SwapShort.md) | [Next](SwapYearDays.md)

# IMTConSymbol::Swap3Day

Get the triple swap day.

C++
    
    
    UINT  IMTConSymbol::Swap3Day()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSymbol.Swap3Day()

### Return Value

The triple swap day as a value from the [IMTConSymbol::EnSwapDays (#enswapdays)](Enumerations.md#enswapdays) enumeration.

# IMTConSymbol::Swap3Day

Set the triple swap day.

C++
    
    
    MTAPIRES  IMTConSymbol::Swap3Day(
       const UINT  day      // Triple-swap day
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.Swap3Day(
       uint        day      // Triple-swap day
       )

### Parameters

**day**  
[in] Triple swap day. Passed as a value from theIMTConSymbol::EnSwapDaysenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method is obsolete and is no longer used. To set a triple swap day, use the [IMTConSymbol::SwapRate*](SwapRateSunday.md) methods.
