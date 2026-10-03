[🏠 Document Start](../../../../README.md) / [Gateway API](../../../README.md) / [Main Interface](../../../Main-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Time](../Time.md) / Unsubscribe

[Previous](Subscribe.md) | [Next](Current.md)

# IMTGatewayAPI::TimeUnsubscribe

Unsubscribe from events and hooks associated with the time configuration.

C++
    
    
    MTAPIRES  IMTGatewayAPI::TimeUnsubscribe(
       IMTConTimeSink*  sink      // A pointer to the IMTConTimeSink object
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.TimeUnsubscribe(
       CIMTConTimeSink  sink      // CIMTConTimeSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConTimeSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTGatewayAPI::TimeSubscribe](Subscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
