[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTAttachmentArray](../IMTAttachmentArray.md) / Delete

[Previous](AddCopy.md) | [Next](Detach.md)

# IMTAttachmentArray::Delete

Delete an attachment object by its position.

C++
    
    
    MTAPIRES  IMTAttachmentArray::Delete(
       const UINT  pos      // attachment position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAttachmentArray.Delete(
       uint        pos      // attachment position
       )

### Parameters

**pos**  
[in] Position of an attachment in the array, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The deleted object will be automatically released by calling the [IMTAttachment::Release](../IMTAttachment/Release.md) method.
