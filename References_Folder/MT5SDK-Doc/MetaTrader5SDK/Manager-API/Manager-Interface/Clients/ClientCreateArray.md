[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Clients](../Clients.md) / ClientCreateArray

[Previous](ClientCreate.md) | [Next](ClientAdd.md)

# IMTManagerAPI::ClientCreateArray

Create an object of the client array.

C++
    
    
    IMTClientArray*  IMTManagerAPI::ClientCreateArray()

.NET
    
    
    CIMTClientArray  CIMTManagerAPI.ClientCreateArray()

### Return Value

Returns a pointer to the created object that implements the [IMTClientArray](../../../Database-Interfaces/Clients/IMTClientArray.md) interface. NULL is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTClientArray::Release](../../../Database-Interfaces/Clients/IMTClientArray/Release.md) method of this object.
