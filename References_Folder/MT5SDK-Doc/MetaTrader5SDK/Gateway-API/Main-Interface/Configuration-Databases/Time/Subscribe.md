[🏠 Document Start](../../../../README.md) / [Gateway API](../../../README.md) / [Main Interface](../../../Main-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Time](../Time.md) / Subscribe

[Previous](Create.md) | [Next](Unsubscribe.md)

# IMTGatewayAPI::TimeSubscribe

Subscribe to events and hooks associated with the time configuration.

C++
    
    
    MTAPIRES  IMTGatewayAPI::TimeSubscribe(
       IMTConTimeSink*  sink      // A pointer to the IMTConTimeSink object
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.TimeSubscribe(
       CIMTConTimeSink  sink      // CIMTConTimeSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConTimeSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTConTimeSink](../../../../Configuration-Interfaces/Time/IMTConSink.md) cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) is returned.
