[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Time](../../Time.md) / [IMTConTime](../IMTCon.md) / IMTCon DaylightState

[Previous](IMTCon-Daylight.md) | [Next](../IMTConSink.md)

# IMTConTime::DaylightState

Get data on the presence of the daylight saving time in the platform time zone.

C++
    
    
    int  IMTConTime::DaylightState()  const

.NET (Gateway/Manager API)
    
    
    int  CIMTConTime.DaylightState()

Python (Manager API)
    
    
    MTConTime.DaylightState

### Return Value

0 means no daylight saving time is applied in the platform time zone. Otherwise, any non-zero value is used.

  * If the daylight saving time is enabled in MetaTrader 5, the platform shifts time within an hour (during an hourly synchronization) after the time shift has occurred in Windows. The platform aligns itself with time shift values stored in the OS time zone.
  * If the daylight saving time is disabled in MetaTrader 5, the platform does not perform a time shift.
  * If the daylight saving time is enabled in MetaTrader 5 but there are no time shift values set in the OS time zone, the platform does not perform a time shift, since it has no data to align itself with.


