[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Mail Database](../Mail-Database.md) / MailDelete

[Previous](MailNext.md) | [Next](MailDeleteId.md)

# IMTManagerAPI::MailDelete

Delete a mail by a position in the mailbox.

C++
    
    
    MTAPIRES  IMTManagerAPI::MailDelete(
       const UINT  pos      // Position of the mail
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.MailDelete(
       uint        pos      // Position of the mail
       )

### Parameters

**pos**  
[in] Position of a mail in a mailbox ranging from 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
