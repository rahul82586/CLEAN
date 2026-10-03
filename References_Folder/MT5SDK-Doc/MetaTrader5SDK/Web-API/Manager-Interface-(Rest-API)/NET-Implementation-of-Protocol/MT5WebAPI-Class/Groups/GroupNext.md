[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../../MT5WebAPI-Class.md) / [Groups](../Groups.md) / GroupNext

[Previous](GroupTotal.md) | [Next](GroupGet.md)

# MT5WebAPI.GroupNext

Get the group configuration by its index in the list of groups of the platform.
    
    
    MTRetCode  MT5WebAPI.GroupNext(
       uint            pos,       // Group position
       out MTConGroup  conGroup   // Group configuration
       )

### Parameters

**pos**  
[in] Position of a group, starting with 0.

**conGroup**  
[out] The MTConGroup structure that describes the group configuration. Description of the structure parameters is provided in the"Data Structure"section.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
