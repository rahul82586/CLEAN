[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Mail Database](../../Mail-Database.md) / [IMTMail](../IMTMail.md) / AttachmentsSize

[Previous](AttachmentsBody.md) | [Next](AttachmentsName.md)

# IMTMail::AttachmentsSize

Get the size of an attachment by its position.

C++
    
    
    UINT  IMTMail::AttachmentsSize(
       const UINT  pos      // File position
       )  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTMail.AttachmentsSize(
       uint        pos      // File position
       )

### Parameters

**pos**  
[in] The position of an attached file in the list, starting with 0.

### Return Value

The size of an attachment at the specified position in bytes.
