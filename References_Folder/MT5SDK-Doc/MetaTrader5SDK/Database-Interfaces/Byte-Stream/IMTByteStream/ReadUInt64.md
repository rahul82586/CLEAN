[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / ReadUInt64

[Previous](ReadInt64.md) | [Next](ReadFloat.md)

# IMTByteStream::ReadUInt64

Reads UInt64 data from the stream object.

C++
    
    
    MTAPIRES  IMTByteStream::ReadUInt64(
       UINT64&    data    // Data
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTByteStream.ReadUInt64(
       out ulong  data    // Data
       )

### Parameters

**data**  
[out] Reference to the read data.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
