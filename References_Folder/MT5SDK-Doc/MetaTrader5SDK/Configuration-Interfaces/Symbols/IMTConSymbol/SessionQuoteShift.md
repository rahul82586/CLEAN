[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / SessionQuoteShift

[Previous](SessionQuoteClear.md) | [Next](SessionQuoteTotal.md)

# IMTConSymbol::SessionQuoteShift

Move a quoting session of a symbol.

C++
    
    
    MTAPIRES  IMTConSymbol::SessionQuoteShift(
       const UINT  wday,      // Day of the week
       const UINT  pos,       // The session position
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.SessionQuoteShift(
       uint        wday,      // Day of the week
       uint        pos,       // The session position
       int         shift      // Shift
       )

Python (Manager API)
    
    
    MTConSymbol.SessionQuoteShift(
       wday,       # Day of the week
       pos,        # The session position
       shift       # Shift
       )

### Parameters

**wday**  
[in] The day of the week in which the quoting session is moved. The day is specified by a value 0 (Sunday) to 6 (Saturday).

**pos**  
[in] The position of a quoting session in the specified day starting with 0.

**shift**  
Shift of a session relative to its current position. A negative value means the shift to the top of the list, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
