[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Additional Parameters](../../Additional-Parameters.md) / [IMTConParam](../IMTConParam.md) / ValueFloat

[Previous](ValueInt.md) | [Next](ValueTime.md)

# IMTConParam::ValueFloat

Gets a previously specified parameter value of the float type.

C++
    
    
    double  IMTConParam::ValueFloat()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConParam.ValueFloat()

Python
    
    
    MTConParam.ValueFloat

### Return Value

A previously specified parameter value of the float type.

### Note

The type of the received parameter must be [IMTConParam::TYPE_FLOAT (#paramtype)](Enumerations.md#paramtype). Otherwise, the method returns 0.

# IMTConParam::ValueFloat

Sets a parameter value of the float type.

C++
    
    
    MTAPIRES  IMTConParam::ValueFloat(
       const double  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConParam.ValueFloat(
       double        value      // Value
       )

Python
    
    
    MTConParam.ValueFloat

### Parameters

**value**  
[in] Parameter value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

After the method call, the parameter type is changed to [IMTConParam::TYPE_FLOAT (#paramtype)](Enumerations.md#paramtype).
