[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Server Services](../Server-Services.md) / ServerUnsubscribe

[Previous](ServerSubscribe.md) | [Next](../Geo-Services.md)

# IMTServerAPI::ServerUnsubscribe

Undubscribe from events associated with server events.
    
    
    MTAPIRES  IMTServerAPI::ServerUnsubscribe(
       IMTServerSink*  sink      // A pointer at the IMTServerSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTServerSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTServerAPI::ServerSubscribe](ServerSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) error is returned.
