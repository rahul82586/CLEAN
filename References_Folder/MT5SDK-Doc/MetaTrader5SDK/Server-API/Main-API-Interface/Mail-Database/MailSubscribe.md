[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Mail Database](../Mail-Database.md) / MailSubscribe

[Previous](MailCreate.md) | [Next](MailUnsubscribe.md)

# IMTServeAPI::MailSubscribe

Subscribe to events and hooks associated with changes in the mail database.
    
    
    MTAPIRES  IMTServerAPI::MailSubscribe(
       IMTMailSink*  sink      // A pointer at the IMTMailSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTMailSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTMailSink](../../../Database-Interfaces/Mail-Database/IMTMailSink.md) cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../Return-Codes/Common-errors.md) is returned.
