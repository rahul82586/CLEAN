[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Gateways](../Gateways.md) / GatewayUnsubscribe

[Previous](GatewaySubscribe.md) | [Next](GatewayAdd.md)

# IMTServerAPI::GatewayUnsubscribe

Unsubscribe from events and hooks associated with the gateway configuration.
    
    
    MTAPIRES  IMTServerAPI::GatewayUnsubscribe(
       IMTConGatewaySink*  sink      // A pointer to the IMTConGatewaySink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConGatewaySinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTServerAPI::GatewaySubscribe](GatewaySubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
