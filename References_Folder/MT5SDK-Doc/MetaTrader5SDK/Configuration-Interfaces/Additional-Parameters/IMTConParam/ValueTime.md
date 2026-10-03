[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Additional Parameters](../../Additional-Parameters.md) / [IMTConParam](../IMTConParam.md) / ValueTime

[Previous](ValueFloat.md) | [Next](ValueDateTime.md)

# IMTConParam::ValueTime

Gets a previously specified parameter value of the time type.

C++
    
    
    INT64  IMTConParam::ValueTime()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConParam.ValueTime()

Python
    
    
    MTConParam.ValueTime

### Return Value

A previously specified parameter value of the time type.

### Note

The type of the received parameter must be [IMTConParam::TYPE_TIME (#paramtype)](Enumerations.md#paramtype). Otherwise, the method returns 0.

# IMTConParam::ValueTime

Sets a parameter value of the time type.

C++
    
    
    MTAPIRES  IMTConParam::ValueTime(
       const INT64  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConParam.ValueTime(
       long         value      // Value
       )

Python
    
    
    MTConParam.ValueTime

### Parameters

**value**  
[in] Parameter value in the HH:MM:SS format.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

After the call of the method, the parameter type is changed to [IMTConParam::TYPE_TIME (#paramtype)](Enumerations.md#paramtype).
