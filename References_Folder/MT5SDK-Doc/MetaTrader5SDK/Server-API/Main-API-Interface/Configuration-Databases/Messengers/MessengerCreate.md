[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Messengers](../Messengers.md) / MessengerCreate

[Previous](../Messengers.md) | [Next](MessengerCountryCreate.md)

# IMTServerAPI::MessengerCreate

Create a messenger configuration object.
    
    
    IMTConMessenger*  IMTServerAPI::MessengerCreate()

### Return Value

Return the pointer to a created object implementing the [IMTConMessenger](../../../../Configuration-Interfaces/Messengers/IMTConMessenger.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTConMessenger::Release](../../../../Configuration-Interfaces/Messengers/IMTConMessenger/Release.md) method of this object.
