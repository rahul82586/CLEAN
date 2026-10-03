[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [VPS](../VPS.md) / Set

[Previous](Get.md) | [Next](../KYC.md)

# IMTAdminAPI::VPSSet

Update VPS sponsorship settings.

C++
    
    
    MTAPIRES  IMTAdminAPI::VPSSet(
       IMTConVPS*  config  // VPS settings object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.VPSSet(
       CIMTConVPS  config  // VPS settings object
       )

Python
    
    
    AdminAPI.VPSSet(
       config      # VPS settings object
       )

### Parameters

**config**  
[in] Settings objectIMTConVPS.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
