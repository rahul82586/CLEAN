[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Clients](../Clients.md) / AttachmentRequest

[Previous](AttachmentAddBatchArray.md) | [Next](../Users.md)

# IMTAdminAPI::AttachmentRequest

Get attachments by identifiers.

C++
    
    
    MTAPIRES  IMTAdminAPI::AttachmentRequest(
       const UINT64*        attachment_ids,       // array of identifiers
       const UINT           attachment_ids_total, // number of identifiers in the array
       IMTAttachmentArray*  attachments           // array of attachments
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.AttachmentRequest(
       ulong[]              attachment_ids,       // array of identifiers
       CIMTAttachmentArray  attachments           // array of attachments
       )

### Parameters

**attachment_ids**  
[in] An array of attachment identifiers (IMTAttachment::RecordID).

**attachment_ids_total**  
[in] The number of identifiers in the attachment_ids array.

**attachments**  
[out] An array of attachment objects. The 'attachments' object must first be created using theIMTAdminAPI::AttachmentCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The method copies data of attachments with the specified IDs, to the 'attachments' object.
