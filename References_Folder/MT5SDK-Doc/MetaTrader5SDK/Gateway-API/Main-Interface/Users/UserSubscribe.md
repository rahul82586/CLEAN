[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Users](../Users.md) / UserSubscribe

[Previous](UserCreateAccount.md) | [Next](UserUnsubscribe.md)

# IMTGatewayAPI::UserSubscribe

Subscribe to events associated with changes in the client base.

C++
    
    
    MTAPIRES  IMTGatewayAPI::UserSubscribe(
       IMTUserSink*  sink      // A pointer to the IMTUserSink object
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.UserSubscribe(
       CIMTUserSink  sink      // CIMTUserSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTUserSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTUserSink](../../../Database-Interfaces/Users/IMTUserSink.md) cannot subscribe to events twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../Return-Codes/Common-errors.md) is returned.

  * [OnUserAdd](../../../Database-Interfaces/Users/IMTUserSink/OnUserAdd.md)
  * [OnUserUpdate](../../../Database-Interfaces/Users/IMTUserSink/OnUserUpdate.md)
  * [OnUserDelete](../../../Database-Interfaces/Users/IMTUserSink/OnUserDelete.md)
  * [OnUserSync](../../../Database-Interfaces/Users/IMTUserSink/OnUserSync.md)


