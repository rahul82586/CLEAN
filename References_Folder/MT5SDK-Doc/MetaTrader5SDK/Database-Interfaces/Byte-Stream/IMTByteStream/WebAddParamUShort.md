[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / WebAddParamUShort

[Previous](WebAddParamShort.md) | [Next](WebAddParamInt.md)

# IMTByteStream::WebAddParamUShort

Adds a UShort parameter to the stream object for transmission to a web client.

C++
    
    
    MTAPIRES  IMTByteStream::WebAddParamUShort(
       LPCWSTR       name,      // Name
       const USHORT  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTByteStream.WebAddParamUShort(
       string        name,      // Name
       ushort        value      // Value
       )

### Parameters

**name**  
[in] The name of the parameter.

**value**  
[in] The value of the parameter. When passed to a web client, the value is converted to a string because the Web API is a text protocol.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Special characters specified in the 'name' and 'value' parameters are automatically escaped when passed to a web client. For example, if the parameter name is specified as "My|Param", the web client will receive it as a "My\|Param".
