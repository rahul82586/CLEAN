[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / AddShort

[Previous](AddUChar.md) | [Next](AddUShort.md)

# IMTByteStream::AddShort

Adds Short data to the stream object.

C++
    
    
    MTAPIRES  IMTByteStream::AddShort(
       const short  data      // Data
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTByteStream.AddShort(
       short        data      // Data
       )

### Parameters

**data**  
[in] The data that you want to add.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
