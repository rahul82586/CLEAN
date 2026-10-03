[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / Swap3Day

[Previous](SwapShortDefault.md) | [Next](Swap3DayDefault.md)

# IMTConGroupSymbol::Swap3Day

Get the day to charge triple swap for a symbol for this group.

C++
    
    
    INT  IMTConGroupSymbol::Swap3Day()  const

.NET (Gateway/Manager API)
    
    
    int  CIMTConGroupSymbol.Swap3Day()

### Return Value

The triple swap day as a value from the [IMTConSymbol::EnSwapDays (#enswapdays)](../../Symbols/IMTConSymbol/Enumerations.md#enswapdays) enumeration.

# IMTConGroupSymbol::Swap3Day

Set the day to charge triple swap for a symbol for this group.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::Swap3Day(
       const INT  day      // Triple-swap day
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.Swap3Day(
       int        day      // Triple-swap day
       )

### Parameters

**day**  
[in] Triple swap day. Passed as a value from theIMTConSymbol::EnSwapDaysenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method is obsolete and is no longer used. To set a triple swap day, use the [IMTConGroupSymbol::SwapRate*](SwapRateSunday.md) methods.
