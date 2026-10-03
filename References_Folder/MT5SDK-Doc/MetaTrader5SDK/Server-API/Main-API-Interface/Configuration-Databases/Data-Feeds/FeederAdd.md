[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Data Feeds](../Data-Feeds.md) / FeederAdd

[Previous](FeederUnsubscribe.md) | [Next](FeederDelete.md)

# IMTServerAPI::FeederAdd

Adds or updates a data feed configuration.
    
    
    MTAPIRES  IMTServerAPI::FeederAdd(
       IMTConFeeder*  feeder      // The object of data feed configuration
       )

### Parameters

**feeder**  
[in] The object of data feed configuration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

When calling the method, a check is made whether the entry already exists. If the entry already exists, it is updated, otherwise a new entry is added. A key field for comparison is the name of the configuration [IMTConFeeder:: Name ()](../../../../Configuration-Interfaces/Data-Feeds/IMTConFeeder/Name.md). When you try to add a completely identical record, no changes are made, and therefore the [IMTConFeederSink::OnFeederUpdate](../../../../Configuration-Interfaces/Data-Feeds/IMTConFeederSink/OnFeederUpdate.md) notification method is not called.
