[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Gateways](../Gateways.md) / GatewayModuleNext

[Previous](GatewayModuleGet.md) | [Next](GatewayPositionRequest.md)

# IMTAdminAPI::GatewayModuleNext

Get the gateway module by the index.

C++
    
    
    MTAPIRES  IMTAdminAPI::GatewayModuleNext(
       const UINT            pos,        // Position of the module
       IMTConGatewayModule*  module      // Object of the gateway module
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.GatewayModuleNext(
       uint                  pos,        // Position of the module
       CIMTConGatewayModule  module      // Object of the gateway module
       )

Python
    
    
    AdminAPI.GatewayModuleNext(
       pos                   # Position of the module
       )

### Parameters

**pos**  
[in] Position of the module, starting with 0.

**module**  
[out] The gateway module object. The gateway object must be first created using theIMTAdminAPI::GatewayModuleCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the gateway configuration with a specified index to the module object.
