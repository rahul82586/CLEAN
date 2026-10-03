[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Mail Servers](../Mail-Servers.md) / EmailCreate

[Previous](../Mail-Servers.md) | [Next](EmailSubscribe.md)

# IMTAdminAPI::EmailCreate

Create a mail server configuration object.

C++
    
    
    IMTConEmail*  IMTAdminAPI::EmailCreate()

.NET
    
    
    CIMTConEmail  CIMTAdminAPI.EmailCreate()

### Return Value

Returns a pointer to the created object which implements the [IMTConEmail](../../../../Configuration-Interfaces/Mail-Servers/IMTConEmail.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTConEmail::Release](../../../../Configuration-Interfaces/Mail-Servers/IMTConEmail/Release.md) method of this object.
