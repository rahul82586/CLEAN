[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / AddChar

[Previous](Add.md) | [Next](AddUChar.md)

# IMTByteStream::AddChar

Adds Char data to the stream object.

C++
    
    
    MTAPIRES  IMTByteStream::AddChar(
       const char  data      // Data
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTByteStream.AddChar(
       sbyte       data      // Data
       )

### Parameters

**data**  
[in] The data that you want to add.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
