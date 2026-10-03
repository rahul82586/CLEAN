[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Data Feeds](../Data-Feeds.md) / FeederNext

[Previous](FeederTotal.md) | [Next](FeederGet.md)

# IMTReportAPI::FeederNext

Gets a data feed configuration based on its index.
    
    
    MTAPIRES  IMTReportAPI::FeederNext(
       const UINT     pos,        // Position of the configuration
       IMTConFeeder*  feeder      // The object of data feed configuration
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**feeder**  
[out] The object of configuration of a data feed. The feeder object must be first created using theIMTReportAPI::FeederCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the configuration data of a feed with a specified index to the feeder object.
