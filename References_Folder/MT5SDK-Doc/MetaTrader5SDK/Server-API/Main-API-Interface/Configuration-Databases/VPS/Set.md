[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [VPS](../VPS.md) / Set

[Previous](Get.md) | [Next](../KYC.md)

# IMTServerAPI::VPSSet

Update VPS sponsorship settings.
    
    
    MTAPIRES  IMTServerAPI::VPSSet(
       const IMTConVPS*  config  // VPS settings object
       )

### Parameters

**config**  
[in] Settings objectIMTConVPS.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
