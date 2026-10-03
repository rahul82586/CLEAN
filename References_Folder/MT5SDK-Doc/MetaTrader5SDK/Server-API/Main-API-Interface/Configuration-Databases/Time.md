[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Configuration Databases](../Configuration-Databases.md) / Time

[Previous](Data-Feeds/FeederRestart.md) | [Next](Time/Create.md)

# Time Configuration

MetaTrader 5 Server API allows managing global time settings of a trading platform: adjust working time, retrieve and change the time zone and the address of the server for synchronizing time.

Functions described in this section allow managing the time configurations of the platform, as well subscribe and unsubscribe from events associated with its change.

Function | Purpose  
---|---  
[TimeCreate](Time/Create.md) | Create an object of the time configuration.  
[TimeSubscribe](Time/Subscribe.md) | Subscribe to events and hooks associated with the time configuration.  
[TimeUnsubscribe](Time/Unsubscribe.md) | Unsubscribe from events and hooks associated with the time configuration.  
[TimeCurrent](Time/Current.md) | Get the current trading time.  
[TimeCurrentMsc](Time/CurrentMsc.md) | Gets the current trading time with millisecond accuracy.  
[TimeGet](Time/Get.md) | Get the time configuration.  
[TimeSet](Time/Set.md) | Set the time configuration.
