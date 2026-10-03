[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Mail Database](../../Mail-Database.md) / [IMTMail](../IMTMail.md) / AttachmentsClear

[Previous](AttachmentsAdd.md) | [Next](AttachmentsTotal.md)

# IMTMail::AttachmentsClear

Clear the list of files attached to an email.

C++
    
    
    MTAPIRES  IMTMail::AttachmentsClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTMail.AttachmentsClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method removes all attachments.
