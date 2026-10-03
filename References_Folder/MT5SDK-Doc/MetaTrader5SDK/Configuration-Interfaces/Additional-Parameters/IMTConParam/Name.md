[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Additional Parameters](../../Additional-Parameters.md) / [IMTConParam](../IMTConParam.md) / Name

[Previous](Clear.md) | [Next](Type.md)

# IMTConParam::Name

Get the name of a parameter.

C++
    
    
    LPCWSTR  IMTConParam::Name()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConParam.Name()

Python
    
    
    MTConParam.Name

### Return Value

If successful, it returns a pointer to the string with the parameter name. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConParam](../IMTConParam.md) object.

# IMTConParam::Name

Set the parameter name.

C++
    
    
    MTAPIRES  IMTConParam::Name(
       LPCWSTR  name      // Parameter name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConParam.Name(
       string   name      // Parameter name
       )

Python
    
    
    MTConParam.Name

### Parameters

**name**  
[in] Parameter Name.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum name length is 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
