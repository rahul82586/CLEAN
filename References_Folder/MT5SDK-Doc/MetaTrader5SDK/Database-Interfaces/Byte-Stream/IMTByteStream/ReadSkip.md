[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / ReadSkip

[Previous](Read.md) | [Next](ReadChar.md)

# IMTByteStream::ReadSkip

Moves the read pointer by the specified number of bytes.

C++
    
    
    MTAPIRES  IMTByteStream::ReadSkip(
       const UINT  len      // Shift of the pointer
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTByteStream.ReadSkip(
       uint        len      // Shift of the pointer
       )

### Parameters

**len**  
[in] The number of bytes by which you want to move the read pointer.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
