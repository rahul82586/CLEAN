[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTAttachmentArray](../IMTAttachmentArray.md) / UpdateCopy

[Previous](Update.md) | [Next](Shift.md)

# IMTAttachmentArray::UpdateCopy

Change an attachment at the specified position of an array by copying the parameters of a passed attachment object.

C++
    
    
    MTAPIRES  IMTAttachmentArray::UpdateCopy(
       const UINT            pos,        // position
       const IMTAttachment*  attachment  // attachment object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAttachmentArray.UpdateCopy(
       uint                  pos,        // position
       CIMTAttachment        attachment  // attachment object
       )

### Parameters

**pos**  
[in] Position of an attachment in the array, starting with 0.

**attachment**  
[in]Attachment object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method copies the 'attachment' object parameters to the attachment object at the specified position in the array.
