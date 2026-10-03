[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [VPS](../VPS.md) / Get

[Previous](Unsubscribe.md) | [Next](Set.md)

# IMTAdminAPI::VPSGet

Get VPS sponsorship settings.

C++
    
    
    MTAPIRES  IMTAdminAPI::VPSGet(
       IMTConVPS*  config  // VPS settings object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.VPSGet(
       CIMTConVPS  config  // VPS settings object
       )

Python
    
    
    AdminAPI.VPSGet()

### Parameters

**config**  
[out] Settings objectIMTConVPS. The 'config' object must be previously created using theIMTAdminAPI::VPSCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
