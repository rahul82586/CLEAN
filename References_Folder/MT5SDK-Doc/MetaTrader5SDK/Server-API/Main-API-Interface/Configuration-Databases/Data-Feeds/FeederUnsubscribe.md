[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Data Feeds](../Data-Feeds.md) / FeederUnsubscribe

[Previous](FeederSubscribe.md) | [Next](FeederAdd.md)

# IMTServerAPI::FeederUnsubscribe

Unsubscribe from events and hooks associated with the configuration of data feeds.
    
    
    MTAPIRES  IMTServerAPI::FeederUnsubscribe(
       IMTConFeederSink*  sink      // A pointer to the IMTConFeederSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConFeederSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTServerAPI::FeederSubscribe](FeederSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
