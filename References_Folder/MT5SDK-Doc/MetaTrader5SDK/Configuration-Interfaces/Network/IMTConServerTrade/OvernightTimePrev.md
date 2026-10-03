[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerTrade](../IMTConServerTrade.md) / OvernightTimePrev

[Previous](OvernightTimeLast.md) | [Next](OvernightDays.md)

# IMTConServerTrade::OvernightTimePrev

Get the time of the last but one transition to the next day.

C++
    
    
    INT64  IMTConServerTrade::OvernightTimePrev()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConServerTrade.OvernightTimePrev()

Python (Manager API)
    
    
    MTConServerTrade.OvernightTimePrev

### Return Value

Time of the last but one transition to the next day - number of seconds elapsed since 01.01.1970.
