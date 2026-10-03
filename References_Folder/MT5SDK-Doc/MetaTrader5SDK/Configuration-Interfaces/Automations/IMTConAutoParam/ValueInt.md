[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoParam](../IMTConAutoParam.md) / ValueInt

[Previous](ValueType.md) | [Next](ValueUInt.md)

# IMTConAutoParam::ValueInt

Get a parameter value of INT type.

C++
    
    
    INT64  IMTConAutoParam::ValueInt()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConAutoParam.ValueInt()

Python
    
    
    MTConAutoParam.ValueInt

### Return Value

A parameter value of the INT type.

# IMTConAutoParam::ValueInt

Set a parameter value of INT type.

C++
    
    
    MTAPIRES  IMTConAutoParam::ValueInt(
       const INT64  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoParam.ValueInt(
       long         value      // Value
       )

Python
    
    
    MTConAutoParam.ValueInt

### Parameters

**value**  
[in] A value of INT type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
