[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / AddUInt64

[Previous](AddInt64.md) | [Next](AddFloat.md)

# IMTByteStream::AddUInt64

Adds UInt64 data to the stream object.

C++
    
    
    MTAPIRES  IMTByteStream::AddUInt64(
       const UINT64  data      // Data
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTByteStream.AddUInt64(
       ulong         data      // Data
       )

### Parameters

**data**  
[in] The data that you want to add.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
