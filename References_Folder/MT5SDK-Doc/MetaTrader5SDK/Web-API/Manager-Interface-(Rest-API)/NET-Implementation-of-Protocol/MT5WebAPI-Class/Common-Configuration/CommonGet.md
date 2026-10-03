[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../../MT5WebAPI-Class.md) / [Common Configuration](../Common-Configuration.md) / CommonGet

[Previous](../Common-Configuration.md) | [Next](../Timing.md)

# MT5WebAPI.CommonGet

Get the common configuration of the trading platform.
    
    
    MTRetCode  MT5WebAPI.CommonGet(
       out MTConCommon  common      // Common configuration
       )

### Parameters

**out common**  
[out] The MTConCommon structure that describes the common configuration of the trading platform. The structure parameters are described in section"Data Structure".

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
