[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / WebReadCommand

[Previous](WebAddParamFinalize.md) | [Next](WebReadParamName.md)

# IMTByteStream::WebReadCommand

Reads the command sent by a web client.

C++
    
    
    MTAPIRES  IMTByteStream::WebReadCommand(
       MTAPISTR&   cmd     // Command
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTByteStream.WebReadCommand(
       out string  cmd     // Command
       )

### Parameters

**cmd**  
[out] A command sent by the web client.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
