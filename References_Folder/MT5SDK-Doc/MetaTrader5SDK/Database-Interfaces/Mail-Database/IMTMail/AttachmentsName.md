[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Mail Database](../../Mail-Database.md) / [IMTMail](../IMTMail.md) / AttachmentsName

[Previous](AttachmentsSize.md) | [Next](../IMTMailSink.md)

# IMTMail::AttachmentsName

Get the name of an attachment by its position.

C++
    
    
    LPCWSTR  IMTMail::AttachmentsName(
       const UINT  pos      // File position
       )  const

.NET (Gateway/Manager API)
    
    
    string  CIMTMail.AttachmentsName(
       uint        pos      // File position
       )

### Parameters

**pos**  
[in] The position of an attached file in the list, starting with 0.

### Return Value

If successful, it returns a pointer to a string with the file name. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTMail](../IMTMail.md) object.
