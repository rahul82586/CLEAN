[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Clients](../Clients.md) / DocumentCreate

[Previous](ClientUserRequest.md) | [Next](DocumentCreateArray.md)

# IMTAdminAPI::DocumentCreate

Create a document object.

C++
    
    
    IMTClient*  IMTAdminAPI::DocumentCreate()

.NET
    
    
    CIMTClient  CIMTAdminAPI.DocumentCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTDocument](../../../Database-Interfaces/Clients/IMTDocument.md) interface. NULL is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTDocument::Release](../../../Database-Interfaces/Clients/IMTDocument/Release.md) method of this object.
