[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Holidays](../../Holidays.md) / [IMTConHoliday](../IMTConHoliday.md) / Month

[Previous](Year.md) | [Next](Day.md)

# IMTConHoliday::Month

Get the month of a holiday.

C++
    
    
    UINT  IMTConHoliday::Month()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConHoliday.Month()

Python (Manager API)
    
    
    MTConHoliday.Month

### Return Value

The month of a holiday.

### Note

Months are passed using values from 1 (January) to 12 (December).

# IMTConHoliday::Month

Set the month of a holiday.

C++
    
    
    MTAPIRES  IMTConHoliday::Month(
       const UINT  month      // Month of a holiday
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConHoliday.Month(
       UINT        month      // Month of a holiday
       )

Python (Manager API)
    
    
    MTConHoliday.Month

### Parameters

**month**  
[in] The month of a holiday. Months are passed using values from 1 (January) to 12 (December).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
