[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Mail Servers](../Mail-Servers.md) / EmailSubscribe

[Previous](EmailCreate.md) | [Next](EmailUnsubscribe.md)

# IMTServerAPI::EmailSubscribe

Subscribe to events and hooks related to mail server configurations.
    
    
    MTAPIRES  IMTServerAPI::EmailSubscribe(
       IMTConEmailSink*   sink      // A pointer to the IMTConEmailSink object
       )

### Parameters

**sink**  
[in] A pointer to the object which implements theIMTConEmailSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same [IMTConEmailSink](../../../../Configuration-Interfaces/Mail-Servers/IMTConEmailSink.md) interface cannot subscribe to an event twice: in this case the [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) response code is returned.
