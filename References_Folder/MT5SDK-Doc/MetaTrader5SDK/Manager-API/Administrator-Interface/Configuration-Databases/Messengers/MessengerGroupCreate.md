[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Messengers](../Messengers.md) / MessengerGroupCreate

[Previous](MessengerCountryCreate.md) | [Next](MessengerTemplateCreate.md)

# IMTAdminAPI::MessengerGroupCreate

Create an object of an account group for which the messenger will be used.

C++
    
    
    IMTConMessengerGroup*  IMTAdminAPI::MessengerGroupCreate()

.NET
    
    
    CIMTConMessengerGroup  CIMTAdminAPI.MessengerGroupCreate()

### Return Value

The method returns a pointer to the created object that implements the [IMTConMessengerGroup](../../../../Configuration-Interfaces/Messengers/IMTConMessengerGroup.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTConMessengerGroup::Release](../../../../Configuration-Interfaces/Messengers/IMTConMessengerGroup/Release.md) method of this object.
