[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Data Feeds](../Data-Feeds.md) / FeederSubscribe

[Previous](FeederTranslateCreate.md) | [Next](FeederUnsubscribe.md)

# IMTServerAPI::FeederSubscribe

Subscribe to events and hooks associated with the configuration of data feeds.
    
    
    MTAPIRES  IMTServerAPI::FeederSubscribe(
       IMTConFeederSink*  sink      // A pointer to the IMTConFeederSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConFeederSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTConFeederSink](../../../../Configuration-Interfaces/Data-Feeds/IMTConFeederSink.md) cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) is returned.
