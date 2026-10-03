[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Clients](../Clients.md) / AttachmentGet

[Previous](AttachmentAdd.md) | [Next](../Users.md)

# IMTServerAPI::AttachmentGet

Get an attachment by identifier.
    
    
    MTAPIRES  IMTServerAPI::AttachmentGet(
       const UINT64    attachment_id,  // Identifier
       IMTAttachment*  attachment      // Attachment object
       )

### Parameters

**attachment_id**  
[in] Attachment identifier (IMTAttachment::RecordID).

**attachment**  
[out] Attachment object. The 'attachment' object must be previously created using theIMTServerAPI::AttachmentCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method copies data of an attachment with the specified ID, to the 'attachment' object.
