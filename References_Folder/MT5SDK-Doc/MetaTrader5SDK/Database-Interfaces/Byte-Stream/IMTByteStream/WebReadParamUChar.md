[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / WebReadParamUChar

[Previous](WebReadParamChar.md) | [Next](WebReadParamShort.md)

# IMTByteStream::WebReadParamUChar

Reads the value of a UChar parameter from the command sent by a web client.

C++
    
    
    MTAPIRES  IMTByteStream::WebReadParamUChar(
       UCHAR&    data    // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTByteStream.WebReadParamUChar(
       out byte  data    // Value
       )

### Parameters

**data**  
[out] The value of a parameter of type UChar. The method reads the received string and casts it to the appropriate type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method is used only in the MetaTrader 5 Server API.
