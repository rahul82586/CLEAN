[🏠 Document Start](../../../../README.md) / [Gateway API](../../../README.md) / [Main Interface](../../../Main-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / GroupUnsubscribe

[Previous](GroupSubscribe.md) | [Next](GroupTotal.md)

# IMTGatewayAPI::GroupUnsubscribe

Unsubscribe from events and hooks associated with the groups configuration.

C++
    
    
    MTAPIRES  IMTGatewayAPI::GroupUnsubscribe(
       IMTConGroupSink*  sink      // A pointer to the IMTConGroupSink object
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.GroupUnsubscribe(
       CIMTConGroupSink  sink      // CIMTConGroupSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConGroupSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTGatewayAPI::GroupSubscribe](GroupSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
