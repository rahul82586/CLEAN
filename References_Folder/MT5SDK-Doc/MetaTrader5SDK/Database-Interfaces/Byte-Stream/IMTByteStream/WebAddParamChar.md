[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / WebAddParamChar

[Previous](WebAddParamStr.md) | [Next](WebAddParamUChar.md)

# IMTByteStream::WebAddParamChar

Adds a Char parameter to the stream object for transmission to a web client.

C++
    
    
    MTAPIRES  IMTByteStream::WebAddParamChar(
       LPCWSTR     name,      // Name
       const char  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTByteStream.WebAddParamChar(
       string      name,      // Name
       sbyte       value      // Data
       )

### Parameters

**name**  
[in] Parameter Name.

**value**  
[in] Parameter value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Special characters specified in the 'name' and 'value' parameters are automatically escaped when passed to a web client. For example, if the parameter name is specified as "My|Param", the web client will receive it as a "My\|Param".
