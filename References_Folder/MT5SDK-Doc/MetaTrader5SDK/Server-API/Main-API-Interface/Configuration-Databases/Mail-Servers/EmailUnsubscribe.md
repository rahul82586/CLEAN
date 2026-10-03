[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Mail Servers](../Mail-Servers.md) / EmailUnsubscribe

[Previous](EmailSubscribe.md) | [Next](EmailAdd.md)

# IMTServerAPI::EmailUnsubscribe

Unsubscribe from events and hooks related to mail server configurations.
    
    
    MTAPIRES  IMTServerAPI::EmailUnsubscribe(
       IMTConEmailSink*   sink      // A pointer to the IMTConEmailSink object
       )

### Parameters

**sink**  
[in] A pointer to the object which implements theIMTConEmailSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTServerAPI::EmailSubscribe](EmailSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
