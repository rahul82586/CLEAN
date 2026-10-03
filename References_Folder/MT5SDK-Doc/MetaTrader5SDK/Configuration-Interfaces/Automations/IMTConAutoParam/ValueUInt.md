[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoParam](../IMTConAutoParam.md) / ValueUInt

[Previous](ValueInt.md) | [Next](ValueDouble.md)

# IMTConAutoParam::ValueUInt

Get a parameter value of UINT type.

C++
    
    
    UINT64  IMTConAutoParam::ValueUInt()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConAutoParam.ValueUInt()

Python
    
    
    MTConAutoParam.ValueUInt

### Return Value

A parameter value of the UINT type.

# IMTConAutoParam

Set a parameter value of UINT type.

C++
    
    
    MTAPIRES  IMTConAutoCondition::ValueUInt(
       const UINT64  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoParam.ValueUInt(
       ulong         value      // Value
       )

Python
    
    
    MTConAutoParam.ValueUInt

### Parameters

**value**  
[in] A value of the UINT type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
