[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_network

[Previous](mt5-holidays.md) | [Next](mt5-network-access-servers.md)

# mt5_network

Data on the platform [servers' general settings](../../../Platform-Setup/Network-cluster/Configuring-Servers.md) is exported to this table. The table contains the following fields:

Name | Type | Description  
Login | Integer | Server ID.  
Timestamp | Integer | A unique value within the table. Used by MetaTrader 5 servers for internal purposes. If the Timestamp of a record has changed, it means that the record has been changed.  
Type | Integer | Server type.  
Name | String | Server name.  
Address | String | Server address.  
Port | String | Server port.  
Adapter | String | Name of the currently used network controller.  
ServiceTime | Integer | Service time (time of optimization) when various operations aimed at increasing the performance and reliability of the platform are conducted. Specified in a number of minutes from 00:00. For example, 600 corresponds to 10:00.  
FailoverMode | Integer | Automatic [failover modes](../Switching-to.md): 

  * 0 — failover disabled
  * 1 — server is unavailable for most access servers
  * 2 — server is unavailable for all access servers

  
FailoverTimeout | Integer | Time in seconds, during which the server should be unavailable for monitoring servers to start switching to the backup server.  
Adapters | String | List of all available network controllers on PC (comma-separated).  
Addresses | String | List of available addresses for outgoing connections from this server (comma-separated).  
Binds | String | List of listen addresses (comma-separated).  
Points | String | List of public access points, via which connections are to be accepted.  
Version | Integer | Server version.  
Build | Integer | Server build.  
BuildDate | String | Server build date.  
SysConnection | Integer | Status of a server connection to the main trade server.  
SysLastBoot | DateTime | Time of the last server boot in the YYYY-MM-DD HH:MM:SS.MSC format.  
SysOsName | String | Operating system of the computer running the server.  
SysCpuName | String | Processor type of the computer that is running the server.  
SysCpuNumber | Integer | Number of CPU cores.  
SysBits | Integer | Operating system bits:

  * 32 — 32 bits
  * 64 — 64 bits
  * 0 — other

  
SysMemoryTotal | Integer | The total amount of RAM in megabytes.  
SysMemoryFree | Integer | The amount of free memory in megabytes.  
SysMemoryCritical | Integer | The critical amount of free memory in megabytes.  
SysHddSize | Integer | Total volume of a disk in megabytes.  
SysHddFree | Integer | Free memory on the disk in megabytes.  
SysHddCritical | Integer | Critical amount of free memory on the disk in megabytes.  
SysHddFragmentation | Integer | The current level of fragmentation of the server files in percentage.  
SysHddFragCritical | Integer | The critical level of fragmentation of the server files in percentage.  
SysDefragRecommend | Integer | The flag indicating that the operating system recommends defragmenting the disk:

  * 0 — no recommendation
  * 1 — recommendation is present

  
SysHddReadSpeed | Integer | The current speed of data reading from the disk in megabytes per second.  
SysHddReadCritical | Integer | The critical speed of data reading from the disk in megabytes per second.  
SysHddWriteSpeed | Integer | The current speed of saving data to the disk in megabytes per second.  
SysHddWriteCritical | Integer | The critical speed of saving data to the disk in megabytes per second.  
PerfConnectsMax | Integer | The maximum number of simultaneous connections to a server that has been achieved during the day.  
PerfConnectsCritical | Integer | Critical number of simultaneous connections to the server.  
PerfCpuMax | Integer | Get the maximum level of CPU usage in percentage for the current day.  
PerfCpuCritical | Integer | Get the critical level of CPU usage in percentage.  
PerfMemoryMin | Integer | The minimum size of free random access and virtual memory in megabytes per day.  
PerfMemoryCritical | Integer | The critical amount of free memory in megabytes.  
PerfMemBlockMin | Integer | The minimum value of the maximum memory block in megabytes per day.  
PerfMemBlockCritical | Integer | The critical value of the maximum memory block in megabytes per day.  
PerfNetworkMax | Integer | The maximum level of network usage in kilobytes per second for the current day.  
PerfNetworkCritical | Integer | The critical level of network usage in kilobytes per second.  
PerfSocketsMax | Integer | The maximum number of active sockets per day.  
PerfSocketsCritial | Integer | The critical number of active sockets.
