[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Clients](../Clients.md) / AttachmentAddBatchArray

[Previous](AttachmentAddBatch.md) | [Next](AttachmentRequest.md)

# IMTManagerAPI::AttachmentAddBatchArray

Create attachment files for documents or comments in batch.

C++
    
    
    MTAPIRES  IMTManagerAPI::AttachmentAddBatchArray(
       IMTAttachment**  attachments,     // array of attachments
       const UINT       comments_total,  // number of attachments in the array
       MTAPIRES*        results          // array of results
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.AttachmentAddBatchArray(
       CIMTAttachment[] attachments,     // array of attachments
       MTRetCode[]      retcodes         // array of results
       )

### Parameters

**attachments**  
[in/out] Array ofattachment objects. You input ready descriptions of attachments. At the output, the server fills theIMTAttachment::RecordIDin these attachments.

**attachments_total**  
[in] The number of attachments in the 'attachments' array.

**results**  
[out] An array with attachment creation results. The size of the 'results' array must not be less than that of 'attachments'.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code means that all the specified comments have been created. The [MT_RET_ERR_PARTIAL](../../../Return-Codes/Common-errors.md) response code means that only some of the comments have been created. Analyze the 'results' array for more details of the execution results. The result of creation of each attachment from the 'attachments' array is added to 'results'. The index of a result corresponds to the index of an attachment in the source array.

### Note

Once the attachment identifier is received, you can add the attachment to a document or a request by calling the [IMTDocument::AttachmenAdd](../../../Database-Interfaces/Clients/IMTDocument/AttachmentsAdd.md) or [IMTComment::AttachmentAdd](../../../Database-Interfaces/Clients/IMTComment/AttachmentsAdd.md) respectively.
