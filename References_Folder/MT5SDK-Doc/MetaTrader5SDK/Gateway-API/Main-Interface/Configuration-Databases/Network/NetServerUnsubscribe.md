[🏠 Document Start](../../../../README.md) / [Gateway API](../../../README.md) / [Main Interface](../../../Main-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / NetServerUnsubscribe

[Previous](NetServerSubscribe.md) | [Next](NetServerTotal.md)

# IMTGatewayAPI::NetServerUnsubscribe

Unsubscribe from events associated with the configuration of the platform components.

C++
    
    
    MTAPIRES  IMTGatewayAPI::NetServerUnsubscribe(
       IMTConServerSink*  sink      // A pointer to the IMTConServerSink object
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.NetServerUnsubscribe(
       CIMTConServerSink  sink      // CIMTConServerSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConServerSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method is pared to [IMTGatewayAPI::NetServerSubscribe](NetServerSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
