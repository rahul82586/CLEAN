[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPSCondition](../IMTConCondition.md) / IMTConCondition ValueTime

[Previous](IMTConCondition-ValueBool.md) | [Next](IMTConCondition-ValueDate.md)

# IMTConVPSCondition::ValueTime

Get the value of a condition that expresses the time.

C++
    
    
    UINT  IMTConVPSCondition::ValueTime()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConVPSCondition.ValueTime()

Python
    
    
    MTConVPSCondition.ValueTime

### Return Value

Time in minutes since 00:00.

# IMTConVPSCondition::ValueTime

Set the value of a condition that expresses the time.

C++
    
    
    MTAPIRES  IMTConVPSCondition::ValueTime(
       const UINT  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPSCondition.ValueTime(
       uint        value      // Value
       )

Python
    
    
    MTConVPSCondition.ValueTime

### Parameters

**value**  
[in] A value in minutes since 00:00.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
