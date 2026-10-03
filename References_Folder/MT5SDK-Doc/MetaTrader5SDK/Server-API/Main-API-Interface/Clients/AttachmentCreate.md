[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Clients](../Clients.md) / AttachmentCreate

[Previous](CommentGetByDocument.md) | [Next](AttachmentAdd.md)

# IMTServerAPI::AttachmentCreate

Create an attachment object.
    
    
    IMTClient*  IMTServerAPI::AttachmentCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTAttachment](../../../Database-Interfaces/Clients/IMTAttachment.md) interface. NULL is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTAttachment::Release](../../../Database-Interfaces/Clients/IMTAttachment/Release.md) method of this object.
