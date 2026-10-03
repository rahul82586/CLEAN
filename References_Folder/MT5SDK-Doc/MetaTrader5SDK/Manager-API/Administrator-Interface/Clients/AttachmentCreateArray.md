[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Clients](../Clients.md) / AttachmentCreateArray

[Previous](AttachmentCreate.md) | [Next](AttachmentAdd.md)

# IMTAdminAPI::AttachmentCreateArray

Create an object of the array of attachments.

C++
    
    
    IMTClient*  IMTAdminAPI::AttachmentCreateArray()

.NET
    
    
    CIMTClient  CIMTAdminAPI.AttachmentCreateArray()

### Return Value

Returns a pointer to the created object that implements the [IMTAttachmentArray](../../../Database-Interfaces/Clients/IMTAttachmentArray.md). NULL is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTAttachmentArray::Release](../../../Database-Interfaces/Clients/IMTAttachmentArray/Release.md) method of this object.
