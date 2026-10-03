[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Server Services](../Server-Services.md) / ServerSubscribe

[Previous](ServerRestartRemote.md) | [Next](ServerUnsubscribe.md)

# IMTServerAPI::ServerSubscribe

Subscribe to events associated with server events.
    
    
    MTAPIRES  IMTServerAPI::ServerSubscribe(
       IMTServerSink*  sink      // A pointer at the IMTServerSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTServerSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTServerSink](../../Interface-of-Server-Events.md) cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../Return-Codes/Common-errors.md) is returned.
