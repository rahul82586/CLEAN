[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Mail Database](../Mail-Database.md) / MailDelete

[Previous](MailNext.md) | [Next](MailDeleteId.md)

# IMTAdminAPI::MailDelete

Delete a mail by a position in the mailbox.

C++
    
    
    MTAPIRES  IMTAdminAPI::MailDelete(
       const UINT  pos      // Position of the mail
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.MailDelete(
       uint        pos      // Position of the mail
       )

### Parameters

**pos**  
[in] Position of a mail in a mailbox ranging from 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
