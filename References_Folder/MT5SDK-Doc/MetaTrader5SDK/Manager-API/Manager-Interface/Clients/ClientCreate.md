[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Clients](../Clients.md) / ClientCreate

[Previous](../Clients.md) | [Next](ClientCreateArray.md)

# IMTManagerAPI::ClientCreate

Create a client object.

C++
    
    
    IMTClient*  IMTManagerAPI::ClientCreate()

.NET
    
    
    CIMTClient  CIMTManagerAPI.ClientCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTClient](../../../Database-Interfaces/Clients/IMTClient.md) interface. NULL is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTClient::Release](../../../Database-Interfaces/Clients/IMTClient/Release.md) method of this object.
