[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Data Feeds](../Data-Feeds.md) / FeederModuleCreate

[Previous](FeederCreate.md) | [Next](FeederParamCreate.md)

# IMTReportAPI::FeederModuleCreate

Create an object of configuration of the data feed module.
    
    
    IMTConFeederModule*  IMTReportAPI::FeederModuleCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConFeederModule](../../../../Configuration-Interfaces/Data-Feeds/IMTConFeederModule.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTConFeederModule::Release](../../../../Configuration-Interfaces/Data-Feeds/IMTConFeederModule/Release.md) method of this object.
