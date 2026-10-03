[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Time](../Time.md) / Set

[Previous](Get.md) | [Next](Server.md)

# IMTAdminAPI::TimeSet

Set the time configuration.

C++
    
    
    MTAPIRES  IMTAdminAPI::TimeSet(
       const IMTConTime*  config      // An object of time configuration
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.TimeSet(
       CIMTConTime        config      // An object of time configuration
       )

Python
    
    
    AdminAPI.TimeSet(
       config             # An object of time configuration
       )

### Parameters

**config**  
[in] An object of time configuration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
