[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Messengers](../Messengers.md) / MessengerSubscribe

[Previous](MessengerTemplateCreate.md) | [Next](MessengerUnsubscribe.md)

# IMTServerAPI::MessengerSubscribe

Subscribe to events and hooks associated with messenger configurations.
    
    
    MTAPIRES  IMTServerAPI::MessengerSubscribe(
       IMTConMessengerSink*  sink   // A pointer to the IMTConMessengerSink object
       )

### Parameters

**sink**  
[in] A pointer to the object which implements theIMTConMessengerSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same [IMTConMessengerSink](../../../../Configuration-Interfaces/Messengers/IMTConMessengerSink.md) interface cannot subscribe to an event twice: in this case the [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) response code is returned.
