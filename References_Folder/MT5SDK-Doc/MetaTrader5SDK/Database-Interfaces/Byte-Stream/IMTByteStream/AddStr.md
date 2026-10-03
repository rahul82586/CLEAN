[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / AddStr

[Previous](AddResult.md) | [Next](ReadReset.md)

# IMTByteStream::AddStr

Adds String data to the stream object.

C++
    
    
    MTAPIRES  IMTByteStream::AddStr(
       LPCWSTR  buf      // Data
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTByteStream.AddStr(
       string   buf      // Data
       )

### Parameters

**buf**  
[in] The data that you want to add.The end of line character (\0) is added automatically after the data string.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The end of line character (\0) is added automatically after the data string passed in the buf parameter.
