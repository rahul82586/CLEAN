[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTAttachmentArray](../IMTAttachmentArray.md) / Next

[Previous](Total.md) | [Next](Sort.md)

# IMTAttachmentArray::Next

Get an attachment object by its position.

C++
    
    
    IMTAttachment*  IMTAttachmentArray::Next(
       const UINT  pos      // attachment position
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTAttachment  CIMTAttachmentArray.Next(
       uint        pos      // attachment position
       )

### Parameters

**pos**  
[in] Position of an attachment in the array, starting with 0.

### Return Value

If successful, it returns a pointer to the attachment object at the specified position. Otherwise NULL is returned.

### Note

The lifetime of the returned object is controlled by the current array object. Thus, if an array object is deleted, the returned pointer becomes invalid.
