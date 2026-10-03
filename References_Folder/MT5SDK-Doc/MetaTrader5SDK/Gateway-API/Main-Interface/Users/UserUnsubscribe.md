[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Users](../Users.md) / UserUnsubscribe

[Previous](UserSubscribe.md) | [Next](UserTotal.md)

# IMTGatewayAPI::UserUnsubscribe

Unsubscribe from events associated with changes in the client base.

C++
    
    
    MTAPIRES  IMTGatewayAPI::UserUnsubscribe(
       IMTUserSink*  sink      // A pointer to the IMTUserSink object
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.UserUnsubscribe(
       CIMTUserSink  sink      // CIMTUserSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTUserSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method is pared to [IMTGatewayAPI::UserSubscribe](UserSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) error is returned.
