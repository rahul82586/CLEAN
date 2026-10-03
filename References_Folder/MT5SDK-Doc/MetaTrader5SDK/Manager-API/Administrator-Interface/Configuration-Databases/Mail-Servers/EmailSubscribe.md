[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Mail Servers](../Mail-Servers.md) / EmailSubscribe

[Previous](EmailCreate.md) | [Next](EmailUnsubscribe.md)

# IMTAdminAPI::EmailSubscribe

Subscribe to events and hooks related to mail server configurations.

C++
    
    
    MTAPIRES  IMTAdminAPI::EmailSubscribe(
       IMTConEmailSink*   sink      // A pointer to the IMTConEmailSink object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.EmailSubscribe(
       CIMTConEmailSink   sink      // The CIMTConEmailSink object
       )

Python
    
    
    AdminAPI.EmailSubscribe(
       sink               # IMTConEmailSink object
       )

### Parameters

**sink**  
[in] A pointer to the object which implements theIMTConEmailSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same [IMTConEmailSink](../../../../Configuration-Interfaces/Mail-Servers/IMTConEmailSink.md) interface cannot subscribe to an event twice: in this case the [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) response code is returned.
