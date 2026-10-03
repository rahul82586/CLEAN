[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Time](../Time.md) / Set

[Previous](Get.md) | [Next](../Holidays.md)

# IMTServerAPI::TimeSet

Set the time configuration.
    
    
    MTAPIRES  IMTServerAPI::TimeSet(
       const IMTConTime*  config      // An object of time configuration
       )

### Parameters

**config**  
[in] An object of time configuration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

When setting a configuration, a check is made whether changes are added. If there are no changes, no update is made and therefore the [IMTConTimeSink::OnTimeUpdate](../../../../Configuration-Interfaces/Time/IMTConTimeSink/IMTConSink-OnUpdate.md) notification method is not called.
