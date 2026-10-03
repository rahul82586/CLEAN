[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / AddUInt

[Previous](AddInt.md) | [Next](AddInt64.md)

# IMTByteStream::AddUInt

Adds UInt data to the stream object.

C++
    
    
    MTAPIRES  IMTByteStream::AddUInt(
       const UINT  data      // Data
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTByteStream.AddUInt(
       uint        data      // Data
       )

### Parameters

**data**  
[in] The data that you want to add.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
