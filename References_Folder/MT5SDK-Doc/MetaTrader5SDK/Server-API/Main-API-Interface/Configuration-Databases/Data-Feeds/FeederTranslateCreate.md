[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Data Feeds](../Data-Feeds.md) / FeederTranslateCreate

[Previous](FeederParamCreate.md) | [Next](FeederSubscribe.md)

# IMTServerAPI::FeederTranslateCreate

Create an object of setup of converting the information transmitted from a data feed.
    
    
    IMTConFeederTranslate*  IMTServerAPI::FeederTranslateCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConFeederTranslate](../../../../Configuration-Interfaces/Data-Feeds/IMTConFeederTranslate.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConFeederTranslate::Release](../../../../Configuration-Interfaces/Data-Feeds/IMTConFeederTranslate/Release.md) method of this object.
