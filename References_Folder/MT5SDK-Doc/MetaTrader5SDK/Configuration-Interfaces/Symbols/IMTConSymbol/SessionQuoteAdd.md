[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / SessionQuoteAdd

[Previous](TimeExpiration.md) | [Next](SessionQuoteUpdate.md)

# IMTConSymbol::SessionQuoteAdd

Add a quoting session for a symbol.

C++
    
    
    MTAPIRES  IMTConSymbol::SessionQuoteAdd(
       const UINT            wday,        // A day of the week
       IMTConSymbolSession*  session      // A session object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.SessionQuoteAdd(
       uint                  wday,        // A day of the week
       CIMTConSymbolSession  session      // A session object
       )

Python (Manager API)
    
    
    MTConSymbol.SessionQuoteAdd(
       wday,                 # A day of the week
       session               # A session object
       )

### Parameters

**wday**  
[in] The day of the week, for which the quoting session is being added. The day is specified by a value 0 (Sunday) to 6 (Saturday).

**session**  
[in] An object of the session.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
