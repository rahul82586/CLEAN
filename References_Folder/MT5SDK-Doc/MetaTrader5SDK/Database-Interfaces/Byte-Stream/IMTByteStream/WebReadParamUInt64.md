[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / WebReadParamUInt64

[Previous](WebReadParamInt64.md) | [Next](WebReadParamDouble.md)

# IMTByteStream::WebReadParamUInt64

Reads the value of a UInt64 parameter from the command sent by a web client.

C++
    
    
    MTAPIRES  IMTByteStream::WebReadParamUInt64(
       UINT64&    value    // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTByteStream.WebReadParamUInt64(
       out ulong  value    // Value
       )

### Parameters

**value**  
[out] The value of a parameter of type UInt64. The method reads the received string and casts it to the appropriate type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method is used only in the MetaTrader 5 Server API.
