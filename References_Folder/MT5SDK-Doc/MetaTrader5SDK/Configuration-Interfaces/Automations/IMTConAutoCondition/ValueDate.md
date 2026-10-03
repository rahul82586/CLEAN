[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoCondition](../IMTConAutoCondition.md) / ValueDate

[Previous](ValueTime.md) | [Next](ValuePercent.md)

# IMTConAutoCondition::ValueDate

Get a condition value expressing a date.

C++
    
    
    INT64  IMTConAutoCondition::ValueDate()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConAutoCondition.ValueDate()

Python
    
    
    MTConAutoCondition.ValueDate

### Return Value

Date in seconds since 01.01.1970 (00:00 of the specified day).

# IMTConAutoCondition::ValueDate

Set a condition value that expresses date and time.

C++
    
    
    MTAPIRES  IMTConAutoCondition::ValueDate(
       const INT64  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoCondition.ValueDate(
       long         value      // Value
       )

Python
    
    
    MTConAutoCondition.ValueDate

### Parameters

**value**  
[in] Date in seconds since 01.01.1970 (00:00 of the specified day).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
