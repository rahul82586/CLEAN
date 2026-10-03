[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRoute](../IMTConRoute.md) / ParamString

[Previous](ParamDouble.md) | [Next](ParamColor.md)

# IMTConRoute::ParamString

Get the value of an additional parameter of the string type.

C++
    
    
    LPCWSTR  IMTConRoute::ParamString()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConRoute.ParamString()

Python (Manager API)
    
    
    MTConRoute.ParamString

### Return Value

If successful, it returns a pointer to the string with the value. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConRoute](../IMTConRoute.md) object.

# IMTConRoute::ParamString

Set the value of an additional parameter of the string type.

C++
    
    
    MTAPIRES  IMTConRoute::ParamString(
       LPCWSTR  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConRoute.ParamString(
       srting   value      // Value
       )

Python (Manager API)
    
    
    MTConRoute.ParamString

### Parameters

**value**  
[in] Parameter value of the string type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum value length is 128 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
