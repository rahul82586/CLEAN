[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbolSession](../IMTConSymbolSession.md) / CloseMinutes

[Previous](CloseHours.md) | [Next](../IMTConSymbolArray.md)

# IMTConSymbolSession::CloseMinutes

Get the number of minutes in the closing time of trading or quoting session of a symbol.

C++
    
    
    UINT  IMTConSymbolSession::CloseMinutes()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSymbolSession.CloseMinutes()

Python (Manager API)
    
    
    MTConSymbolSession.CloseMinutes

### Return Value

The number of minutes in the closing time of trading or quoting session of a symbol.

### Note

For example, if the [IMTConSymbolSession::Close](Close.md) method returns the value 100, the IMTConSymbolSession::CloseMinutes will return 40 (the number of minutes for 01:40).
