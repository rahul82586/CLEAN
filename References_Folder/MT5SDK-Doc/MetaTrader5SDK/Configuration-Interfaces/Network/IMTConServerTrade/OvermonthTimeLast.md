[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerTrade](../IMTConServerTrade.md) / OvermonthTimeLast

[Previous](OvermonthMode.md) | [Next](OvermonthTimePrev.md)

# IMTConServerTrade::OvermonthTimeLast

Get the time of the last transition to the next month.

C++
    
    
    INT64  IMTConServerTrade::OvermonthTimeLast()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConServerTrade.OvermonthTimeLast()

Python (Manager API)
    
    
    MTConServerTrade.OvermonthTimeLast

### Return Value

Time of the last transition to the next month - number of seconds elapsed since 01.01.1970.
