[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoCondition](../IMTConAutoCondition.md) / ValueInt

[Previous](ValueType.md) | [Next](ValueUInt.md)

# IMTConAutoCondition::ValueInt

Get a condition value of the INT type.

C++
    
    
    INT64  IMTConAutoCondition::ValueInt()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConAutoCondition.ValueInt()

Python
    
    
    MTConAutoCondition.ValueInt

### Return Value

The condition value of the INT type.

# IMTConAutoCondition::ValueInt

Set a condition value of the INT type.

C++
    
    
    MTAPIRES  IMTConAutoCondition::ValueInt(
       const INT64  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoCondition.ValueInt(
       long         value      // Value
       )

Python
    
    
    MTConAutoCondition.ValueInt

### Parameters

**value**  
[in] A value of INT type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
