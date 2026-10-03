[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoCondition](../IMTConAutoCondition.md) / ValueDatetime

[Previous](ValueVolume.md) | [Next](ValueLeverage.md)

# IMTConAutoCondition::ValueDatetime

Get a condition value expressing date and time.

C++
    
    
    INT64  IMTConAutoCondition::ValueDatetime()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConAutoCondition.ValueDatetime()

Python
    
    
    MTConAutoCondition.ValueDatetime

### Return Value

Date and time in seconds elapsed since 01.01.1970.

# IMTConAutoCondition::ValueDatetime

Set a condition value that expresses date and time.

C++
    
    
    MTAPIRES  IMTConAutoCondition::ValueDatetime(
       const INT64  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoCondition.ValueDatetime(
       long         value      // Value
       )

Python
    
    
    MTConAutoCondition.ValueDatetime

### Parameters

**value**  
[in] Date and time in seconds elapsed since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
