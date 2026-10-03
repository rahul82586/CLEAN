[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Mail Servers](../Mail-Servers.md) / EmailUnsubscribe

[Previous](EmailSubscribe.md) | [Next](EmailUpdate.md)

# IMTAdminAPI::EmailUnsubscribe

Unsubscribe from events and hooks related to mail server configurations.

C++
    
    
    MTAPIRES  IMTAdminAPI::EmailUnsubscribe(
       IMTConEmailSink*   sink      // A pointer to the IMTConEmailSink object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.EmailUnsubscribe(
       CIMTConEmailSink  sink      // The CIMTConEmailSink object
       )

Python
    
    
    AdminAPI.EmailUnsubscribe(
       sink              # IMTConEmailSink object
       )

### Parameters

**sink**  
[in] A pointer to the object which implements theIMTConEmailSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTServerAPI::EmailSubscribe](../../../../Server-API/Main-API-Interface/Configuration-Databases/Mail-Servers/EmailSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
