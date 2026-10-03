[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Mail Database](../../Mail-Database.md) / [IMTMail](../IMTMail.md) / AttachmentsAdd

[Previous](BodySize.md) | [Next](AttachmentsClear.md)

# IMTMail::AttachmentsAdd

Attach a file to an email.

C++
    
    
    MTAPIRES  IMTMail::AttachmentsAdd(
       LPCWSTR      filename,            // Name of the attachment
       LPCVOID      attachment,          // Body of the attachment
       const UINT   attachment_size      // File size
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTMail.AttachmentsAdd(
       string       filename,            // Name of the attachment
       byte[]       attachment           // Body of the attachment
       )

### Parameters

**filename**  
[in] The name of the attachment that will be displayed in the email.

**attachment**  
[in] Attachment body.

**attachment_size**  
[in] File size in bytes, which will be displayed in the email.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
