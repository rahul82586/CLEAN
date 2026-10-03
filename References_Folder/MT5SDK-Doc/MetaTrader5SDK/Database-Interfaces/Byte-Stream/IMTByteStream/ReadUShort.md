[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / ReadUShort

[Previous](ReadShort.md) | [Next](ReadInt.md)

# IMTByteStream::ReadUShort

Reads UShort data from the stream object.

C++
    
    
    MTAPIRES  IMTByteStream::ReadUShort(
       USHORT&     data   // Data
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTByteStream.ReadUShort(
       out ushort  data   // Data
       )

### Parameters

**data**  
[out] Reference to the read data.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
