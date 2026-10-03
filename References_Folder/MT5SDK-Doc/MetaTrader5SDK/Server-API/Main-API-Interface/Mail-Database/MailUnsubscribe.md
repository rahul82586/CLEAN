[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Mail Database](../Mail-Database.md) / MailUnsubscribe

[Previous](MailSubscribe.md) | [Next](MailSend.md)

# IMTServeAPI::MailUnsubscribe

Undubscribe from events and hooks associated with changes in the mail database.
    
    
    MTAPIRES  IMTServerAPI::MailUnsubscribe(
       IMTMailSink*  sink      // A pointer at the IMTMailSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTMailSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTServerAPI::MailSubscribe](MailSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) error is returned.
