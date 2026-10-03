[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Gateways](../Gateways.md) / GatewayGet

[Previous](GatewayNext.md) | [Next](GatewayModuleTotal.md)

# IMTServerAPI::GatewayGet

Get the gateway configuration by the name.
    
    
    MTAPIRES  IMTServerAPI::GatewayGet(
       LPCWSTR         name,        // Name of the configuration
       IMTConGateway*  gateway      // Gateway configuration object
       )

### Parameters

**name**  
[in] The name of the configuration.

**gateway**  
[out] The gateway configuration object. The gateway object must be first created using theIMTServerAPI::GatewayCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConGateway::Name](../../../../Configuration-Interfaces/Gateways/IMTConGateway/Name.md) value is used as the name.
