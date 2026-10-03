[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Holidays](../../Holidays.md) / [IMTConHoliday](../IMTConHoliday.md) / WorkFromMinutes

[Previous](WorkFromHours.md) | [Next](WorkTo.md)

# IMTConHoliday::WorkFromMinutes

Get the number of minutes in the beginning of the range of the server working time.

C++
    
    
    UINT  IMTConHoliday::WorkFromMinutes()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConHoliday.WorkFromMinutes()

Python (Manager API)
    
    
    MTConHoliday.WorkFromMinutes

### Return Value

The number of minutes in the beginning of the range of the server working time.

### Note

For example, if the [IMTConHoliday::WorkFrom](WorkFrom.md) method returns , the IMTConHoliday::WorkFromMinutes will return 40 (the number of minutes for 01:40).
