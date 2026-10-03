[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Time](../Time.md) / Get

[Previous](Generation.md) | [Next](../Holidays.md)

# IMTReportAPI::TimeGet

Get the time configuration.
    
    
    MTAPIRES  IMTReportAPI::TimeGet(
       IMTConTime*  config      // An object of time configuration
       )

### Parameters

**config**  
[out] An object of the time configuration. The config object must first be created using theIMTReportAPI::TimeCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
