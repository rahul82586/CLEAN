[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Mail Servers](../Mail-Servers.md) / EmailUpdate

[Previous](EmailUnsubscribe.md) | [Next](EmailUpdateBatch.md)

# IMTAdminAPI::EmailUpdate

Add or update a mail server configuration.

C++
    
    
    MTAPIRES  IMTAdminAPI::EmailUpdate(
       IMTConEmail*  config     // Mail server configuration object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.EmailUpdate(
       CIMTConEmail  config     // Mail server configuration object
       )

Python
    
    
    AdminAPI.EmailUpdate(
       config        # Mail server configuration object
       )

### Parameters

**config**  
[in] Mail server configuration object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can only be added or updated from the applications running on the main server. For all other plugins the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned.
