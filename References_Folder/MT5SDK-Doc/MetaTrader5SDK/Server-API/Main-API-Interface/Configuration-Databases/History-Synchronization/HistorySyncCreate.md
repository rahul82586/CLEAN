[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [History Synchronization](../History-Synchronization.md) / HistorySyncCreate

[Previous](../History-Synchronization.md) | [Next](HistorySyncSubscribe.md)

# IMTServerAPI::HistorySyncCreate

Create an object of configuration of price data synchronization.
    
    
    IMTConHistorySync*  IMTServerAPI::HistorySyncCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConHistorySync](../../../../Configuration-Interfaces/History-Synchronization/IMTConHistorySync.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTConHistorySync::Release](../../../../Configuration-Interfaces/History-Synchronization/IMTConHistorySync/Release.md) method of this object.
