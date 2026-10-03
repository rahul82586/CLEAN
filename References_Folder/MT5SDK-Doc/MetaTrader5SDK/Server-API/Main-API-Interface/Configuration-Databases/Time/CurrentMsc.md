[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Time](../Time.md) / CurrentMsc

[Previous](Current.md) | [Next](Get.md)

# IMTServerAPI::TimeCurrentMsc

Gets the current trading time with millisecond accuracy.
    
    
    INT64  IMTServerAPI::TimeCurrentMsc()

### Return Value

The current trading time of the platform - the number of milliseconds elapsed since 01.01.1970.

### Note

In all configurations, databases and logs, the platform trading time is used, except where explicitly stated otherwise.
