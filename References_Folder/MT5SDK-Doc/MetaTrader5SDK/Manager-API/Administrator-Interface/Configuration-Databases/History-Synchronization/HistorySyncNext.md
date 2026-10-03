[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [History Synchronization](../History-Synchronization.md) / HistorySyncNext

[Previous](HistorySyncTotal.md) | [Next](../Gateways.md)

# IMTAdminAPI::HistorySyncNext

Get a configuration of price data synchronization based on its index.

C++
    
    
    MTAPIRES  IMTAdminAPI::HistorySyncNext(
       const UINT          pos,        // Position of the configuration
       IMTConHistorySync*  config      // An object of configuration of price data synchronization
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.HistorySyncNext(
       uint                pos,        // Position of the configuration
       CIMTConHistorySync  config      // An object of configuration of price data synchronization
       )

Python
    
    
    AdminAPI.HistorySyncNext(
       pos                 # Position of the configuration
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**config**  
[out] An object of configuration of price data synchronization. The config object must first be created using theIMTAdminAPI::HistorySyncCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the synchronization configuration entry with a specified index to the config object.
