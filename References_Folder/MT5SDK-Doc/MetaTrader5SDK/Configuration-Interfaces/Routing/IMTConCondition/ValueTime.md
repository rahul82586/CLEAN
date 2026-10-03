[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConCondition](../IMTConCondition.md) / ValueTime

[Previous](ValueBool.md) | [Next](ValueWeekDay.md)

# IMTConCondition::ValueTime

Get the value of a condition that expresses the time.

C++
    
    
    UINT  IMTConCondition::ValueTime()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConCondition.ValueTime()

Python (Manager API)
    
    
    MTConCondition.ValueTime

### Return Value

Time in minutes elapsed since 00:00.

# IMTConCondition::ValueTime

Set the value of a condition that expresses the time.

C++
    
    
    MTAPIRES  IMTConCondition::ValueTime(
       const UINT  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCondition.ValueTime(
       uint        value      // Value
       )

Python (Manager API)
    
    
    MTConCondition.ValueTime

### Parameters

**value**  
[in] A value in minutes elapsed since 00:00.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
