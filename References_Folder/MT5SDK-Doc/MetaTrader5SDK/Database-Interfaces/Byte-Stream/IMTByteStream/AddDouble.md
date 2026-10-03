[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / AddDouble

[Previous](AddFloat.md) | [Next](AddResult.md)

# IMTByteStream::AddDouble

Adds Double data to the stream object.

C++
    
    
    MTAPIRES  IMTByteStream::AddDouble(
       const double  data      // Data
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTByteStream.AddDouble(
       double        data      // Data
       )

### Parameters

**data**  
[in] The data that you want to add.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
