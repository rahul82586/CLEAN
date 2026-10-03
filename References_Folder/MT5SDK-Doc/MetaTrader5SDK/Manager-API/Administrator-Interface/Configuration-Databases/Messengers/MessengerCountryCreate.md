[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Messengers](../Messengers.md) / MessengerCountryCreate

[Previous](MessengerCreate.md) | [Next](MessengerGroupCreate.md)

# IMTAdminAPI::MessengerCountryCreate

Create an object of a country for which the messenger will be used.

C++
    
    
    IMTConMessengerCountry*  IMTAdminAPI::MessengerCountryCreate()

.NET
    
    
    CIMTConMessengerCountry  CIMTAdminAPI.MessengerCountryCreate()

### Return Value

The method returns a pointer to the created object that implements the [IMTConMessengerCountry](../../../../Configuration-Interfaces/Messengers/IMTConMessengerCountry.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTConMessengerCountry::Release](../../../../Configuration-Interfaces/Messengers/IMTConMessengerCountry/Release.md) method of this object.
