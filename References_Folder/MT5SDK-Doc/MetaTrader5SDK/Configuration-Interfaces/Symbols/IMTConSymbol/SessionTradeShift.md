[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / SessionTradeShift

[Previous](SessionTradeClear.md) | [Next](SessionTradeTotal.md)

# IMTConSymbol::SessionTradeShift

Move a trading session of a symbol.

C++
    
    
    MTAPIRES  IMTConSymbol::SessionTradeShift(
       const UINT  wday,      // Day of the week
       const UINT  pos,       // The session position
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.SessionTradeShift(
       uint        wday,      // Day of the week
       uint        pos,       // The session position
       int         shift      // Shift
       )

Python (Manager API)
    
    
    MTConSymbol.SessionTradeShift(
       wday,       # Day of the week
       pos,        # The session position
       shift       # Shift
       )

### Parameters

**wday**  
[in] The day of the week in which the trading session is moved. The day is specified by a value 0 (Sunday) to 6 (Saturday).

**pos**  
[in] The position of a trading session in the specified day starting with 0.

**shift**  
Shift of a session relative to its current position. A negative value means the shift to the top of the list, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
