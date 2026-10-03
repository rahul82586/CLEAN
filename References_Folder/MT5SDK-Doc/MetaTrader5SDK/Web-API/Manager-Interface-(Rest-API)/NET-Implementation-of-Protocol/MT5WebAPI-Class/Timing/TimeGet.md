[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../../MT5WebAPI-Class.md) / [Timing](../Timing.md) / TimeGet

[Previous](../Timing.md) | [Next](TimeServer.md)

# MT5WebAPI.TimeGet

Get the working time configuration of the server.
    
    
    MTRetCode  MT5WebAPI.TimeGet(
       out MTConTime  time      // Time configuration
       )

### Parameters

**time**  
[out] The MTConTime structure that describes the current settings of the server working time. Description of the structure parameters is provided in the"Data Structure"section.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
