[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Messengers](../Messengers.md) / MessengerTemplateCreate

[Previous](MessengerGroupCreate.md) | [Next](MessengerSubscribe.md)

# IMTServerAPI::MessengerTemplateCreate

Create a message template object that will be used in the messenger.
    
    
    IMTConMessengerTemplate*  IMTServerAPI::MessengerTemplateCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTConMessengerTemplate](../../../../Configuration-Interfaces/Messengers/IMTConMessengerTemplate.md) interface. On failure, NULL is returned.

### Note

The created object must be destroyed by calling its [IMTConMessengerTemplate::Release](../../../../Configuration-Interfaces/Messengers/IMTConMessengerTemplate/Release.md) method.
