[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Clients](../Clients.md) / ClientCreateArray

[Previous](ClientCreate.md) | [Next](ClientSubscribe.md)

# IMTServerAPI::ClientCreateArray

Create an object of the client array.
    
    
    IMTClientArray*  IMTServerAPI::ClientCreateArray()

### Return Value

Returns a pointer to the created object that implements the [IMTClientArray](../../../Database-Interfaces/Clients/IMTClientArray.md) interface. NULL is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTClientArray::Release](../../../Database-Interfaces/Clients/IMTClientArray/Release.md) method of this object.
