[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Clients](../Clients.md) / DocumentCreateArray

[Previous](DocumentCreate.md) | [Next](DocumentSubscribe.md)

# IMTServerAPI::DocumentCreateArray

Create an object of the array of documents.
    
    
    IMTClientArray*  IMTServerAPI::DocumentCreateArray()

### Return Value

Returns a pointer to the created object that implements the [IMTDocumentArray](../../../Database-Interfaces/Clients/IMTDocumentArray.md) interface. NULL is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTDocumentArray::Release](../../../Database-Interfaces/Clients/IMTDocumentArray/Release.md) method of this object.
