[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Gateways](../Gateways.md) / GatewayModuleGet

[Previous](GatewayModuleTotal.md) | [Next](GatewayModuleNext.md)

# IMTServerAPI::GatewayModuleGet

Get the gateway module by the name.
    
    
    MTAPIRES  IMTServerAPI::GatewayModuleGet(
       LPCWSTR               name,       // Name of the module
       IMTConGatewayModule*  module      // Object of the gateway module
       )

### Parameters

**name**  
[in] The name of the module.

**module**  
[out] The gateway module object. The module object must be first created using theIMTServerAPI::GatewayModuleCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConGatewayModule::Name](../../../../Configuration-Interfaces/Gateways/IMTConGatewayModule/Name.md) value is used as the name.
