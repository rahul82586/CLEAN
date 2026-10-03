[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / SessionQuoteClear

[Previous](SessionQuoteDelete.md) | [Next](SessionQuoteShift.md)

# IMTConSymbol::SessionQuoteClear

Clear the list of quoting sessions of a symbol.

C++
    
    
    MTAPIRES  IMTConSymbol::SessionQuoteClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.SessionQuoteClear()

Python (Manager API)
    
    
    MTConSymbol.SessionQuoteClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
