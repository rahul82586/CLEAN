[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Gateways](../Gateways.md) / GatewayUpdate

[Previous](GatewayRestart.md) | [Next](GatewayUpdateBatch.md)

# IMTAdminAPI::GatewayUpdate

Add or update a gateway configuration.

C++
    
    
    MTAPIRES  IMTAdminAPI::GatewayUpdate(
       IMTConGateway*  gateway      // Gateway configuration object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.GatewayUpdate(
       CIMTConGateway  gateway      // Gateway configuration object
       )

Python
    
    
    AdminAPI.GatewayUpdate(
       gateway         # Gateway configuration object
       )

### Parameters

**gateway**  
[in] The gateway configuration object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can be added or updated only from the applications that run on the main server. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned.
