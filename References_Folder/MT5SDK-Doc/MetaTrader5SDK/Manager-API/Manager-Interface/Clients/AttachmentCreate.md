[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Clients](../Clients.md) / AttachmentCreate

[Previous](CommentRequestByDocument.md) | [Next](AttachmentCreateArray.md)

# IMTManagerAPI::AttachmentCreate

Create an attachment object.

C++
    
    
    IMTClient*  IMTManagerAPI::AttachmentCreate()

.NET
    
    
    CIMTClient  CIMTManagerAPI.AttachmentCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTAttachment](../../../Database-Interfaces/Clients/IMTAttachment.md) interface. NULL is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTAttachment::Release](../../../Database-Interfaces/Clients/IMTAttachment/Release.md) method of this object.
