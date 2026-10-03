[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / ReadUChar

[Previous](ReadChar.md) | [Next](ReadShort.md)

# IMTByteStream::ReadUChar

Reads UChar data from the stream object.

C++
    
    
    MTAPIRES  IMTByteStream::ReadUChar(
       UCHAR&    data    // Data
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTByteStream.ReadUChar(
       out byte  data    // Data
       )

### Parameters

**data**  
[out] Reference to the read data.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
