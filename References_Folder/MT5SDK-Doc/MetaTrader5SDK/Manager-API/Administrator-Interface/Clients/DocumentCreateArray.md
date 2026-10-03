[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Clients](../Clients.md) / DocumentCreateArray

[Previous](DocumentCreate.md) | [Next](DocumentAdd.md)

# IMTAdminAPI::DocumentCreateArray

Create an object of the array of documents.

C++
    
    
    IMTClientArray*  IMTAdminAPI::DocumentCreateArray()

.NET
    
    
    CIMTClientArray  CIMTAdminAPI.DocumentCreateArray()

### Return Value

Returns a pointer to the created object that implements the [IMTDocumentArray](../../../Database-Interfaces/Clients/IMTDocumentArray.md) interface. NULL is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTDocumentArray::Release](../../../Database-Interfaces/Clients/IMTDocumentArray/Release.md) method of this object.
