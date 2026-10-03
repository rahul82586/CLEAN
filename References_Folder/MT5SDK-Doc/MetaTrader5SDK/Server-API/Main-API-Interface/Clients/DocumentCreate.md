[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Clients](../Clients.md) / DocumentCreate

[Previous](ClientUserLogins.md) | [Next](DocumentCreateArray.md)

# IMTServerAPI::DocumentCreate

Create a document object.
    
    
    IMTClient*  IMTServerAPI::DocumentCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTDocument](../../../Database-Interfaces/Clients/IMTDocument.md) interface. NULL is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTDocument::Release](../../../Database-Interfaces/Clients/IMTDocument/Release.md) method of this object.
