[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / WebAddParamFinalize

[Previous](WebAddParamDouble.md) | [Next](WebReadCommand.md)

# IMTByteStream::WebAddParamFinalize

Completes the formation of parameters of the command sent in response to a web client.

C++
    
    
    MTAPIRES  IMTByteStream::WebAddParamFinalize()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTByteStream.WebAddParamFinalize()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method adds a newline character \r\n to the stream object. This symbol indicates the end of the main body of the response (command and parameters).
