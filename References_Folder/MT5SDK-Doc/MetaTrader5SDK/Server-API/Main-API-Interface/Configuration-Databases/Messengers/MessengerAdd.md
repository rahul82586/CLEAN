[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Messengers](../Messengers.md) / MessengerAdd

[Previous](MessengerUnsubscribe.md) | [Next](MessengerDelete.md)

# IMTServerAPI::MessengerAdd

Add or update a messenger configuration.
    
    
    MTAPIRES  IMTServerAPI::MessengerAdd(
       IMTConMessenger*  config  // Messenger configuration object
       )

### Parameters

**config**  
[in] Messenger configuration object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

When calling the method, a check is made whether the record already exists. If the record exists, it is updated, otherwise a new one is added. A key field for comparison is the configuration name [IMTConMessenger::Name()](../../../../Configuration-Interfaces/Messengers/IMTConMessenger/Name.md). When you try to add a completely identical record, no changes are made, and therefore the [IMTConMessengerSink::OnMessengerUpdate](../../../../Configuration-Interfaces/Messengers/IMTConMessengerSink/OnMessengerUpdate.md) notification method is not called.
