[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Data Feeds](../Data-Feeds.md) / FeederModuleGet

[Previous](FeederModuleNext.md) | [Next](FeederRestart.md)

# IMTServerAPI::FeederModuleGet

Get the configuration of the data feed module by the name.
    
    
    MTAPIRES  IMTServerAPI::FeederModuleGet(
       LPCWSTR              name,       // Name of the configuration
       IMTConFeederModule*  module      // Object of configuration of a data feed module
       )

### Parameters

**name**  
[in] The name of the configuration.

**module**  
[out] The object of configuration of the data feed module. The module object must be first created using theIMTServerAPI::FeederModuleCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConFeederModule::Module()](../../../../Configuration-Interfaces/Data-Feeds/IMTConFeederModule/Module.md) value is used as the name.
