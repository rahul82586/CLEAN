[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTAttachmentArray](../IMTAttachmentArray.md) / Detach

[Previous](Delete.md) | [Next](Update.md)

# IMTAttachmentArray::Detach

Detach an attachment object from an array.

C++
    
    
    IMTAttachment*  IMTAttachmentArray::Detach(
       const UINT  pos      // attachment position
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTAttachment  CIMTAttachmentArray.Detach(
       uint        pos      // attachment position
       )

### Parameters

**pos**  
[in] Position of an attachment in the array, starting with 0.

### Return Value

Returns a pointer to the detached attachment object.

### Note

This method removes a pointer to the object at the given position of the array and returns it. The size of the array is decreased by one, and the deleted object is not released.
