[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConCondition](../IMTConCondition.md) / ValueInt

[Previous](ValueType.md) | [Next](ValueUInt.md)

# IMTConCondition::ValueInt

Get the value of a condition of the INT type.

C++
    
    
    INT64  IMTConCondition::ValueInt()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConCondition.ValueInt()

Python (Manager API)
    
    
    MTConCondition.ValueInt

### Return Value

The condition value of the INT type.

# IMTConCondition::ValueInt

Set the value of a condition of the INT type.

C++
    
    
    MTAPIRES  IMTConCondition::ValueInt(
       const INT64  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCondition.ValueInt(
       long         value      // Value
       )

Python (Manager API)
    
    
    MTConCondition.ValueInt

### Parameters

**value**  
[in] A value of INT type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
