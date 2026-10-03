[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Holidays](../../Holidays.md) / [IMTConHoliday](../IMTConHoliday.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConHoliday::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConHoliday::Assign(
       const IMTConHoliday*  holiday      // Source objects
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConHoliday.Assign(
       CIMTConHoliday        holiday      // Source objects
       )

### Parameters

**holiday**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
