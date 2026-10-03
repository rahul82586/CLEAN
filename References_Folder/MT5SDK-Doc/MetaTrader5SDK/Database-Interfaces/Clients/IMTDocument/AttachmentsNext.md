[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTDocument](../IMTDocument.md) / AttachmentsNext

[Previous](AttachmentsTotal.md) | [Next](../IMTDocumentArray.md)

# IMTDocument::AttachmentsNext

Get the file ID from a document, by index.

C++
    
    
    MTAPIRES  IMTDocument::AttachmentsNext(
       const UINT  pos,             // Position in the list
       UINT64&     attachment_id,   // Identifier
       MTAPISTR&   attachment_name, // Name
       UINT&       attachment_size  // Size
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDocument.AttachmentsNext(
       uint        pos,             // Position in the list
       out ulong   attachment_id,   // Identifier
       out string  attachment_name, // Name
       out uint    attachment_size  // Size
       )

### Parameters

**pos**  
[in] File position starting with 0.

**attachment_id**  
[out] File identifier (IMTAttachment::RecordId).

**attachment_name**  
[out] File name (IMTAttachment::FileName).

**attachment_size**  
[out] File size in bytes (IMTAttachment::Size).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

To get a file, use the [IMTServerAPI::AttachmentGet](../../../Server-API/Main-API-Interface/Clients/AttachmentGet.md) method by passing an appropriate identifier to it.
