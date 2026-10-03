[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_network_access_servers

[Previous](mt5-network.md) | [Next](mt5-network-history-servers.md)

# mt5_network_access_servers

Data on the [access servers settings](../../../Platform-Setup/Network-cluster/Configuring-Servers/Access-Server.md) is exported to this table. The table contains the following fields:

Name | Type | Description  
Login | Integer | Server ID.  
Priority | Integer | Base priority of the access server from 0 to 15. The special priority 255 (idle) designed to create backup access servers is possible as well.  
AntifloodEnable | Integer | Antiflood control: 0 — disabled, 1 — enabled.  
AntifloodConnects | Integer | The maximum number of connections from one IP address for a certain period of time, after which the address is temporarily blocked.  
AntifloodErrors | Integer | The maximum number of incorrect connections, after which the IP address is temporarily blocked.  
NewsMaxCount | Integer | The maximum number of news that can be stored on the access server.  
BalancingConnections | Integer | The current number of connections.  
BalancingPriority | Integer | The current priority of the access server.  
AccessMask | Integer | The allowed types of connection to the access server. Set as a sum of flag values:

  * 1 — client connections.
  * 2 — manager connections.
  * 4 — administrator connections.
  * 8 — connections via the Client API.
  * 16 — connections via the Manager API.


  * 32 — connections via the Web API.

For example, the value of 63 means that all connection types are allowed.  
AccessFlags | Integer | Additional server accessing flags:

  * 1 — the access server is [hidden from all terminals (#permissions)](../../../Platform-Setup/Network-cluster/Configuring-Servers/Access-Server.md#permissions) but is available for connection.

  
Servers | String | IDs of trade servers (comma-separated), the connection to which is implemented through this access server.
