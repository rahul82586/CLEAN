[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Byte Stream](../../Byte-Stream.md) / [IMTByteStream](../IMTByteStream.md) / WebReadParamSkip

[Previous](WebReadParamStr.md) | [Next](WebReadParamChar.md)

# IMTByteStream::WebReadParamSkip

Skips parameter value. After calling this method, moves to the name of the next parameter.

C++
    
    
    MTAPIRES  IMTByteStream::WebReadParamSkip()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTByteStream.WebReadParamSkip()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method only allows skipping parameter values, but not their names.
