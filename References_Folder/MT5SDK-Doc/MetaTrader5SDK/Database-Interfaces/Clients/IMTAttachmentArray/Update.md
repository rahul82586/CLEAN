[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTAttachmentArray](../IMTAttachmentArray.md) / Update

[Previous](Detach.md) | [Next](UpdateCopy.md)

# IMTAttachmentArray::Update

Change an attachment at the specified position of the array.

C++
    
    
    MTAPIRES  IMTAttachmentArray::Update(
       const UINT      pos,        // position
       IMTAttachment*  attachment  // attachment object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAttachmentArray.Update(
       uint            pos,        // position
       CIMTAttachment  attachment  // attachment object
       )

### Parameters

**pos**  
[in] Position of an attachment in the array, starting with 0.

**attachment**  
[in]Attachment object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The IMTAttachmentArray::Update method deletes the previous element ([IMTAttachment::Release](../IMTAttachment/Release.md) call) and replaces it with a new one. After that, the lifetime of a new element is controlled by an array object. Thus, when deleting an array object (by a call of IMTAttachmentArray::Release), an earlier inserted object is automatically removed.

### The example
    
    
    //--- Example
       IMTAttachmentArray *array      =api->AttachmentCreateArray();   
       IMTAttachment      *attachment1=api->AttachmentCreate();
       IMTAttachment      *attachment2=api->AttachmentCreate();
    //---
       array->Add(attachment1);
       array->Update(0,attachment2); // the first element (the attachment1 object) is replaced by attachment2
       //--- after that the attachment1 element will be released via Release, and the attachment2 lifetime will be controlled by the array
