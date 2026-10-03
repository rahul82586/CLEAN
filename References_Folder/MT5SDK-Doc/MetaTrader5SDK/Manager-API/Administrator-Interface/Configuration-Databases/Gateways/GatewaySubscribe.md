[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Gateways](../Gateways.md) / GatewaySubscribe

[Previous](GatewayTranslateCreate.md) | [Next](GatewayUnsubscribe.md)

# IMTAdminAPI::GatewaySubscribe

Subscribe to events associated with the gateway configuration.

C++
    
    
    MTAPIRES  IMTAdminAPI::GatewaySubscribe(
       IMTConGatewaySink*  sink      // A pointer to the IMTConGatewaySink object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.GatewaySubscribe(
       CIMTConGatewaySink  sink      // CIMTConGatewaySink object
       )

Python
    
    
    AdminAPI.GatewaySubscribe(
       sink                # IMTConGatewaySink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConGatewaySinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTConGatewaySink](../../../../Configuration-Interfaces/Gateways/IMTConGatewaySink.md) cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) is returned.
