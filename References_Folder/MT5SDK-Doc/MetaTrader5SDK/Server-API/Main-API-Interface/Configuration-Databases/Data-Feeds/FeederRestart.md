[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Data Feeds](../Data-Feeds.md) / FeederRestart

[Previous](FeederModuleGet.md) | [Next](../Time.md)

# IMTServerAPI::FeederRestart

Restart data feeds.
    
    
    MTAPIRES  IMTServerAPI::FeederRestart()

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The execution of this command restarts all data feeds.
