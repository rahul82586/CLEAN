[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / ReadDouble

[Previous](ReadFloat.md) | [Next](ReadResult.md)

# IMTByteStream::ReadDouble

Reads Double data from the stream object.

C++
    
    
    MTAPIRES  IMTByteStream::ReadDouble(
       double&     data   // Data
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTByteStream.ReadDouble(
       out double  data   // Data
       )

### Parameters

**data**  
[out] Reference to the read data.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
