[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Mail Servers](../Mail-Servers.md) / EmailNext

[Previous](EmailTotal.md) | [Next](EmailGet.md)

# IMTAdminAPI::EmailNext

Get a mail server configuration by index.

C++
    
    
    MTAPIRES  IMTAdminAPI::EmailNext(
       const UINT     pos,        // Configuration position
       IMTConEmail*   email       // Mail server configuration object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.EmailNext(
       uint           pos,        // Configuration position
       CIMTConEmail   email       // Email configuration object
       )

Python
    
    
    AdminAPI.EmailNext(
       pos            # Configuration position
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**email**  
[out] Mail server configuration object. The 'email' object must be previously created using theIMTAdminAPI::EmailCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method copies mail server configuration data with the specified index to the 'email' object.
