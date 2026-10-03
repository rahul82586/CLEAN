[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPSCondition](../IMTConCondition.md) / IMTConCondition ValueUInt

[Previous](IMTConCondition-ValueInt.md) | [Next](IMTConCondition-ValueDouble.md)

# IMTConVPSCondition::ValueUInt

Get the value of a condition of the UINT type.

C++
    
    
    UINT64  IMTConVPSCondition::ValueUInt()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConVPSCondition.ValueUInt()

Python
    
    
    MTConVPSCondition.ValueUInt

### Return Value

The condition value of the UINT type.

# IMTConAutoCondition::ValueUInt

Set the value of a condition of the UINT type.

C++
    
    
    MTAPIRES  IMTConVPSCondition::ValueUInt(
       const UINT64  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPSCondition.ValueUInt(
       ulong         value      // Value
       )

Python
    
    
    MTConVPSCondition.ValueUInt

### Parameters

**value**  
[in] A value of the UINT type.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
