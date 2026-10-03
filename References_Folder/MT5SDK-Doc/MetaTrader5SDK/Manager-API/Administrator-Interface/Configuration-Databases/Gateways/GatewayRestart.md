[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Gateways](../Gateways.md) / GatewayRestart

[Previous](GatewayUnsubscribe.md) | [Next](GatewayUpdate.md)

# IMTAdminAPI::GatewayRestart

Restart gateways.

C++
    
    
    MTAPIRES  IMTAdminAPI::GatewayRestart()

.NET
    
    
    MTRetCode  CIMTAdminAPI.GatewayRestart()

Python
    
    
    AdminAPI.GatewayRestart()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This command restarts all gateways.
