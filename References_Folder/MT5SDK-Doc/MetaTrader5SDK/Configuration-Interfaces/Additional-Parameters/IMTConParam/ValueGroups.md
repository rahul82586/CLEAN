[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Additional Parameters](../../Additional-Parameters.md) / [IMTConParam](../IMTConParam.md) / ValueGroups

[Previous](ValueDateTime.md) | [Next](ValueSymbols.md)

# IMTConParam::ValueGroups

Gets the previously set parameter value of the "group of users" type.

C++
    
    
    LPCWSTR  IMTConParam::ValueGroups()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConParam.ValueGroups()

Python
    
    
    MTConParam.ValueGroups

### Return Value

A previously set parameter value of the "group of users" type.

### Note

The type of the received parameter must be [IMTConParam:TYPE_GROUPS (#paramtype)](Enumerations.md#paramtype). Otherwise, the method returns 0.

# IMTConParam::ValueGroups

Sets a parameter value of the "group of users" type.

C++
    
    
    MTAPIRES  IMTConParam::ValueDateTime(
       const LPCWSTR  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConParam.ValueDateTime(
       stirng         value      // Value
       )

Python
    
    
    MTConParam.ValueGroups

### Parameters

**value**  
[in] Parameter value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

After the call of the method, the parameter type is changed to [IMTConParam:TYPE_GROUPS (#paramtype)](Enumerations.md#paramtype).
