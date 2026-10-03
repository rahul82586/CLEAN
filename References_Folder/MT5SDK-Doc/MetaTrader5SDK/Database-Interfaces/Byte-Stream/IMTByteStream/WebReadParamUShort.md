[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / WebReadParamUShort

[Previous](WebReadParamShort.md) | [Next](WebReadParamInt.md)

# IMTByteStream::WebReadParamUShort

Reads the value of a UShort parameter from the command sent by a web client.

C++
    
    
    MTAPIRES  IMTByteStream::WebReadParamUShort(
       USHORT&     data   // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTByteStream.WebReadParamUShort(
       out ushort  data   // Value
       )

### Parameters

**data**  
[out] The value of a parameter of type UShort. The method reads the received string and casts it to the appropriate type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method is used only in the MetaTrader 5 Server API.
