[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [History Synchronization](../History-Synchronization.md) / HistorySyncNext

[Previous](HistorySyncTotal.md) | [Next](../Gateways.md)

# IMTServerAPI::HistorySyncNext

Get a configuration of price data synchronization based on its index.
    
    
    MTAPIRES  IMTServerAPI::HistorySyncNext(
       const UINT          pos,        // Position of the configuration
       IMTConHistorySync*  config      // An object of configuration of price data synchronization
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**config**  
[out] An object of configuration of price data synchronization. The config object must first be created using theIMTServerAPI::HistorySyncCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the synchronization configuration entry with a specified index to the config object.
