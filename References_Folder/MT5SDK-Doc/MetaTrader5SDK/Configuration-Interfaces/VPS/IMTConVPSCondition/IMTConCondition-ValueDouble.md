[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPSCondition](../IMTConCondition.md) / IMTConCondition ValueDouble

[Previous](IMTConCondition-ValueUInt.md) | [Next](IMTConCondition-ValueString.md)

# IMTConVPSCondition::ValueDouble

Get a condition value of the double type.

C++
    
    
    double  IMTConVPSCondition::ValueDouble()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConVPSCondition.ValueDouble()

Python
    
    
    MTConVPSCondition.ValueDouble

### Return Value

The condition value of the double type.

# IMTConVPSCondition::ValueDouble

Set a condition value of the double type.

C++
    
    
    MTAPIRES  IMTConVPSCondition::ValueDouble(
       const double  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPSCondition.ValueDouble(
       double        value      // Value
       )

Python
    
    
    MTConVPSCondition.ValueDouble

### Parameters

**value**  
[in] A value of the double type.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
