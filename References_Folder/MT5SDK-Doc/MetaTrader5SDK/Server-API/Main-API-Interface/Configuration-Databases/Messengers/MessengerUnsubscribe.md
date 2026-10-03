[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Messengers](../Messengers.md) / MessengerUnsubscribe

[Previous](MessengerSubscribe.md) | [Next](MessengerAdd.md)

# IMTServerAPI::MessengerUnsubscribe

Unsubscribe from events and hooks associated with messenger configurations.
    
    
    MTAPIRES  IMTServerAPI::MessengerUnsubscribe(
       IMTConMessengerSink*  sink   // A pointer to the IMTConMessengerSink object
       )

### Parameters

**sink**  
[in] A pointer to the object which implements theIMTConMessengerSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTServerAPI::MessengerSubscribe](MessengerSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
