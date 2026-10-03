[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / ReadStr

[Previous](ReadResult.md) | [Next](WebAddParamStr.md)

# IMTByteStream::ReadStr

Reads String data from the stream object.

C++
    
    
    MTAPIRES  IMTByteStream::ReadStr(
       MTAPISTR&   buf     // Data
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTByteStream.ReadStr(
       out string  buf     // Data
       )

### Parameters

**buf**  
[out] Reference to the read data.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Data is read until a newline character (\n) or until the end of line character (\0).
