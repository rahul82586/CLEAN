[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Mail Servers](../Mail-Servers.md) / EmailGet

[Previous](EmailNext.md) | [Next](EmailSend.md)

# IMTAdminAPI::EmailGet

Get a mail server configuration by name.

C++
    
    
    MTAPIRES  IMTAdminAPI::EmailGet(
       LPCWSTR        name,       // Configuration name
       IMTConEmail*   email       // Mail server configuration object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.EmailGet(
       string         name,       // Configuration name
       CIMTConEmail   email       // Mail server configuration object
       )

Python
    
    
    AdminAPI.EmailGet(
       name           # Configuration name
       )

### Parameters

**name**  
[in] The name of the configuration.

**email**  
[out] Mail server configuration object. The 'email' object must be previously created using theIMTAdminAPI::EmailCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConEmail::Name](../../../../Configuration-Interfaces/Mail-Servers/IMTConEmail/Name.md) value is used for the name.
