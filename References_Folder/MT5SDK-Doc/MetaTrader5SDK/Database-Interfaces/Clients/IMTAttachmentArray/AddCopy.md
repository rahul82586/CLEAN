[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTAttachmentArray](../IMTAttachmentArray.md) / AddCopy

[Previous](Add.md) | [Next](Delete.md)

# IMTAttachmentArray::AddCopy

Add a copy of an attachment object to the end of an array.

C++
    
    
    MTAPIRES  IMTAttachmentArray::AddCopy(
       const IMTAttachment*  attachment  // attachment to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAttachmentArray.AddCopy(
       CIMTAttachment        attachment  // attachment to be added
       )

### Parameters

**attachment**  
[in]Attachment object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The method creates a copy of the attachment object and inserts it at the end of the array.

# IMTAttachmentArray::AddCopy

Add copies of attachment objects to an array.

C++
    
    
    MTAPIRES  IMTAttachmentArray::AddCopy(
       const IMTAttachmentArray*  array     // array of attachments to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAttachmentArray.AddCopy(
       CIMTAttachmentArray        array      // array of attachments to be added
       )

### Parameters

**array**  
[in] Object of the array of attachments.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method creates a copy of attachment objects belonging to the 'array' object and inserts them at the end of the current array.
