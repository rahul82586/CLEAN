[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoParam](../IMTConAutoParam.md) / ValueString

[Previous](ValueDouble.md) | [Next](ValueColor.md)

# IMTConAutoParam::ValueString

Get a parameter value of the string type.

C++
    
    
    LPCWSTR  IMTConAutoParam::ValueString()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConAutoParam.ValueString()

Python
    
    
    MTConAutoParam.ValueString

### Return Value

If successful, the method returns a pointer to the string with the value. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for [IMTConAutoParam](../IMTConAutoParam.md) object lifetime.

# IMTConAutoParam::ValueString

Set a parameter value of the string type.

C++
    
    
    MTAPIRES  IMTConAutoParam::ValueString(
       LPCWSTR  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoParam.ValueString(
       string   value      // Value
       )

Python
    
    
    MTConAutoParam.ValueString

### Parameters

**value**  
[in] A value of the string type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The value length is limited to 128 characters (including the end-of-line character). If a string of a greater length is assigned, it will be truncated to this length.
