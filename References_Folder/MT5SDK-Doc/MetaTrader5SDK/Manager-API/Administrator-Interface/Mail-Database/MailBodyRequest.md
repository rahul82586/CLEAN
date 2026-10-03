[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Mail Database](../Mail-Database.md) / MailBodyRequest

[Previous](MailSend.md) | [Next](../News-Database.md)

# IMTAdminAPI::MailBodyRequest

Get an email body.

C++
    
    
    MTAPIRES  IMTAdminAPI::MailBodyRequest(
       const UINT64  id,     // email ID
       IMTMail*      mail    // an email object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.MailBodyRequest(
       ulong         id,     // email ID
       CIMTMail      mail    // an email object
       )

### You should use these inputs;

**pos**  
[in] The ID of the email received by the manager. TheIMTMail::Idvalue is used as the identifier.

**mail**  
[out] An email object. The 'mail' object must be first created using theIMTAdminAPI::MailCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Further Note

To prevent from the slowdown of the API performance and from unnecessary traffic, the server sends large emails without bodies and attachments. If [IMTMail::BodySize](../../../Database-Interfaces/Mail-Database/IMTMail/Body.md) is equal to 0, request the email body using the IMTAdminAPI::MailBodyRequest method and pass to it the ID of the received email [IMTMail::Id](../../../Database-Interfaces/Mail-Database/IMTMail/ID.md).
