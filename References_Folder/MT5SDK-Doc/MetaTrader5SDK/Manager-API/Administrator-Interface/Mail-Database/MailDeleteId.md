[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Mail Database](../Mail-Database.md) / MailDeleteId

[Previous](MailDelete.md) | [Next](MailSend.md)

# IMTAdminAPI::MailDeleteId

Delete a mail by an ID.

C++
    
    
    MTAPIRES  IMTAdminAPI::MailDeleteId(
       const UINT64  id      // Mail ID
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.MailDeleteId(
       ulong         id      // Mail ID
       )

### Parameters

**id**  
[in] The ID of the email that should be deleted.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTMail::Id](../../../Database-Interfaces/Mail-Database/IMTMail/ID.md) value is used as the identifier.
