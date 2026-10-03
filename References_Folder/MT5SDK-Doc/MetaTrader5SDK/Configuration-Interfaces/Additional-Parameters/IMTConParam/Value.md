[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Additional Parameters](../../Additional-Parameters.md) / [IMTConParam](../IMTConParam.md) / Value

[Previous](Type.md) | [Next](ValueString.md)

# IMTConParam::Value

Get the value of a parameter.

C++
    
    
    LPCWSTR  IMTConParam::Value()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConParam.Value()

Python
    
    
    MTConParam.Value

### Return Value

If successful, it returns a pointer to the string with the parameter value. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConParam](../IMTConParam.md) object.

# IMTConParam::Value

Set the parameter value.

C++
    
    
    MTAPIRES  IMTConParam::Value(
       LPCWSTR  value      // Parameter value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConParam.Value(
       string   value      // Parameter value
       )

Python
    
    
    MTConParam.Value

### Parameters

**value**  
[in] Parameter value

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The value length is limited 256 characters (with the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
