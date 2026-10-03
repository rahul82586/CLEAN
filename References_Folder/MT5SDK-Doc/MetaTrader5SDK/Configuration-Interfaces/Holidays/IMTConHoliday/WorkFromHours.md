[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Holidays](../../Holidays.md) / [IMTConHoliday](../IMTConHoliday.md) / WorkFromHours

[Previous](WorkFrom.md) | [Next](WorkFromMinutes.md)

# IMTConHoliday::WorkFromHours

Get the number of hours in the beginning of the range of the server working time.

C++
    
    
    UINT  IMTConHoliday::WorkFromHours()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConHoliday.WorkFromHours()

Python (Manager API)
    
    
    MTConHoliday.WorkFromHours

### Return Value

The number of hours in the beginning of the range of the server working time.

### Note

For example, if the [IMTConHoliday:WorkFrom](WorkFrom.md) method returns 100, the IMTConHoliday::WorkFromHours will return 1 (the number of hours for 01:40).
