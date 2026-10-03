[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Common](../Common.md) / Get

[Previous](Unsubscribe.md) | [Next](Set.md)

# IMTAdminAPI::CommonGet

Gets the common platform configuration.

C++
    
    
    MTAPIRES  IMTAdminAPI::CommonGet(
       IMTConCommon*  common      // IMTConCommon object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.CommonGet(
       CIMTConCommon  common      // CIMTConCommon object
       )

Python
    
    
    AdminAPI.CommonGet()

### Parameters

**common**  
[out] An object of the common configuration. The object must first be created using theIMTAdminAPI::CommonCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
