[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [MTWebAPI Class](../../MTWebAPI-Class.md) / [Groups](../Groups.md) / GroupNext

[Previous](GroupTotal.md) | [Next](GroupGet.md)

# MTWebAPI::GroupNext

Get the group configuration by its index in the list of groups of the platform.
    
    
    MTAPIRES  MTWebAPI::GroupNext(
       int         $pos,        // Group position
       MTConGroup  &$group      // Group configuration
       )

### Parameters

**$pos**  
[in] Position of a group, starting with 0.

**& $group**  
[out] The MTConGroup structure that describes the group configuration. Description of the structure parameters is provided in the"Data Structure"section.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
