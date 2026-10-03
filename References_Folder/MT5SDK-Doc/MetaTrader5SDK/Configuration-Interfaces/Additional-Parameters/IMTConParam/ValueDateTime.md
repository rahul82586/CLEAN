[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Additional Parameters](../../Additional-Parameters.md) / [IMTConParam](../IMTConParam.md) / ValueDateTime

[Previous](ValueTime.md) | [Next](ValueGroups.md)

# IMTConParam::ValueDateTime

Gets a previously specified parameter value of the datetime type.

C++
    
    
    INT64  IMTConParam::ValueDateTime()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConParam.ValueDateTime()

Python
    
    
    MTConParam.ValueDateTime

### Return Value

A previously specified parameter value of the datetime type.

### Note

The type of the received parameter must be [IMTConParam:TYPE_DATETIME (#paramtype)](Enumerations.md#paramtype). Otherwise, the method returns 0.

# IMTConParam::ValueDateTime

Sets a parameter value of the datetime type.

C++
    
    
    MTAPIRES  IMTConParam::ValueDateTime(
       const INT64  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConParam.ValueDateTime(
       long         value      // Value
       )

Python
    
    
    MTConParam.ValueDateTime

### Parameters

**value**  
[in] Parameter value in the YYYY.MM.DD HH:MM:SS format.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

After the call of the method, the parameter type is changed to [IMTConParam:TYPE_DATETIME (#paramtype)](Enumerations.md#paramtype).
