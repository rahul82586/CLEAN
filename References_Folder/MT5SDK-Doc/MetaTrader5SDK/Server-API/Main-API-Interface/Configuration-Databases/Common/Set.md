[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Common](../Common.md) / Set

[Previous](Get.md) | [Next](../Network.md)

# IMTServerAPI::CommonSet

Sets the common platform configuration.
    
    
    MTAPIRES  IMTServerAPI::CommonSet(
       const IMTConCommon*  common      // An object of configuration
       )

### Parameters

**common**  
[in] An object of the common configuration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

When setting a configuration, a check is made whether changes are added. If there are no changes, no update is made and therefore the [IMTConCommonSink::OnCommonUpdate](../../../../Configuration-Interfaces/Common/IMTConCommonSink/IMTConSink-OnUpdate.md) notification method is not called.
