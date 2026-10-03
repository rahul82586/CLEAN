[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Messengers](../Messengers.md) / MessengerCreate

[Previous](../Messengers.md) | [Next](MessengerCountryCreate.md)

# IMTAdminAPI::MessengerCreate

Create a messenger configuration object.

C++
    
    
    IMTConMessenger*  IMTAdminAPI::MessengerCreate()

.NET
    
    
    CIMTConMessenger  CIMTAdminAPI.MessengerCreate()

### Return Value

Return the pointer to a created object implementing the [IMTConMessenger](../../../../Configuration-Interfaces/Messengers/IMTConMessenger.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTConMessenger::Release](../../../../Configuration-Interfaces/Messengers/IMTConMessenger/Release.md) method of this object.
