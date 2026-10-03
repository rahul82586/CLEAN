[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Time](../Time.md) / Current

[Previous](Unsubscribe.md) | [Next](CurrentMsc.md)

# IMTServerAPI::TimeCurrent

Get the current trading time.
    
    
    INT64  IMTServerAPI::TimeCurrent()

### Return Value

The current trading time of the platform - the number of seconds elapsed since 01.01.1970.

### Note

In all configurations, databases and logs, the trading time of the platform is used, except where explicitly stated otherwise.
