[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Gateways](../Gateways.md) / GatewayModuleGet

[Previous](GatewayModuleTotal.md) | [Next](GatewayModuleNext.md)

# IMTAdminAPI::GatewayModuleGet

Get the gateway module by the name.

C++
    
    
    MTAPIRES  IMTAdminAPI::GatewayModuleGet(
       LPCWSTR               name,       // Name of the module
       IMTConGatewayModule*  module      // Object of the gateway module
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.GatewayModuleGet(
       string                name,       // Name of the configuration
       CIMTConGatewayModule  module      // Object of the gateway module
       )

Python
    
    
    AdminAPI.GatewayModuleGet(
       name                  # Name of the configuration
       )

### Parameters

**name**  
[in] The name of the module.

**module**  
[out] The gateway module object. The gateway object must be first created using theIMTAdminAPI::GatewayModuleCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConGatewayModule::Name](../../../../Configuration-Interfaces/Gateways/IMTConGatewayModule/Name.md) value is used as the name.
