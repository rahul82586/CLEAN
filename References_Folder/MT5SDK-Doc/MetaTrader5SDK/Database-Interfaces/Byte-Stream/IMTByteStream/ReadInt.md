[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / ReadInt

[Previous](ReadUShort.md) | [Next](ReadUInt.md)

# IMTByteStream::ReadInt

Reads Int data from the stream object.

C++
    
    
    MTAPIRES  IMTByteStream::ReadInt(
       INT&     data   // Data
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTByteStream.ReadInt(
       out int  data   // Data
       )

### Parameters

**data**  
[out] Reference to the read data.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
