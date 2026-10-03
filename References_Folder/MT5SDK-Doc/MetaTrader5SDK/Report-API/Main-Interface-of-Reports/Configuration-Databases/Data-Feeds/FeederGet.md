[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Data Feeds](../Data-Feeds.md) / FeederGet

[Previous](FeederNext.md) | [Next](FeederModuleTotal.md)

# IMTReportAPI::FeederGet

Gets the data feed configuration based on its name.
    
    
    MTAPIRES  IMTReportAPI::FeederGet(
       LPCWSTR        name,       // Name of the configuration
       IMTConFeeder*  feeder      // The object of data feed configuration
       )

### Parameters

**name**  
[in] The name of the configuration.

**feeder**  
[out] The object of configuration of a data feed. The feeder object must be first created using theIMTReportAPI::FeederCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConFeeder::Name()](../../../../Configuration-Interfaces/Data-Feeds/IMTConFeeder/Name.md) value is used as the name.
