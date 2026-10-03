[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerTrade](../IMTConServerTrade.md) / OvermonthTimePrev

[Previous](OvermonthTimeLast.md) | [Next](LoginsRangeAdd.md)

# IMTConServerTrade::OvermonthTimePrev

Get the time of the last but one transition to the next month.

C++
    
    
    INT64  IMTConServerTrade::OvermonthTimePrev()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConServerTrade.OvermonthTimePrev()

Python (Manager API)
    
    
    MTConServerTrade.OvermonthTimePrev

### Return Value

Time of the last but one transition to the next month - number of seconds elapsed since 01.01.1970.
