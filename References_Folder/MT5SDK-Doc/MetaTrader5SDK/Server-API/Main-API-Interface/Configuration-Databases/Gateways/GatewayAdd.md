[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Gateways](../Gateways.md) / GatewayAdd

[Previous](GatewayUnsubscribe.md) | [Next](GatewayDelete.md)

# IMTServerAPI::GatewayAdd

Add or update a gateway configuration.
    
    
    MTAPIRES  IMTServerAPI::GatewayAdd(
       IMTConGateway*  gateway      // Gateway configuration object
       )

### Parameters

**gateway**  
[in] The gateway configuration object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

When calling the method, a check is made whether the entry already exists. If the entry already exists, it is updated, otherwise a new entry is added. A key field for comparison is the name of the configuration [IMTConGateway::Name()](../../../../Configuration-Interfaces/Gateways/IMTConGateway/Name.md). When you try to add a completely identical record, no changes are made, and therefore the [IMTConGatewaySink::OnGatewayUpdate](../../../../Configuration-Interfaces/Gateways/IMTConGatewaySink/OnGatewayUpdate.md) notification method is not called.
