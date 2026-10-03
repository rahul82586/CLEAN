[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPSCondition](../IMTConCondition.md) / IMTConCondition ValueBool

[Previous](IMTConCondition-ValueLeverage.md) | [Next](IMTConCondition-ValueTime.md)

# IMTConVPSCondition::ValueBool

Get the condition value of the bool type.

C++
    
    
    bool  IMTConVPSCondition::ValueBool()  const

.NET (Gateway/Manager API)
    
    
    bool  CIMTConVPSCondition.ValueBool()

Python
    
    
    MTConVPSCondition.ValueBool

### Return Value

True or false.

# IMTConVPSCondition::ValueBool

Set the condition value of the bool type.

C++
    
    
    MTAPIRES  IMTConVPSCondition::ValueBool(
       const bool  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPSCondition.ValueBool(
       bool        value      // Value
       )

Python
    
    
    MTConVPSCondition.ValueBool

### Parameters

**value**  
[in] True or false.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
