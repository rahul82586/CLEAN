[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTComment](../IMTComment.md) / AttachmentsAdd

[Previous](CommentResult.md) | [Next](AttachmentsClear.md)

# IMTComment::AttachmentsAdd

Add [attachment](../IMTAttachment.md) to a comment.

C++
    
    
    MTAPIRES  IMTComment::AttachmentsAdd(
       IMTAttachment*  attachment  // Attachment object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTComment.AttachmentsAdd(
       CIMTAttachment  attachment  // Attachment object
       )

### Parameters

**attachment**  
[in]Attachment object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The [IMTAttachment::RecordID](../IMTAttachment/RecordID.md) identifier must be specified for the attachment to be added. To get the identifier, call the [IMTServerAPI::AttachmentAdd](../../../Server-API/Main-API-Interface/Clients/AttachmentAdd.md) method and only after that add the ready attachment object to a comment. Actually, IMTComment::AttachmentsAdd does not create an attachment, but it only adds to a comment a link to a ready attachment.
