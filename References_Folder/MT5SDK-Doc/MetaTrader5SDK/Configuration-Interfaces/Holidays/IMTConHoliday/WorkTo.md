[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Holidays](../../Holidays.md) / [IMTConHoliday](../IMTConHoliday.md) / WorkTo

[Previous](WorkFromMinutes.md) | [Next](WorkToHours.md)

# IMTConHoliday::WorkTo

Get the end of the range of the server working time on a holiday.

C++
    
    
    UINT  IMTConHoliday::WorkTo()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConHoliday.WorkTo()

Python (Manager API)
    
    
    MTConHoliday.WorkTo

### Return Value

The end of the range of the server working time on a holiday, in minutes elapsed since 00:00. For example, 100 denotes 01:40.

# IMTConHoliday::WorkTo

Set the end of the range of the server working time on a holiday.

C++
    
    
    MTAPIRES  IMTConHoliday::WorkTo(
       const UINT  from      // End of the range
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConHoliday.WorkTo(
       uint        from      // End of the range
       )

Python (Manager API)
    
    
    MTConHoliday.WorkTo

### Parameters

**from**  
[in] The end of the range of the server working time in minutes elapsed since 00:00. For example, 100 denotes 01:40.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
