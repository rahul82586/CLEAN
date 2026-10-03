[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / AddInt64

[Previous](AddUInt.md) | [Next](AddUInt64.md)

# IMTByteStream::AddInt64

Adds Int64 data to the stream object.

C++
    
    
    MTAPIRES  IMTByteStream::AddInt64(
       const INT64  data      // Data
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTByteStream.AddInt64(
       long         data      // Data
       )

### Parameters

**data**  
[in] The data that you want to add.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
