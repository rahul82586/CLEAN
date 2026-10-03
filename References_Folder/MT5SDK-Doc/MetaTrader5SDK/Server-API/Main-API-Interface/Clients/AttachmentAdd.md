[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Clients](../Clients.md) / AttachmentAdd

[Previous](AttachmentCreate.md) | [Next](AttachmentGet.md)

# IMTServerAPI::AttachmentAdd

Create an attachment file for a document or a comment.
    
    
    MTAPIRES  IMTServerAPI::AttachmentAdd(
       IMTAttachment*  attachment,  // Attachment object
       const UINT64    author       // Author
       )

### Parameters

**attachment**  
[in/out]Attachment object. A ready description of the attachment is input. At the output, the server fills theIMTAttachment::RecordIDidentifier in this description.

**author**  
[in] The login of the manager account, on whose behalf the attachment is being added. The login is equal to theIMTConManager::Loginvalue. This information is used to keep the history of client changes.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

After receiving an attachment ID, you can add it to a document or a comment by calling the [IMTDocument::AttachmenAdd](../../../Database-Interfaces/Clients/IMTDocument/AttachmentsAdd.md) or [IMTComment::AttachmentAdd](../../../Database-Interfaces/Clients/IMTComment/AttachmentsAdd.md) method, respectively.
