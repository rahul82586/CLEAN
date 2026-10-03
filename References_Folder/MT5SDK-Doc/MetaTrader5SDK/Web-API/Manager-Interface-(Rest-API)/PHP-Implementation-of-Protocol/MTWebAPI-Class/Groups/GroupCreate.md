[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [MTWebAPI Class](../../MTWebAPI-Class.md) / [Groups](../Groups.md) / GroupCreate

[Previous](../Groups.md) | [Next](GroupAdd.md)

# MTWebAPI::GroupCreate

Create an object of a client group.
    
    
    MTUser  MTWebAPI::GroupCreate()

### Return Value

It returns a pointer to the created MTConGroup object used to describe the client group. The client group parameters are described in the ["Data Structure"](../../../Configuration-Databases/Groups/Data-Structure.md) section.

### Note

This method creates an MTConGroup object completely filled with default group parameters.
