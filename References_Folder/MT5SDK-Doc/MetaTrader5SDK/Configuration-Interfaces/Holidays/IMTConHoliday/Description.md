[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Holidays](../../Holidays.md) / [IMTConHoliday](../IMTConHoliday.md) / Description

[Previous](Clear.md) | [Next](Mode.md)

# IMTConHoliday::Description

Get the description of a holiday.

C++
    
    
    LPCWSTR  IMTConHoliday::Description()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConHoliday.Description()

Python (Manager API)
    
    
    MTConHoliday.Description

### Return Value

If successful, it returns a pointer to a string with the description of a holiday. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConHoliday](../IMTConHoliday.md) object.

# IMTConHoliday::Description

Set the description of a holiday.

C++
    
    
    MTAPIRES  IMTConHoliday::Description(
       LPCWSTR  descr      // Holiday description
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConHoliday.Description(
       string   descr      // Holiday description
       )

Python (Manager API)
    
    
    MTConHoliday.Description

### Parameters

**descr**  
[in] Description of a holiday.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum description length is 128 characters (with the sign of the string end). If a string of a greater length is assigned, it will be cut to this length.
