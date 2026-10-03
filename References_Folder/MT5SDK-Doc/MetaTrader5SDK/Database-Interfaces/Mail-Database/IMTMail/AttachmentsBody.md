[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Mail Database](../../Mail-Database.md) / [IMTMail](../IMTMail.md) / AttachmentsBody

[Previous](AttachmentsTotal.md) | [Next](AttachmentsSize.md)

# IMTMail::AttachmentsBody

Get the attachment body by its position.

C++
    
    
    LPVOID  IMTMail::AttachmentsBody(
       const UINT  pos      // Position of attachment
       )  const

.NET (Gateway/Manager API)
    
    
    byte[]  CIMTMail.AttachmentsBody(
       uint        pos      // Position of attachment
       )

### Parameters

**pos**  
[in] The position of an attached file in the list, starting with 0.

### Return Value

A pointer to the attachment body at the specified position.

### Note

The returned pointer is valid until the object is deleted by calling [IMTMail::Release](Release.md) or another object control method ([IMTMail::AttachmentsAdd](AttachmentsAdd.md) or [IMTMail::AttachmentsClear](AttachmentsClear.md)).
