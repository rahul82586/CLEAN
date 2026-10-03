[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Data Feeds](../Data-Feeds.md) / FeederCreate

[Previous](../Data-Feeds.md) | [Next](FeederModuleCreate.md)

# IMTAdminAPI::FeederCreate

Create an object of the data feed configuration.

C++
    
    
    IMTConFeeder*  IMTAdminAPI::FeederCreate()

.NET
    
    
    CIMTConFeeder  CIMTAdminAPI.FeederCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConFeeder](../../../../Configuration-Interfaces/Data-Feeds/IMTConFeeder.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConFeeder::Release](../../../../Configuration-Interfaces/Data-Feeds/IMTConFeeder/Release.md) method of this object.
