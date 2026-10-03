[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Time](../Time.md) / Get

[Previous](Unsubscribe.md) | [Next](Server.md)

# IMTManagerAPI::TimeGet

Get the time configuration.

C++
    
    
    MTAPIRES  IMTManagerAPI::TimeGet(
       IMTConTime*  config      // An object of time configuration
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.TimeGet(
       CIMTConTime  config      // An object of time configuration
       )

Python
    
    
    ManagerAPI.TimeGet()

### Parameters

**config**  
[out] An object of the time configuration. The config object must first be created using theIMTManagerAPI::TimeCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method is valid only if the [IMTManagerAPI::PUMP_MODE_TIME](../../Connection-to-the-Server/Pumping-Modes.md) pumping mode was specified during connection.
