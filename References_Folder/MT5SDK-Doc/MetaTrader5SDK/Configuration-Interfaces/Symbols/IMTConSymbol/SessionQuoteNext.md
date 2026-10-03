[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / SessionQuoteNext

[Previous](SessionQuoteTotal.md) | [Next](SessionTradeAdd.md)

# IMTConSymbol::SessionQuoteNext

Get a quoting session of a symbol by the day and index.

C++
    
    
    MTAPIRES  IMTConSymbol::SessionQuoteNext(
       const UINT            wday,        // A day of the week
       const UINT            pos,         // The position of a session
       IMTConSymbolSession*  session      // A session object
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.SessionQuoteNext(
       uint                  wday,        // A day of the week
       uint                  pos,         // The position of a session
       CIMTConSymbolSession  session      // A session object
       )

Python (Manager API)
    
    
    MTConSymbol.SessionQuoteNext(
       wday,                 # A day of the week
       pos                   # The position of a session
       )
    
    
    MTConSymbol.SessionQuoteGet()

### Parameters

**wday**  
[in] The day of the week to get a quoting session. The day is specified by a value 0 (Sunday) to 6 (Saturday).

**pos**  
[in] The position of a quoting session in the specified day starting with 0.

**session**  
[out] An object of the session. The session object must be first created using theIMTAdminAPI::SymbolSessionCreateorIMTManagerAPI::SymbolSessionCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
