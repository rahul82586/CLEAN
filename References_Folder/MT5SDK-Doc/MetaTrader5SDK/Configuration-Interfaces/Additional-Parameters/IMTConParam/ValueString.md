[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Additional Parameters](../../Additional-Parameters.md) / [IMTConParam](../IMTConParam.md) / ValueString

[Previous](Value.md) | [Next](ValueInt.md)

# IMTConParam::ValueString

Gets a previously specified string value of a parameter.

C++
    
    
    LPCWSTR  IMTConParam::ValueString()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConParam.ValueString()

Python
    
    
    MTConParam.ValueString

### Return Value

A previously specified string value of a parameter.

### Note

The type of the received parameter must be [IMTConParam::TYPE_STRING (#paramtype)](Enumerations.md#paramtype). Otherwise, the method returns an empty string.

# IMTConParam::ValueString

Sets a string value of a parameter.

C++
    
    
    MTAPIRES  IMTConParam::ValueString(
       LPCWSTR  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConParam.ValueString(
       string   value      // Value
       )

Python
    
    
    MTConParam.ValueString

### Parameters

**value**  
[in] Parameter value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

After the call of the method, the parameter type is changed to [IMTConParam::TYPE_STRING (#paramtype)](Enumerations.md#paramtype).

The maximum string length is 256 characters (with the sign of the string end). If a string of a greater length is assigned, it will be cut to this length.
