[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPSCondition](../IMTConCondition.md) / IMTConCondition ValueInt

[Previous](IMTConCondition-ValueType.md) | [Next](IMTConCondition-ValueUInt.md)

# IMTConVPSCondition::ValueInt

Get a condition value of the INT type.

C++
    
    
    INT64  IMTConVPSCondition::ValueInt()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConVPSCondition.ValueInt()

Python
    
    
    MTConVPSCondition.ValueInt

### Return Value

The condition value of the INT type.

# IMTConAutoCondition::ValueInt

Set the value of a condition of the INT type.

C++
    
    
    MTAPIRES  IMTConVPSCondition::ValueInt(
       const INT64  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPSCondition.ValueInt(
       long         value      // Value
       )

Python
    
    
    MTConVPSCondition.ValueInt

### Parameters

**value**  
[in] A value of INT type.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
