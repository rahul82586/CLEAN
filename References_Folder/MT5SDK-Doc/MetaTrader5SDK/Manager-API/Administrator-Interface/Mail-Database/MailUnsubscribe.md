[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Mail Database](../Mail-Database.md) / MailUnsubscribe

[Previous](MailSubscribe.md) | [Next](MailTotal.md)

# IMTAdminAPI::MailUnsubscribe

Undubscribe from events associated with changes in the mail database.

C++
    
    
    MTAPIRES  IMTAdminAPI::MailUnsubscribe(
       IMTMailSink*  sink      // A pointer at the IMTMailSink object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.MailUnsubscribe(
       CIMTMailSink  sink      // CIMTMailSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTMailSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTAdminAPI::MailSubscribe](MailSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) error is returned.
