[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Configuration Databases](../Configuration-Databases.md) / Data Feeds

[Previous](Plugins/PluginModuleGet.md) | [Next](Data-Feeds/FeederCreate.md)

# Data Feed Configuration

To receive quotes and news in the online trading platform, data feeds are used. Data feeds transmit information to the history server, from which they are translated to access points (data centers) and terminals.

Functions described in this section allow managing the data feed configurations, as well subscribe and unsubscribe from events associated with their change.

Function | Purpose  
---|---  
[FeederCreate](Data-Feeds/FeederCreate.md) | Create an object of the data feed configuration.  
[FeederModuleCreate](Data-Feeds/FeederModuleCreate.md) | Create an object of configuration of the data feed module.  
[FeederParamCreate](Data-Feeds/FeederParamCreate.md) | Create an object of the parameter of the data feeds.  
[FeederTranslateCreate](Data-Feeds/FeederTranslateCreate.md) | Create an object of setup of converting the information transmitted from a data feed.  
[FeederSubscribe](Data-Feeds/FeederSubscribe.md) | Subscribe to events and hooks associated with the configuration of data feeds.  
[FeederUnsubscribe](Data-Feeds/FeederUnsubscribe.md) | Unsubscribe from events and hooks associated with the configuration of data feeds.  
[FeederAdd](Data-Feeds/FeederAdd.md) | Adds or updates a data feed configuration.  
[FeederDelete](Data-Feeds/FeederDelete.md) | Delete a data feed configuration by name and by index  
[FeederShift](Data-Feeds/FeederShift.md) | Change the position of the data feed configuration in the list.  
[FeederTotal](Data-Feeds/FeederTotal.md) | The total number of data feed configurations available in the platform.  
[FeederNext](Data-Feeds/FeederNext.md) | Gets a data feed configuration based on its index.  
[FeederGet](Data-Feeds/FeederGet.md) | Gets the data feed configuration based on its name.  
[FeederModuleTotal](Data-Feeds/FeederModuleTotal.md) | The total number of configurations of data feed modules (EXE files) available in the platform.  
[FeederModuleNext](Data-Feeds/FeederModuleNext.md) | Get the configuration of the data feed module by the index.  
[FeederModuleGet](Data-Feeds/FeederModuleGet.md) | Get the configuration of the data feed module by the name.  
[FeederRestart](Data-Feeds/FeederRestart.md) | Restart data feeds.
