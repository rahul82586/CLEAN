[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / UserAccountUnsubscribe

[Previous](UserAccountSubscribe.md) | [Next](UserAccountGet.md)

# IMTManagerAPI::UserAccountUnsubscribe

Unsubscribe from the events related to changes in the account trading state.

C++
    
    
    MTAPIRES  IMTManagerAPI::UserAccountUnsubscribe(
       IMTAccountSink*  sink    // A pointer to the IMTAccountSink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.UserAccountUnsubscribe(
       CIMTAccountSink  obj     // the CIMTAccountSink object
       )

Python
    
    
    ManagerAPI.UserAccountUnsubscribe(
       sink             # IMTAccountSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTAccountSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method is paired with [IMTManagerAPI::UserAccountSubscribe](UserAccountSubscribe.md). If an attempt is made to unsubscribe from the interface that has not been previously subscribed to, the [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) error is returned.
