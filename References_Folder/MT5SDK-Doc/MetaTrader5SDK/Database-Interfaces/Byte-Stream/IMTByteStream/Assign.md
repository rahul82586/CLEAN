[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTByteStream::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTByteStream::Assign(
       const IMTByteStream*  stream      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTByteStream.Assign(
       CIMTByteStream        stream      // Source object
       )

### Parameters

**stream**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
