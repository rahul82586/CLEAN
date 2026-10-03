[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Data Feeds](../Data-Feeds.md) / FeederGet

[Previous](FeederNext.md) | [Next](FeederModuleTotal.md)

# IMTAdminAPI::FeederGet

Gets the data feed configuration based on its name.

C++
    
    
    MTAPIRES  IMTAdminAPI::FeederGet(
       LPCWSTR        name,       // Name of the configuration
       IMTConFeeder*  feeder      // The object of data feed configuration
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.FeederGet(
       string         name,       // Name of the configuration
       CIMTConFeeder  feeder      // The object of data feed configuration
       )

Python
    
    
    AdminAPI.FeederGet(
       name           # Name of the configuration
       )

### Parameters

**name**  
[in] The name of the configuration.

**feeder**  
[out] The object of configuration of a data feed. The feeder object must be first created using theIMTAdminAPI::FeederCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConFeeder::Name()](../../../../Configuration-Interfaces/Data-Feeds/IMTConFeeder/Name.md) value is used as the name.
