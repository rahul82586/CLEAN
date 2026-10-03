[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / WebAddParamDouble

[Previous](WebAddParamUInt64.md) | [Next](WebAddParamFinalize.md)

# IMTByteStream::WebAddParamDouble

Adds a Double parameter to the stream object for transmission to a web client.

C++
    
    
    MTAPIRES  IMTByteStream::WebAddParamDouble(
       LPCWSTR       name,      // Name
       const double  value      // Value
       const UINT    digits     // Digits
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTByteStream.WebAddParamDouble(
       string        name,      // Name
       double        value      // Value
       uint          digits     // Digits
       )

### Parameters

**name**  
[in] The name of the parameter.

**value**  
[in] The value of the parameter. When passed to a web client, the value is converted to a string because the Web API is a text protocol.

**digits**  
The number of decimal places to round up the value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Special characters specified in the 'name' and 'value' parameters are automatically escaped when passed to a web client. For example, if the parameter name is specified as "My|Param", the web client will receive it as a "My\|Param".
