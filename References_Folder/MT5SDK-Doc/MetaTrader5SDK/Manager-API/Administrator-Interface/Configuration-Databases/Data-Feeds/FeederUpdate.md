[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Data Feeds](../Data-Feeds.md) / FeederUpdate

[Previous](FeederRestart.md) | [Next](FeederUpdateBatch.md)

# IMTAdminAPI::FeederUpdate

Add and update a data feed configuration.

C++
    
    
    MTAPIRES  IMTAdminAPI::FeederUpdate(
       IMTConFeeder*  feeder      // The object of data feed configuration
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.FeederUpdate(
       CIMTConFeeder  feeder      // The object of data feed configuration
       )

Python
    
    
    AdminAPI.FeederUpdate(
       feeder         # The object of data feed configuration
       )

### Parameters

**feeder**  
[in] The object of data feed configuration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can be added or updated only from the applications that run on the main server. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/Common-errors.md) will be returned.
