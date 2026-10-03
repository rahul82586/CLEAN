[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Data Feeds](../Data-Feeds.md) / FeederModuleCreate

[Previous](FeederCreate.md) | [Next](FeederParamCreate.md)

# IMTServerAPI::FeederModuleCreate

Create an object of configuration of the data feed module.
    
    
    IMTConFeederModule*  IMTServerAPI::FeederModuleCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConFeederModule](../../../../Configuration-Interfaces/Data-Feeds/IMTConFeederModule.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTConFeederModule::Release](../../../../Configuration-Interfaces/Data-Feeds/IMTConFeederModule/Release.md) method of this object.
