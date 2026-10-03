[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoParam](../IMTConAutoParam.md) / ValueHTML

[Previous](ValueServer.md) | [Next](../IMTConAutomationSink.md)

# IMTConAutoParam::ValueHTML

Get the parameter value of type "HTML content".

C++
    
    
    LPCWSTR  IMTConAutoParam::ValueHTML()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConAutoParam.ValueHTML()

Python
    
    
    MTConAutoParam.ValueHTML

### Return Value

If successful, the method returns a pointer to a string with the HTML contents. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for [IMTConAutoParam](../IMTConAutoParam.md) object lifetime.

# IMTConAutoParam::ValueHTML

Set the parameter value of type "HTML content".

C++
    
    
    MTAPIRES  IMTConAutoParam::ValueHTML(
       LPCWSTR  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoParam.ValueHTML(
       string   value      // Value
       )

Python
    
    
    MTConAutoParam.ValueHTML

### Parameters

**value**  
[in] HTML content.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The value length is limited to 128 characters (including the end-of-line character). If a string of a greater length is assigned, it will be truncated to this length.
