[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConCondition](../IMTConCondition.md) / ValueDatetime

[Previous](ValueVolumeExt.md) | [Next](ValueLeverage.md)

# IMTConCondition::ValueDatetime

Get the value of a condition that expresses date and time.

C++
    
    
    INT64  IMTConCondition::ValueDatetime()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConCondition.ValueDatetime()

Python (Manager API)
    
    
    MTConCondition.ValueDatetime

### Return Value

Date and time in seconds that have elapsed since 01.01.1970.

# IMTConCondition::ValueDatetime

Set the value of a condition that expresses date and time.

C++
    
    
    MTAPIRES  IMTConCondition::ValueDatetime(
       const INT64  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCondition.ValueDatetime(
       long         value      // Value
       )

Python (Manager API)
    
    
    MTConCondition.ValueDatetime

### Parameters

**value**  
[in] Date and time in seconds that have elapsed since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
