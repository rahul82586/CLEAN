[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Data Feeds](../Data-Feeds.md) / FeederCreate

[Previous](../Data-Feeds.md) | [Next](FeederModuleCreate.md)

# IMTServerAPI::FeederCreate

Create an object of the data feed configuration.
    
    
    IMTConFeeder*  IMTServerAPI::FeederCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConFeeder](../../../../Configuration-Interfaces/Data-Feeds/IMTConFeeder.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConFeeder::Release](../../../../Configuration-Interfaces/Data-Feeds/IMTConFeeder/Release.md) method of this object.
