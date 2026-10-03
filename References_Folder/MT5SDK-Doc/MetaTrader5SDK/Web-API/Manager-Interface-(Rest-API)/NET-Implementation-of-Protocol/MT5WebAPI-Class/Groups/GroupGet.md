[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../../MT5WebAPI-Class.md) / [Groups](../Groups.md) / GroupGet

[Previous](GroupNext.md) | [Next](../Symbols.md)

# MT5WebAPI.GroupGet

Get the group configuration by its name.
    
    
    MTRetCode  MT5WebAPI.GroupGet(
       string          name,       // Group name
       out MTConGroup  conGroup    // Group configuration
       )

### Parameters

**name**  
[in] Group name.

**conGroup**  
[out] The MTConGroup structure that describes the group configuration. Description of the structure parameters is provided in the"Data Structure"section.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
