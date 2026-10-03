[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Clients](../Clients.md) / AttachmentRequest

[Previous](AttachmentAddBatchArray.md) | [Next](../Users.md)

# IMTManagerAPI::AttachmentRequest

Get attachments by identifiers.

C++
    
    
    MTAPIRES  IMTManagerAPI::AttachmentRequest(
       const UINT64*        attachment_ids,       // array of identifiers
       const UINT           attachment_ids_total, // number of identifiers in the array
       IMTAttachmentArray*  attachments           // array of attachments
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.AttachmentRequest(
       ulong[]              attachment_ids,       // array of identifiers
       CIMTAttachmentArray  attachments           // array of attachments
       )

### Parameters

**attachment_ids**  
[in] An array of attachment identifiers (IMTAttachment::RecordID).

**attachment_ids_total**  
[in] The number of identifiers in the attachment_ids array.

**attachments**  
[out] An array of attachment objects. The 'attachments' object must be previously created using theIMTManagerAPI::AttachmentCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The method copies data of attachments with the specified IDs, to the 'attachments' object.
