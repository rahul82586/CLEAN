[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [History Synchronization](../History-Synchronization.md) / HistorySyncAdd

[Previous](HistorySyncUnsubscribe.md) | [Next](HistorySyncDelete.md)

# IMTServerAPI::HistorySyncAdd

Add or update of a configuration of price data synchronization.
    
    
    MTAPIRES  IMTServerAPI::HistorySyncAdd(
       IMTConHistorySync*  config      // An object of configuration of price data synchronization
       )

### Parameters

**config**  
[in] An object of configuration of price data synchronization.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

When calling the method, a check is made whether the entry already exists. If the entry already exists, it is updated, otherwise a new entry is added. A key field for comparison is the address of the synchronization server [IMTConHistorySync::Server()](../../../../Configuration-Interfaces/History-Synchronization/IMTConHistorySync/Server.md). When you try to add a completely identical record, no changes are made, and therefore the [IMTConHisotrySyncSink::OnHistorySyncUpdate](../../../../Configuration-Interfaces/History-Synchronization/IMTConHistorySyncSink/OnHistorySyncUpdate.md) notification method is not called.
