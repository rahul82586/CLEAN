[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [History Synchronization](../History-Synchronization.md) / HistorySyncSubscribe

[Previous](HistorySyncCreate.md) | [Next](HistorySyncUnsubscribe.md)

# IMTAdminAPI::HistorySyncSubscribe

Subscribe to events associated with the configuration of price data synchronization.

C++
    
    
    MTAPIRES  IMTAdminAPI::HistorySyncSubscribe(
       IMTConHistorySyncSink*  sink      // A pointer to the IMTConHistorySyncSink object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.HistorySyncSubscribe(
       CIMTConHistorySyncSink  sink      // CIMTConHistorySyncSink object
       )

Python
    
    
    AdminAPI.HistorySyncSubscribe(
       sink                   # IMTConHistorySyncSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConHistorySyncSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTConHistorySyncSink](../../../../Configuration-Interfaces/History-Synchronization/IMTConHistorySyncSink.md) cannot subscribe to events twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) is returned.
