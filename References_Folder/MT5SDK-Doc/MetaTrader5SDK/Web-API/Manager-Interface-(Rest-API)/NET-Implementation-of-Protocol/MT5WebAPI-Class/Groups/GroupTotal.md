[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../../MT5WebAPI-Class.md) / [Groups](../Groups.md) / GroupTotal

[Previous](GroupDelete.md) | [Next](GroupNext.md)

# MT5WebAPI.GroupTotal

Get the number of groups created on the trade server.
    
    
    MTRetCode  MT5WebAPI.GroupTotal(
       out int  total      // The number of groups
       )

### Parameters

**total**  
[out] The number of groups on the server.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
