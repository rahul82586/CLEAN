[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Clients](../Clients.md) / ClientCreate

[Previous](../Clients.md) | [Next](ClientCreateArray.md)

# IMTServerAPI::ClientCreate

Create a client object.
    
    
    IMTClient*  IMTServerAPI::ClientCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTClient](../../../Database-Interfaces/Clients/IMTClient.md) interface. NULL is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTClient::Release](../../../Database-Interfaces/Clients/IMTClient/Release.md) method of this object.
