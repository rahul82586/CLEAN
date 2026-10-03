[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / UserUnsubscribe

[Previous](UserSubscribe.md) | [Next](UserAdd.md)

# IMTManagerAPI::UserUnsubscribe

Unsubscribe from events associated with changes in the client base.

C++
    
    
    MTAPIRES  IMTManagerAPI::UserUnsubscribe(
       IMTUserSink*  sink      // A pointer to the IMTUserSink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.UserUnsubscribe(
       CIMTUserSink  obj       // CIMTUserSink object
       )

Python
    
    
    ManagerAPI.UserUnsubscribe(
       sink          # IMTUserSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTUserSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTManagerAPI::UserSubscribe](UserSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) error is returned.
