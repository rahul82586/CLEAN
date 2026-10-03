[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / SessionQuoteUpdate

[Previous](SessionQuoteAdd.md) | [Next](SessionQuoteDelete.md)

# IMTConSymbol::SessionQuoteUpdate

Update a quoting session of a symbol by the day and index.

C++
    
    
    MTAPIRES  IMTConSymbol::SessionQuoteUpdate(
       const UINT                  wday,        // Day of the week
       const UINT                  pos,         // The position of a session
       const IMTConSymbolSession*  session      // An object of the session
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.SessionQuoteUpdate(
       uint                        wday,        // Day of the week
       uint                        pos,         // The position of a session
       CIMTConSymbolSession        session      // An object of the session
       )

Python (Manager API)
    
    
    MTConSymbol.SessionQuoteUpdate(
       wday,                       # Day of the week
       pos,                        # The position of a session
       session                     # An object of the session
       )
    
    
    MTConSymbol.SessionQuoteSet()

### Parameters

**wday**  
[in] The day of the week in which the quoting session is updated. The day is specified by a value 0 (Sunday) to 6 (Saturday).

**pos**  
[in] The position of a quoting session in the specified day starting with 0.

**session**  
[in] An object of the session.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
