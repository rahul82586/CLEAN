[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Trade Requests](../Trade-Requests.md) / RequestSubscribe

[Previous](RequestArrayCreate.md) | [Next](RequestUnsubscribe.md)

# IMTGatewayAPI::RequestSubscribe

Subscribe to events associated with trade requests queue changes.

C++
    
    
    MTAPIRES  IMTGatewayAPI::RequestSubscribe(
       IMTRequestSink*  sink      // A pointer to the IMTRequestSink object
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.RequestSubscribe(
       CIMTRequestSink  sink      // CIMTRequestSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTRequestSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTRequestSink](../../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTRequestSink.md) cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../Return-Codes/Common-errors.md) is returned.
