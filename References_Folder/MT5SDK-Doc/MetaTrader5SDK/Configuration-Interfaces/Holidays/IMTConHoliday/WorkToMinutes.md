[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Holidays](../../Holidays.md) / [IMTConHoliday](../IMTConHoliday.md) / WorkToMinutes

[Previous](WorkToHours.md) | [Next](SymbolAdd.md)

# IMTConHoliday::WorkToMinutes

Get the number of minutes in the end of the range of the server working time.

C++
    
    
    UINT  IMTConHoliday::WorkToMinutes()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConHoliday.WorkToMinutes()

Python (Manager API)
    
    
    MTConHoliday.WorkToMinutes

### Return Value

The number of minutes in the end of the range of the server working time.

### Note

For example, if the [IMTConHoliday::WorkTo](WorkTo.md) method returns , the IMTConHoliday::WorkToMinutes will return 40 (the number of minutes for 01:40).
