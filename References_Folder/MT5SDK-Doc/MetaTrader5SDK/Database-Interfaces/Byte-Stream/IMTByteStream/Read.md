[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / Read

[Previous](ReadReset.md) | [Next](ReadSkip.md)

# IMTByteStream::Read

Reads data from the stream object.

C++
    
    
    MTAPIRES  IMTByteStream::Read(
       void*          buf,  // Data
       const UINT     len   // Length
       )

.NET (Gateway/Manager API)
    
    
    byte[]  CIMTByteStream.Read(
       uint           len,  // Length
       out MTRetCode  res   // Response code
       )

### Parameters

**buf**  
[out] A pointer to the read data.

**len**  
[in] The length of data that you want to read from the current pointer.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
