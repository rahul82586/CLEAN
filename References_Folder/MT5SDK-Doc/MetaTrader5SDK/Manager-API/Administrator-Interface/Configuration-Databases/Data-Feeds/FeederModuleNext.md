[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Data Feeds](../Data-Feeds.md) / FeederModuleNext

[Previous](FeederModuleTotal.md) | [Next](FeederModuleGet.md)

# IMTAdminAPI::FeederModuleNext

Get the configuration of the data feed module by the index.

C++
    
    
    MTAPIRES  IMTAdminAPI::FeederModuleNext(
       const UINT           pos,        // Position of the configuration
       IMTConFeederModule*  module      // The object of data feed configuration
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.FeederModuleNext(
       uint                 pos,        // Position of the configuration
       CIMTConFeederModule  module      // The object of data feed configuration
       )

Python
    
    
    AdminAPI.FeederModuleNext(
       pos                  # Position of the configuration
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**module**  
[out] The object of configuration of a data feed. The module object must be first created using theIMTAdminAPI::FeederModuleCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the configuration of a data feed module with a specified index to the module object.
