[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / SessionTradeClear

[Previous](SessionTradeDelete.md) | [Next](SessionTradeShift.md)

# IMTConSymbol::SessionTradeClear

Clear the list of all trading sessions of a symbol.

C++
    
    
    MTAPIRES  IMTConSymbol::SessionTradeClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.SessionTradeClear()

Python (Manager API)
    
    
    MTConSymbol.SessionTradeClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
