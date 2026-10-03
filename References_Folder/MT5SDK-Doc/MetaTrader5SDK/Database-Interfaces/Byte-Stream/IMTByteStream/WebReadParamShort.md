[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / WebReadParamShort

[Previous](WebReadParamUChar.md) | [Next](WebReadParamUShort.md)

# IMTByteStream::WebReadParamShort

Reads the value of a Short parameter from the command sent by a web client.

C++
    
    
    MTAPIRES  IMTByteStream::WebReadParamShort(
       SHORT&     data   // Value
       )

C++
    
    
    MTRetCode  CIMTByteStream.WebReadParamShort(
       out short  data   // Value
       )

### Parameters

**data**  
[out] The value of a parameter of type Short. The method reads the received string and casts it to the appropriate type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method is used only in the MetaTrader 5 Server API.
