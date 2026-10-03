[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / ReadResult

[Previous](ReadDouble.md) | [Next](ReadStr.md)

# IMTByteStream::ReadResult

Reads [MTAPIRES (#mtapires)](../../../Internal-Data-Types/README.md#mtapires) data from the stream object.

C++
    
    
    MTAPIRES  IMTByteStream::ReadResult(
       MTAPIRES&      data  // Data
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTByteStream.ReadResult(
       out MTRetCode  data  // Data
       )

### Parameters

**data**  
[out] Reference to the read data.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
