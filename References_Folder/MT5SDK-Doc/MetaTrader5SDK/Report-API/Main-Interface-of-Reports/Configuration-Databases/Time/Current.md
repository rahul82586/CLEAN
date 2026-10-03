[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Time](../Time.md) / Current

[Previous](Create.md) | [Next](Generation.md)

# IMTReportAPI::TimeCurrent

Get the current trading time.
    
    
    INT64  IMTReportAPI::TimeCurrent()

### Return Value

The current trading time of the platform - the number of seconds elapsed since 01.01.1970.

### Note

In all configurations, databases and logs, the trading time of the platform is used, except where explicitly stated otherwise.
