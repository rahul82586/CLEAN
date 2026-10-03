[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / WebReadParamUInt

[Previous](WebReadParamInt.md) | [Next](WebReadParamInt64.md)

# IMTByteStream::WebReadParamUInt

Reads the value of a UInt parameter from the command sent by a web client.

C++
    
    
    MTAPIRES  IMTByteStream::WebReadParamUInt(
       UINT&     value   // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTByteStream.WebReadParamUInt(
       out uint  value   // Value
       )

### Parameters

**value**  
[out] The value of a parameter of type UInt. The method reads the received string and casts it to the appropriate type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method is used only in the MetaTrader 5 Server API.
