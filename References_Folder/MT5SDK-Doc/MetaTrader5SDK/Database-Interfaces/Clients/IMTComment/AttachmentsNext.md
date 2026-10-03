[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTComment](../IMTComment.md) / AttachmentsNext

[Previous](AttachmentsTotal.md) | [Next](../IMTCommentArray.md)

# IMTComment::AttachmentsNext

Get the comment attachment identifier by index.

C++
    
    
    MTAPIRES  IMTComment::AttachmentsNext(
       const UINT  pos,             // Position in the list
       UINT64&     attachment_id,   // Identifier
       MTAPISTR&   attachment_name, // Name
       UINT&       attachment_size  // Size
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTComment.AttachmentsNext(
       uint        pos,             // Position in the list
       out ulong   attachment_id,   // Identifier
       out string  attachment_name, // Name
       out uint    attachment_size  // Size
       )

### Parameters

**pos**  
[in] Attachment position starting with 0.

**attachment_id**  
[out] Attachment ID (IMTAttachment::RecordId).

**attachment_name**  
[out] Attachment name (IMTAttachment::FileName).

**attachment_size**  
[out] Attachment size in bytes (IMTAttachment::Size).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

To get an attachment, use the [IMTServerAPI::AttachmentGet](../../../Server-API/Main-API-Interface/Clients/AttachmentGet.md) method by passing the appropriate identifier to it.
