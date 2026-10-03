[🏠 Document Start](../../../../README.md) / [Gateway API](../../../README.md) / [Main Interface](../../../Main-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / NetServerSubscribe

[Previous](NetServerRangeCreate.md) | [Next](NetServerUnsubscribe.md)

# IMTGatewayAPI::NetServerSubscribe

Subscribe to events associated with the configuration of the platform components.

C++
    
    
    MTAPIRES  IMTGatewayAPI::NetServerSubscribe(
       IMTConServerSink*  sink      // A pointer to the IMTConServerSink object
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.NetServerSubscribe(
       CIMTConServerSink  sink      // CIMTConServerSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConServerSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTConServerSink](../../../../Configuration-Interfaces/Network/IMTConServerSink.md) cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) is returned.
