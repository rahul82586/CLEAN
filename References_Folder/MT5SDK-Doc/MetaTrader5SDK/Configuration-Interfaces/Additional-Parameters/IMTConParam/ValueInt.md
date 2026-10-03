[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Additional Parameters](../../Additional-Parameters.md) / [IMTConParam](../IMTConParam.md) / ValueInt

[Previous](ValueString.md) | [Next](ValueFloat.md)

# IMTConParam::ValueInt

Gets a previously specified integer value of a parameter.

C++
    
    
    INT64  IMTConParam::ValueInt()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConParam.ValueInt()

Python
    
    
    MTConParam.ValueInt

### Return Value

A previously specified integer value of a parameter.

### Note

The type of the received parameter must be [IMTConParam::TYPE_INT (#paramtype)](Enumerations.md#paramtype). Otherwise, the method returns 0.

# IMTConParam::ValueInt

Sets an integer value of a parameter.

C++
    
    
    MTAPIRES  IMTConParam::ValueInt(
       const INT64  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConParam.ValueInt(
       long         value      // Value
       )

Python
    
    
    MTConParam.ValueInt

### Parameters

**value**  
[in] Parameter value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

After the call of the method, the parameter type is changed to [IMTConParam::TYPE_INT (#paramtype)](Enumerations.md#paramtype).
