[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [History Synchronization](../History-Synchronization.md) / HistorySyncUpdate

[Previous](HistorySyncStart.md) | [Next](HistorySyncUpdateBatch.md)

# IMTAdminAPI::HistorySyncUpdate

Add or update of a configuration of price data synchronization.

C++
    
    
    MTAPIRES  IMTAdminAPI::HistorySyncUpdate(
       IMTConHistorySync*  config      // An object of configuration of price data synchronization
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.HistorySyncUpdate(
       CIMTConHistorySync  config      // An object of configuration of price data synchronization
       )

Python
    
    
    AdminAPI.HistorySyncUpdate(
       config              # An object of configuration of price data synchronization
       )

### Parameters

**config**  
[in] An object of configuration of price data synchronization.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can be added or updated only from the applications that run on the main server. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned.
