[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTComment](../IMTComment.md) / AttachmentsClear

[Previous](AttachmentsAdd.md) | [Next](AttachmentsTotal.md)

# IMTComment::AttachmentsClear

Clear the list of comment [attachments](../IMTAttachment.md).

C++
    
    
    MTAPIRES  IMTComment::AttachmentsClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTComment.AttachmentsClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

This method clears the entire list of attachments in a comment.
