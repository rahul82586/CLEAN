[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Mail Servers](../Mail-Servers.md) / EmailGet

[Previous](EmailNext.md) | [Next](EmailSend.md)

# IMTServerAPI::EmailGet

Get a mail server configuration by name.
    
    
    MTAPIRES  IMTServerAPI::EmailGet(
       LPCWSTR        name,       // Configuration name
       IMTConEmail*   email       // Mail server configuration object
       )

### Parameters

**name**  
[in] The name of the configuration.

**email**  
[out] Mail server configuration object. The 'email' object must be previously created using theIMTServerAPI::EmailCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConEmail::Name](../../../../Configuration-Interfaces/Mail-Servers/IMTConEmail/Name.md) value is used for the name.
