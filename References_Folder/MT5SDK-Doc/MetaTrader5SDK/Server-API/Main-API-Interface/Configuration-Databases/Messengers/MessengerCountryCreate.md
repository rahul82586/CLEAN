[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Messengers](../Messengers.md) / MessengerCountryCreate

[Previous](MessengerCreate.md) | [Next](MessengerGroupCreate.md)

# IMTServerAPI::MessengerCountryCreate

Create an object of a country for which the messenger will be used.
    
    
    IMTConMessengerCountry*  IMTServerAPI::MessengerCountryCreate()

### Return Value

The method returns a pointer to the created object that implements the [IMTConMessengerCountry](../../../../Configuration-Interfaces/Messengers/IMTConMessengerCountry.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTConMessengerCountry::Release](../../../../Configuration-Interfaces/Messengers/IMTConMessengerCountry/Release.md) method of this object.
