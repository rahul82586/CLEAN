[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConCondition](../IMTConCondition.md) / ValueWeekDay

[Previous](ValueTime.md) | [Next](../IMTConRouteDealer.md)

# IMTConCondition::ValueWeekDay

Get the value of a condition that expresses a weekday.

C++
    
    
    UINT  IMTConCondition::ValueWeekDay()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConCondition.ValueWeekDay()

Python (Manager API)
    
    
    MTConCondition.ValueWeekDay

### Return Value

Weekday index. 0 corresponds to Sunday, 6 - to Saturday.

# IMTConCondition::ValueWeekDay

Set the value of a condition that expresses a weekday.

C++
    
    
    MTAPIRES  IMTConCondition::ValueWeekDay(
       const UINT  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCondition.ValueWeekDay(
       uint        value      // Value
       )

Python (Manager API)
    
    
    MTConCondition.ValueWeekDay

### Parameters

**value**  
[in] Weekday index. 0 corresponds to Sunday, 6 - to Saturday.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
