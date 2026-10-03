[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Trade Requests](../Trade-Requests.md) / RequestUnsubscribe

[Previous](RequestSubscribe.md) | [Next](RequestTotal.md)

# IMTGatewayAPI::RequestUnsubscribe

Unsubscribe from events associated with requests queue changes.

C++
    
    
    MTAPIRES  IMTGatewayAPI::RequestUnsubscribe(
       IMTRequestSink*  sink      // A pointer to the IMTRequestSink object
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.RequestUnsubscribe(
       CIMTRequestSink  sink      // CIMTRequestSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTRequestSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTGatewayAPI::RequestSubscribe](RequestSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) error is returned.
