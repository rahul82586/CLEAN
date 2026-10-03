[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [MTWebAPI Class](../../MTWebAPI-Class.md) / [Groups](../Groups.md) / GroupGet

[Previous](GroupNext.md) | [Next](../Symbols.md)

# MTWebAPI::GroupGet

Get the group configuration by its name.
    
    
    MTAPIRES  MTWebAPI::GroupGet(
       string      $name,       // Group name
       MTConGroup  &$group      // Group configuration
       )

### Parameters

**$name**  
[in] Group name.

**& $group**  
[out] The MTConGroup structure that describes the group configuration. Description of the structure parameters is provided in the"Data Structure"section.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The string specifying the group name must be passed in the UTF-8 format.
