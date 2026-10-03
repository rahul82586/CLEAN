[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Gateways](../Gateways.md) / GatewayNext

[Previous](GatewayTotal.md) | [Next](GatewayGet.md)

# IMTAdminAPI::GatewayNext

Get the gateway configuration by the index.

C++
    
    
    MTAPIRES  IMTAdminAPI::GatewayNext(
       const UINT      pos,         // Position of the configuration
       IMTConGateway*  gateway      // Gateway configuration object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.GatewayNext(
       uint            pos,         // Position of the configuration
       CIMTConGateway  gateway      // Gateway configuration object
       )

Python
    
    
    AdminAPI.GatewayNext(
       pos             # Position of the configuration
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**gateway**  
[out] The gateway configuration object. The gateway object must be first created using theIMTAdminAPI::GatewayCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the configuration data of a gateway with a specified index to the gateway object.
