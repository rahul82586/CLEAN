[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / GroupUnsubscribe

[Previous](GroupSubscribe.md) | [Next](GroupAdd.md)

# IMTServerAPI::GroupUnsubscribe

Unsubscribe from events and hooks associated with the groups configuration.
    
    
    MTAPIRES  IMTServerAPI::GroupUnsubscribe(
       IMTConGroupSink*  sink      // A pointer to the IMTConGroupSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConGroupSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTServerAPI::GroupSubscribe](GroupSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
