[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoCondition](../IMTConAutoCondition.md) / ValueUInt

[Previous](ValueInt.md) | [Next](ValueDouble.md)

# IMTConAutoCondition::ValueUInt

Get the value of a condition of the UINT type.

C++
    
    
    UINT64  IMTConAutoCondition::ValueUInt()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConAutoCondition.ValueUInt()

Python
    
    
    MTConAutoCondition.ValueUInt

### Return Value

The condition value of the UINT type.

# IMTConAutoCondition::ValueUInt

Set the value of a condition of the UINT type.

C++
    
    
    MTAPIRES  IMTConAutoCondition::ValueUInt(
       const UINT64  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoCondition.ValueUInt(
       ulong         value      // Value
       )

Python
    
    
    MTConAutoCondition.ValueUInt

### Parameters

**value**  
[in] A value of the UINT type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
