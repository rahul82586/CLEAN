[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoCondition](../IMTConAutoCondition.md) / ValueTime

[Previous](ValueBool.md) | [Next](ValueDate.md)

# IMTConAutoCondition::ValueTime

Get a condition value expressing the time.

C++
    
    
    UINT  IMTConAutoCondition::ValueTime()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConAutoCondition.ValueTime()

Python
    
    
    MTConAutoCondition.ValueTime

### Return Value

Time in minutes elapsed since 00:00.

# IMTConAutoCondition::ValueTime

Set a condition value expressing the time.

C++
    
    
    MTAPIRES  IMTConAutoCondition::ValueTime(
       const UINT  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoCondition.ValueTime(
       uint        value      // Value
       )

Python
    
    
    MTConAutoCondition.ValueTime

### Parameters

**value**  
[in] A value in minutes elapsed since 00:00.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
