[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / UserSubscribe

[Previous](UserCreateAccountArray.md) | [Next](UserUnsubscribe.md)

# IMTManagerAPI::UserSubscribe

Subscribe to events associated with changes in the client base.

C++
    
    
    MTAPIRES  IMTManagerAPI::UserSubscribe(
       IMTUserSink*  sink      // A pointer to the IMTUserSink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.UserSubscribe(
       CIMTUserSink  obj       // CIMTUserSink object
       )

Python
    
    
    ManagerAPI.UserSubscribe(
       sink          # IMTUserSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTUserSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTUserSink](../../../Database-Interfaces/Users/IMTUserSink.md) cannot subscribe to events twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../Return-Codes/Common-errors.md) is returned.
