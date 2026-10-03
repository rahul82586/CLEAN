[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Data Feeds](../Data-Feeds.md) / FeederNext

[Previous](FeederTotal.md) | [Next](FeederGet.md)

# IMTAdminAPI::FeederNext

Gets a data feed configuration based on its index.

C++
    
    
    MTAPIRES  IMTAdminAPI::FeederNext(
       const UINT     pos,        // Position of the configuration
       IMTConFeeder*  feeder      // The object of data feed configuration
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.FeederNext(
       uint           pos,        // Position of the configuration
       CIMTConFeeder  feeder      // Position of the configuration
       )

Python
    
    
    AdminAPI.FeederNext(
       pos            # Position of the configuration
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**feeder**  
[out] The object of configuration of a data feed. The feeder object must be first created using theIMTAdminAPI::FeederCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the configuration data of a feed with a specified index to the feeder object.
