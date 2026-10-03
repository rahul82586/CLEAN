[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoParam](../IMTConAutoParam.md) / ValueDate

[Previous](ValueTime.md) | [Next](ValuePercent.md)

# IMTConAutoParam::ValueDate

Get the value of the parameter that expresses the date.

C++
    
    
    INT64  IMTConAutoParam::ValueDate()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConAutoParam.ValueDate()

Python
    
    
    MTConAutoParam.ValueDate

### Return Value

Date in seconds since 01.01.1970 (00:00 of the specified day).

# IMTConAutoParam::ValueDate

Set the value of the parameter that expresses date and time.

C++
    
    
    MTAPIRES  IMTConAutoParam::ValueDate(
       const INT64  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoParam.ValueDate(
       long         value      // Value
       )

Python
    
    
    MTConAutoParam.ValueDate

### Parameters

**value**  
[in] Date in seconds since 01.01.1970 (00:00 of the specified day).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
