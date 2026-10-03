[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Mail Servers](../Mail-Servers.md) / EmailAdd

[Previous](EmailUnsubscribe.md) | [Next](EmailDelete.md)

# IMTServerAPI::EmailAdd

Add or update a mail server configuration.
    
    
    MTAPIRES  IMTServerAPI::EmailAdd(
       IMTConEmail*  config     // Mail server configuration object
       )

### Parameters

**config**  
[in] Mail server configuration object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

When calling the method, a check is made whether the record already exists. If the record exists, it is updated, otherwise a new one is added. A key field for comparison is the configuration name [IMTConEmail::Name()](../../../../Configuration-Interfaces/Mail-Servers/IMTConEmail/Name.md). When you try to add a completely identical record, no changes are made, and therefore the [IMTConEmailSink::OnEmailUpdate](../../../../Configuration-Interfaces/Mail-Servers/IMTConEmailSink/OnEmailUpdate.md) notification method is not called.
