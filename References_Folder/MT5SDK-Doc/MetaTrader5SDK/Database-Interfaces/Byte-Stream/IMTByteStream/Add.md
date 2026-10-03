[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / Add

[Previous](ReadLen.md) | [Next](AddChar.md)

# IMTByteStream::Add

Adds data to the stream object.

C++
    
    
    MTAPIRES  IMTByteStream::Add(
       const void  *buf,     // Data
       const UINT  len       // Data size
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTByteStream.Add(
       byte[]      buf       // Data
       )

### Parameters

***buf**  
[in] A pointer to the data that you want to add.

**len**  
[in] The length of the data to add in bytes.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
