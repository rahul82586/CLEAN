[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Holidays](../../Holidays.md) / [IMTConHoliday](../IMTConHoliday.md) / Mode

[Previous](Description.md) | [Next](Year.md)

# IMTConHoliday::Mode

Get the state of a holiday.

C++
    
    
    UINT  IMTConHoliday::Mode()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConHoliday.Mode()

Python (Manager API)
    
    
    MTConHoliday.Mode

### Return Value

One of the values of the [IMTConHoliday::EnHolidayMode (#enholidaymode)](Enumerations.md#enholidaymode) enumeration.

# IMTConHoliday::Mode

Set the state of a holiday.

C++
    
    
    MTAPIRES  IMTConHoliday::Mode(
       const UINT  mode      // State of a holiday
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConHoliday.Mode(
       UINT        mode      // State of a holiday
       )

Python (Manager API)
    
    
    MTConHoliday.Mode

### Parameters

**mode**  
[in] The state of a holiday. The state is passed using theIMTConHoliday::EnHolidayModeenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
