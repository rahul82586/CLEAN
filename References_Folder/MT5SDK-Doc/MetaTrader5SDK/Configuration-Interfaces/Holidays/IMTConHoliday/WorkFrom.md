[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Holidays](../../Holidays.md) / [IMTConHoliday](../IMTConHoliday.md) / WorkFrom

[Previous](Day.md) | [Next](WorkFromHours.md)

# IMTConHoliday::WorkFrom

Get the beginning of the range of the server working time on a holiday.

C++
    
    
    UINT  IMTConHoliday::WorkFrom()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConHoliday.WorkFrom()

Python (Manager API)
    
    
    MTConHoliday.WorkFrom

### Return Value

The beginning of the range of the server working time on a holiday, in minutes elapsed since 00:00. For example, 100 denotes 01:40.

# IMTConHoliday::WorkFrom

Set the beginning of the range of the server working time on a holiday.

C++
    
    
    MTAPIRES  IMTConHoliday::WorkFrom(
       const UINT  from      // Beginning of the range
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConHoliday.WorkFrom(
       uint        from      // Beginning of the range
       )

Python (Manager API)
    
    
    MTConHoliday.WorkFrom

### Parameters

**from**  
[in] The beginning of the range of the server working time in minutes elapsed since 00:00. For example, 100 denotes 01:40.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
