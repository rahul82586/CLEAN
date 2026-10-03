[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTAttachmentArray](../IMTAttachmentArray.md) / Add

[Previous](Clear.md) | [Next](AddCopy.md)

# IMTAttachmentArray::Add

Add an attachment object at the end of an array.

C++
    
    
    MTAPIRES  IMTAttachmentArray::Add(
       IMTAttachment*  attachment  // attachment to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAttachmentArray.Add(
       CIMTAttachment  attachment  // attachment to be added
       )

### Parameters

**attachment**  
[in]Attachment object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method places a pointer to a passed object at the end of an array. After a successful call of this method, the control over the life time of the "attachment" object is passed to the array object. Thus, when deleting an array object (by a call of [IMTAttachmentArray::Release](Release.md)), an earlier inserted object is automatically removed.

# IMTAttachmentArray::Add

Add an array of attachment objects to the end of an array.

C++
    
    
    MTAPIRES  IMTAttachmentArray::Add(
       IMTAttachmentArray*  array   // array of attachments to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAttachmentArray.Add(
       CIMTAttachmentArray  array    // array of attachments to be added
       )

### Parameters

**array**  
[in] Object of the array of attachments.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

This method places the pointers from the 'array' object to the end of the current array, and clears the 'array' object.

### The example
    
    
    //--- Example
       IMTAttachmentArray *array     =api->AttachmentCreateArray();   
       IMTAttachment      *attachment=api->AttachmentCreate();
    //---
       array->Add(attachment);  // after that the array controls the lifetime
       array->Delete(0);        // delete the first element, after which a pointer in 'attachment' becomes invalid ('Release' was called)
     
    //--- Incorrect use example
       IMTAttachmentArray *array     =api->AttachmentCreateArray();   
       IMTAttachment      *attachment=api->AttachmentCreate();
    //---
       array->Add(attachment);
       array->Add(attachment); // in this case, the array will contain two pointers to one and the same object!
       //--- an attempt to clear the array will lead to crash, because this will be an attempt to delete the object twice
