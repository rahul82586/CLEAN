[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [History Synchronization](../History-Synchronization.md) / HistorySyncUnsubscribe

[Previous](HistorySyncSubscribe.md) | [Next](HistorySyncAdd.md)

# IMTServerAPI::HistorySyncUnsubscribe

Unsubscribe from events and hooks associated with the configuration of price data synchronization.
    
    
    MTAPIRES  IMTServerAPI::HistorySyncUnsubscribe(
       IMTConHistorySyncSink*  sink      // A pointer to the IMTConHistorySyncSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConHistorySyncSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTServerAPI::HistorySyncSubscribe](HistorySyncSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
