[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Data Feeds](../Data-Feeds.md) / FeederRestart

[Previous](FeederUnsubscribe.md) | [Next](FeederUpdate.md)

# IMTAdminAPI::FeederRestart

Restart data feeds.

C++
    
    
    MTAPIRES  IMTAdminAPI::FeederRestart()

.NET
    
    
    MTRetCode  CIMTAdminAPI.FeederRestart()

Python
    
    
    AdminAPI.FeederRestart()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This command restarts all data feeds.
