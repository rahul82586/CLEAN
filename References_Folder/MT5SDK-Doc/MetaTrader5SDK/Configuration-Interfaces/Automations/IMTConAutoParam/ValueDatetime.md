[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoParam](../IMTConAutoParam.md) / ValueDatetime

[Previous](ValueVolume.md) | [Next](ValueLeverage.md)

# IMTConAutoParam::ValueDatetime

Get the value of the parameter that expresses date and time.

C++
    
    
    INT64  IMTConAutoParam::ValueDatetime()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConAutoParam.ValueDatetime()

Python
    
    
    MTConAutoParam.ValueDatetime

### Return Value

Date and time in seconds elapsed since 01.01.1970.

# IMTConAutoParam::ValueDatetime

Set the value of the parameter that expresses date and time.

C++
    
    
    MTAPIRES  IMTConAutoParam::ValueDatetime(
       const INT64  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoParam.ValueDatetime(
       long         value      // Value
       )

Python
    
    
    MTConAutoParam.ValueDatetime

### Parameters

**value**  
[in] Date and time in seconds elapsed since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
