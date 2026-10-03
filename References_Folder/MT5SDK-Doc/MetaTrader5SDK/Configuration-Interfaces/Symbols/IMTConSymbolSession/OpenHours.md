[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbolSession](../IMTConSymbolSession.md) / OpenHours

[Previous](Open.md) | [Next](OpenMinutes.md)

# IMTConSymbolSession::OpenHours

Get the number of hours in the opening time of trading or quoting session of a symbol.

C++
    
    
    UINT  IMTConSymbolSession::OpenHours()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSymbolSession.OpenHours()

Python (Manager API)
    
    
    MTConSymbolSession.OpenHours

### Return Value

The number of hours in the opening time of trading or quoting session of a symbol.

### Note

For example, if the [IMTConSymbolSession::Open](Open.md) method returns the value 100, the IMTConSymbolSession::OpenHours will return 1 (the number of hours for 01:40).
