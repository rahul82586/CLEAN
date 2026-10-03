[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Time](../Time.md) / Get

[Previous](Unsubscribe.md) | [Next](Set.md)

# IMTAdminAPI::TimeGet

Get the time configuration.

C++
    
    
    MTAPIRES  IMTAdminAPI::TimeGet(
       IMTConTime*  config      // An object of time configuration
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.TimeGet(
       CIMTConTime  config      // An object of time configuration
       )

Python
    
    
    AdminAPI.TimeGet()

### Parameters

**config**  
[out] An object of the time configuration. The config object must first be created using theIMTAdminAPI::TimeCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
