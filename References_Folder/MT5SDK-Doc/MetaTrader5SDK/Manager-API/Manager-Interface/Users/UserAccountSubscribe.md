[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / UserAccountSubscribe

[Previous](UserCertConfirm.md) | [Next](UserAccountUnsubscribe.md)

# IMTManagerAPI::UserAccountSubscribe

Subscribe to receive events related to changes in the account trading state.

C++
    
    
    MTAPIRES  IMTManagerAPI::UserAccountSubscribe(
       IMTAccountSink*  sink    // A pointer to the IMTAccountSink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.UserAccountSubscribe(
       CIMTAccountSink  obj     // the CIMTAccountSink object
       )

Python
    
    
    ManagerAPI.UserAccountSubscribe(
       sink             # IMTAccountSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTAccountSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Event subscriptions are thread safe. One and the same [IMTAccountSink](../../../Database-Interfaces/Trade/Accounts/IMTAccountSink.md) interface cannot subscribe to an event twice. In this case, the [MT_RET_ERR_DUPLICATE](../../../Return-Codes/Common-errors.md) response code is returned.
