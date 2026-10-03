[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Data Feeds](../Data-Feeds.md) / FeederModuleGet

[Previous](FeederModuleNext.md) | [Next](../Time.md)

# IMTAdminAPI::FeederModuleGet

Get the configuration of the data feed module by the name.

C++
    
    
    MTAPIRES  IMTAdminAPI::FeederModuleGet(
       LPCWSTR              name,       // Name of the configuration
       IMTConFeederModule*  module      // Object of configuration of a data feed module
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.FeederModuleGet(
       string               name,       // Name of the configuration
       CIMTConFeederModule  module      // Object of configuration of a data feed module
       )

Python
    
    
    AdminAPI.FeederModuleGet(
       name                 # Name of the configuration
       )

### Parameters

**name**  
[in] The name of the configuration.

**module**  
[out] The object of configuration of the data feed module. The module object must be first created using theIMTAdminAPI::FeederModuleCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConFeederModule::Module()](../../../../Configuration-Interfaces/Data-Feeds/IMTConFeederModule/Module.md) value is used as the name.
