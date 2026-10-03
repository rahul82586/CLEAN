[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Clients](../Clients.md) / AttachmentCreate

[Previous](CommentRequestByDocument.md) | [Next](AttachmentCreateArray.md)

# IMTAdminAPI::AttachmentCreate

Create an attachment object.

C++
    
    
    IMTClient*  IMTAdminAPI::AttachmentCreate()

.NET
    
    
    CIMTClient  CIMTAdminAPI.AttachmentCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTAttachment](../../../Database-Interfaces/Clients/IMTAttachment.md) interface. NULL is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTAttachment::Release](../../../Database-Interfaces/Clients/IMTAttachment/Release.md) method of this object.
