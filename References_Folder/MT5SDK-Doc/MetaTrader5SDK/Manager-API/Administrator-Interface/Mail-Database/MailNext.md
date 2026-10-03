[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Mail Database](../Mail-Database.md) / MailNext

[Previous](MailTotal.md) | [Next](MailDelete.md)

# IMTAdminAPI::MailNext

Get an email by a position in the mailbox.

C++
    
    
    MTAPIRES  IMTAdminAPI::MailNext(
       const UINT  pos,      // Mail position
       IMTMail*    mail      // Mail object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.MailNext(
       uint        pos,      // Mail position
       CIMTMail    mail      // Mail object
       )

### Parameters

**pos**  
[in] Position of a message in a mailbox ranging from 0.

**mail**  
[out] An object of the mail. The mail object must be first created using theIMTAdminAPI::MailCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method copies data of the mail at the specified position to the mail object. The method is valid only if the [IMTAdminAPI::PUMP_MODE_MAIL](../Connection-to-the-Server/Pumping-Modes.md) pumping mode was specified during connection.
