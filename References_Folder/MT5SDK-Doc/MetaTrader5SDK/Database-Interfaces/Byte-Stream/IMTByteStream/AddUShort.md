[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / AddUShort

[Previous](AddShort.md) | [Next](AddInt.md)

# IMTByteStream::AddUShort

Adds UShort data to the stream object.

C++
    
    
    MTAPIRES  IMTByteStream::AddUShort(
       const USHORT  data      // Data
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTByteStream.AddUShort(
       ushort        data      // Data
       )

### Parameters

**data**  
[in] The data that you want to add.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
