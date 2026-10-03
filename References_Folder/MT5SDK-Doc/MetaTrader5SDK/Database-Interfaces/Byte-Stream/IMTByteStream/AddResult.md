[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / AddResult

[Previous](AddDouble.md) | [Next](AddStr.md)

# IMTByteStream::AddResult

Adds [MTAPIRES (#mtapires)](../../../Internal-Data-Types/README.md#mtapires) data to the stream object.

C++
    
    
    MTAPIRES  IMTByteStream::AddResult(
       const MTAPIRES  data      // Data
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTByteStream.AddResult(
       MTRetCode       data      // Data
       )

### Parameters

**data**  
[in] The data that you want to add.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
