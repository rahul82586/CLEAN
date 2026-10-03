[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Gateways](../Gateways.md) / GatewayGet

[Previous](GatewayNext.md) | [Next](GatewayModuleTotal.md)

# IMTAdminAPI::GatewayGet

Get the gateway configuration by the name.

C++
    
    
    MTAPIRES  IMTAdminAPI::GatewayGet(
       LPCWSTR         name,        // Name of the configuration
       IMTConGateway*  gateway      // Gateway configuration object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.GatewayGet(
       string          name,        // Name of the configuration
       CIMTConGateway  gateway      // Gateway configuration object
       )

Python
    
    
    AdminAPI.GatewayGet(
       name            # Name of the configuration
       )

### Parameters

**name**  
[in] The name of the configuration.

**gateway**  
[out] The gateway configuration object. The gateway object must be first created using theIMTAdminAPI::GatewayCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConGateway::Name()](../../../../Configuration-Interfaces/Gateways/IMTConGateway/Name.md) value is used as the name.
