[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [MTWebAPI Class](../../MTWebAPI-Class.md) / [Clients](../Clients.md) / UserCreate

[Previous](../Clients.md) | [Next](UserAdd.md)

# MTWebAPI::UserCreate

Create an object of a client record.
    
    
    MTUser  MTWebAPI::UserCreate()

### Return Value

It returns a pointer to the created MTUser object used to describe the client account. The client account parameters are described in the ["Data Structure"](../../../Users/Data-Structure.md) section.

### Note

This method creates an MTUser object completely filled with default user parameters.
