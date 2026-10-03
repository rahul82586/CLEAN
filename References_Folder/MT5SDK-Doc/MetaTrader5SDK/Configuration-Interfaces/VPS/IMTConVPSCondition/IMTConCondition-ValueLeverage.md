[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPSCondition](../IMTConCondition.md) / IMTConCondition ValueLeverage

[Previous](IMTConCondition-ValueDatetime.md) | [Next](IMTConCondition-ValueBool.md)

# IMTConVPSCondition::ValueLeverage

Get the value of a condition that expresses the leverage.

C++
    
    
    INT64  IMTConVPSCondition::ValueLeverage()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConVPSCondition.ValueLeverage()

Python
    
    
    MTConVPSCondition.ValueLeverage

### Return Value

Value of the leverage from 1 to 500.

# IMTConVPSCondition::ValueLeverage

Set the value of a condition that expresses the leverage.

C++
    
    
    MTAPIRES  IMTConVPSCondition::ValueLeverage(
       const INT64  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPSCondition.ValueLeverage(
       long         value      // Value
       )

Python
    
    
    MTConVPSCondition.ValueLeverage

### Parameters

**value**  
[in] Value of the leverage from 1 to 500.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
