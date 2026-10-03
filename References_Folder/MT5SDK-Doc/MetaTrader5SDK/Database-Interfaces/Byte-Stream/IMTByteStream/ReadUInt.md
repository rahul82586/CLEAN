[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / ReadUInt

[Previous](ReadInt.md) | [Next](ReadInt64.md)

# IMTByteStream::ReadUInt

Reads UInt data from the stream object.

C++
    
    
    MTAPIRES  IMTByteStream::ReadUInt(
       UINT&     data   // Data
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTByteStream.ReadUInt(
       out uint  data   // Data
       )

### Parameters

**data**  
[out] Reference to the read data.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
