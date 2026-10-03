[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / GroupSubscribe

[Previous](GroupTierCreate.md) | [Next](GroupUnsubscribe.md)

# IMTServerAPI::GroupSubscribe

Subscribe to events and hooks associated with the groups configuration.
    
    
    MTAPIRES  IMTServerAPI::GroupSubscribe(
       IMTConGroupSink*  sink      // A pointer to the IMTConGroupSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConGroupSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTConGroupSink](../../../../Configuration-Interfaces/Groups/IMTConGroupSink.md) cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) is returned.
