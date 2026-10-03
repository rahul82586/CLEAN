[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Clients](../Clients.md) / AttachmentAdd

[Previous](AttachmentCreateArray.md) | [Next](AttachmentAddBatch.md)

# IMTAdminAPI::AttachmentAdd

Create an attachment file for a document or a comment.

C++
    
    
    MTAPIRES  IMTAdminAPI::AttachmentAdd(
       IMTAttachment*  attachment  // Attachment object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.AttachmentAdd(
       CIMTAttachment  attachment  // Attachment object
       )

### Parameters

**attachment**  
[in/out]Attachment object. A ready description of the attachment is input. At the output, the server fills theIMTAttachment::RecordIDidentifier in this description.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Once the attachment identifier is received, you can add the attachment to a document or a request by calling the [IMTDocument::AttachmenAdd](../../../Database-Interfaces/Clients/IMTDocument/AttachmentsAdd.md) or [IMTComment::AttachmentAdd](../../../Database-Interfaces/Clients/IMTComment/AttachmentsAdd.md) respectively.
