[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_network_history_servers

[Previous](mt5-network-access-servers.md) | [Next](mt5-network-trade-servers.md)

# mt5_network_history_servers

Data on the [history server settings](../../../Platform-Setup/Network-cluster/Configuring-Servers/History-Server.md) is exported to this table. The table contains the following fields:

Name | Type | Description  
Login | Integer | Server ID.  
DatafeedsTimeout | Integer | Timeout of data feeds before switching to other ones. Specified in seconds.  
NewsMax | Integer | The maximum number of news that can be stored on the history server.
