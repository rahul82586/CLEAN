[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / ReadInt64

[Previous](ReadUInt.md) | [Next](ReadUInt64.md)

# IMTByteStream::ReadInt64

Reads Int64 data from the stream object.

C++
    
    
    MTAPIRES  IMTByteStream::ReadInt64(
       INT64&    data    // Data
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTByteStream.ReadInt64(
       out long  data    // Data
       )

### Parameters

**data**  
[out] Reference to the read data.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
