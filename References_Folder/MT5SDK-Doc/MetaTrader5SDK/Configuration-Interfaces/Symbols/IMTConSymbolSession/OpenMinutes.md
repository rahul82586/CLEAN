[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbolSession](../IMTConSymbolSession.md) / OpenMinutes

[Previous](OpenHours.md) | [Next](Close.md)

# IMTConSymbolSession::OpenMinutes

Get the number of minutes in the opening time of trading or quoting session of a symbol.

C++
    
    
    UINT  IMTConSymbolSession::OpenMinutes()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSymbolSession.OpenMinutes()

Python (Manager API)
    
    
    MTConSymbolSession.OpenMinutes

### Return Value

The number of minutes in the opening time of trading or quoting session of a symbol.

### Note

For example, if the [IMTConSymbolSession::Open](Open.md) method returns the value 100, the IMTConSymbolSession::OpenMinutes will return 40 (the number of minutes for 01:40).
