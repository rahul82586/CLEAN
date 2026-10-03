[🏠 Document Start](../../../../README.md) / [Gateway API](../../../README.md) / [Main Interface](../../../Main-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Time](../Time.md) / Get

[Previous](Current.md) | [Next](../Network.md)

# IMTGatewayAPI::TimeGet

Get the time configuration.

C++
    
    
    MTAPIRES  IMTGatewayAPI::TimeGet(
       IMTConTime*  config      // An object of time configuration
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.TimeGet(
       CIMTConTime  config      // An object of time configuration
       )

### Parameters

**config**  
[out] An object of the time configuration. The config object must first be created using theIMTGatewayAPI::TimeCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [MT_RET_OK_NONE](../../../../Return-Codes/Successful-completion.md) response means that the time settings have not been yet initialized on the Gateway API side. Time settings can only be requested after receiving the [IMTGatewaySink::OnGatewayStart](../../../Event-Interface/OnGatewayStart.md) event.
