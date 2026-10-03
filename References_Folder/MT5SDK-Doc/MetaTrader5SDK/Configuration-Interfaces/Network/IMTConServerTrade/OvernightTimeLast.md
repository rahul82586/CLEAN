[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerTrade](../IMTConServerTrade.md) / OvernightTimeLast

[Previous](OvernightTime.md) | [Next](OvernightTimePrev.md)

# IMTConServerTrade::OvernightTimeLast

Get the time of the last transition to the next day.

C++
    
    
    INT64  IMTConServerTrade::OvernightTimeLast()  const

.NET (Gateway/Manager API)s
    
    
    long  CIMTConServerTrade.OvernightTimeLast()

Python (Manager API)
    
    
    MTConServerTrade.OvernightTimeLast

### Return Value

Time of the last transition to the next day - number of seconds elapsed since 01.01.1970.
