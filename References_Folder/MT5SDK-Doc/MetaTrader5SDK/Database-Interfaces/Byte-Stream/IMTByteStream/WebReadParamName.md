[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / WebReadParamName

[Previous](WebReadCommand.md) | [Next](WebReadParamStr.md)

# IMTByteStream::WebReadParamName

Reads the name of the next parameter of the command sent by a web client.

C++
    
    
    MTAPIRES  IMTByteStream::WebReadParamName(
       MTAPISTR&   name     // Name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTByteStream.WebReadParamName(
       out string  name     // Name
       )

### Parameters

**name**  
[out] The name of the parameter.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code. The return code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) means the end of the command parameters.
