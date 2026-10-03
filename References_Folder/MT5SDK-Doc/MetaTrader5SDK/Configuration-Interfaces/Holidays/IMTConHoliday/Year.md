[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Holidays](../../Holidays.md) / [IMTConHoliday](../IMTConHoliday.md) / Year

[Previous](Mode.md) | [Next](Month.md)

# IMTConHoliday::Year

Get the year of a holiday.

C++
    
    
    UINT  IMTConHoliday::Year()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConHoliday.Year()

Python (Manager API)
    
    
    MTConHoliday.Year

### Return Value

The year of a holiday.

### Note

The 0 value means that the holiday is annual.

# IMTConHoliday::Year

Set the year of a holiday.

C++
    
    
    MTAPIRES  IMTConHoliday::Year(
       const UINT  year      // The year of a holiday
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConHoliday.Year(
       uint        year      // The year of a holiday
       )

Python (Manager API)
    
    
    MTConHoliday.Year

### Parameters

**year**  
[in] The year of a holiday, e.g. 2010. If the 0 value is set, the holiday will be annual.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
