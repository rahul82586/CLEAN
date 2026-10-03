[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / SessionQuoteTotal

[Previous](SessionQuoteShift.md) | [Next](SessionQuoteNext.md)

# IMTConSymbol::SessionQuoteTotal

Get the number of symbol quoting sessions for a specified day.

C++
    
    
    UINT  IMTConSymbol::SessionQuoteTotal(
       const UINT  wday      // Day of the week
       )  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSymbol.SessionQuoteTotal(
       uint        wday      // Day of the week
       )

Python (Manager API)
    
    
    MTConSymbol.SessionQuoteTotal()

### Parameters

**wday**  
[in] The day of the week to get the number of quoting sessions. The day is specified by a value 0 (Sunday) to 6 (Saturday).

### Return Value

The number of symbol quoting sessions for a specified day.
