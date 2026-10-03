[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Holidays](../../Holidays.md) / [IMTConHoliday](../IMTConHoliday.md) / WorkToHours

[Previous](WorkTo.md) | [Next](WorkToMinutes.md)

# IMTConHoliday::WorkToHours

Get the number of hours in the end of the range of the server working time.

C++
    
    
    UINT  IMTConHoliday::WorkToHours()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConHoliday.WorkToHours()

Python (Manager API)
    
    
    MTConHoliday.WorkToHours

### Return Value

The number of hours in the end of the range of the server working time.

### Note

For example, if the [IMTConHoliday::WorkTo](WorkTo.md) method returns the value 100, the IMTConHoliday::WorkToHours will return 1 (the number of hours for 01:40).
