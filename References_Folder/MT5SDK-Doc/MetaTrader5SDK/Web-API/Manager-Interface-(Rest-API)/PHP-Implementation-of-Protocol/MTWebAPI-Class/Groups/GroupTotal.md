[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [MTWebAPI Class](../../MTWebAPI-Class.md) / [Groups](../Groups.md) / GroupTotal

[Previous](GroupDelete.md) | [Next](GroupNext.md)

# MTWebAPI::GroupTotal

Get the number of groups created on the trade server.
    
    
    MTAPIRES  MTWebAPI::GroupTotal(
       int  &$total      // Number of groups
       )

### Parameters

**& $total**  
[out] The number of groups on the server.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
