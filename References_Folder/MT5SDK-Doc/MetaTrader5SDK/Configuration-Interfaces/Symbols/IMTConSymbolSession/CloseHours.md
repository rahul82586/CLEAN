[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbolSession](../IMTConSymbolSession.md) / CloseHours

[Previous](Close.md) | [Next](CloseMinutes.md)

# IMTConSymbolSession::CloseHours

Get the number of hours in the closing time of trading or quoting session of a symbol.

C++
    
    
    UINT  IMTConSymbolSession::CloseHours()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSymbolSession.CloseHours()

Python (Manager API)
    
    
    MTConSymbolSession.CloseHours

### Return Value

The number of hours in the closing time of trading or quoting session of a symbol.

### Note

For example, if the [IMTConSymbolSession::Close](Close.md) method returns the value 100, the IMTConSymbolSession::CloseHours will return 1 (the number of hours for 01:40).
