[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / Data Structure

[Previous](../Network.md) | [Next](Add-Server.md)

<a id="data-structure"></a>
# Data Structure (#data-structure)

The group configuration is passed in JSON format as a response to [/api/server/add](Add-Server.md) and [/api/server/get](Get-Server-by-Index.md) parameters.

<a id="server"></a>
## Common Server Parameters (#server)

Parameter | Type | Description  
Type | Integer | Server type. Passed in a value of the [EnFailoverModes (#enservertypes)](../../../../Configuration-Interfaces/Network/IMTConServer/Enumerations.md#enservertypes) enumeration.  
Name | String | Server name.  
Address | String | Server address.  
Login | Integer | Server ID.  
Adapter | String | The current network adapter.  
ServiceTime | Integer | Service time (time of optimization) when various operations aimed at increasing the platform performance and reliability are conducted. Specified in minutes elapsed since 00:00.  
Adapters | Array of strings | An array describing available network adapters.  
Addresses | Array of strings | Array with the description of available network addresses.  
Binds | Array of strings | Array with binding addresses descriptions.  
Points | Array of strings | Array with the server access points descriptions.  
TradeServer | Array | Array with the description of [trade server (#trade)](Data-Structure.md#trade) specific parameters.  
HistoryServer | Array | Array with the description of [history server (#history)](Data-Structure.md#history) specific parameters.  
AccessServer | Array | Array with the description of [access server (#access)](Data-Structure.md#access) specific parameters.  
BackupServer | Array | Array with the description of [backup server (#backup)](Data-Structure.md#backup) specific parameters.  
AntiDDosServer | Array | Array with the description of [Anti DDoS server (#antiddos)](Data-Structure.md#antiddos) specific parameters.  
FailoverMode | Integer | Automatic failover mode. Passed in a value of the [EnFailoverModes (#enfailovermodes)](../../../../Configuration-Interfaces/Network/IMTConServer/Enumerations.md#enfailovermodes) enumeration.  
FailoverTime | Integer | Downtime of the primary server, after which the platform switches to a backup server. This is done in seconds.  
ServerState | Array | Array with the [server state (#state)](Data-Structure.md#state) description.  
ServerData | Array | Array with the description of [server update parameters (#data)](Data-Structure.md#data).  
  
<a id="state"></a>
## Server State (#state)

Parameter | Type | Description  
Version | Integer | Server version.  
Build | Float | Server build.  
BuildDate | DateTime | Server build date.  
SysOsName | String | The operating system of the computer on which the server is running.  
SysLastBoot | String | Time of the last server boot in the YYYY-MM-DD HH:MM:SS.MSC format.  
SysBits | String | Operating system bit.  
SysConnection | String | Status of a server connection to the main trade server.  
SysCpuName | String | Processor type of the computer on which the server is running.  
SysCpuNumber | Integer | Number of CPU cores.  
SysMemoryTotal | Integer | The total amount of RAM in megabytes.  
SysMemoryFree | Integer | The amount of free memory in megabytes.  
SysMemoryCritical | Integer | The critical amount of free memory in megabytes.  
SysHddSize | Integer | Total hard disk capacity in megabytes.  
SysHddFree | Integer | Free memory on the hard disk in megabytes.  
SysHddCritical | Integer | Critical amount of free memory on the hard disk in megabytes.  
SysHddFragmentation | Integer | The current file fragmentation level on the server, in percentage.  
SysHdFragCritical | Integer | The critical level of file fragmentation on the server in percentage.  
SysHddReadSpeed | Integer | Current hard disk read speed, in Mb/s.  
SysHDDReadCritical | Integer | Critical hard disk read speed in Mb/s.  
SysHddWriteSpeed | Integer | Current hard disk write speed, in Mb/s.  
SysHddWriteCritical | Integer | Critical hard disk write speed in Mb/s.  
PerfConnectsMax | Integer | The maximum number of simultaneous connections to a server that has been achieved during the day.  
PerfConnectsCritical | Integer | Critical number of simultaneous connections to the server.  
PerfCpuMax | Integer | Maximum CPU load level.  
PerfCpuCritical | Integer | Critical CPU load server.  
PerfMemoryMin | Integer | The minimum size of free RAM and virtual memory in megabytes.  
PerfMemoryCritical | Integer | The critical size of free RAM and virtual memory in megabytes.  
PerfMemBlockMin | Integer | The largest available RAM block on the computer, which can be allocated for server operation. Indicated in megabytes.  
PerfMemBlockCritical | Integer | The critical size of the largest available RAM block. Indicated in megabytes.  
PerfNetworkMax | Integer | Maximum network usage level for the current day.  
PerfNetworkCritical | Integer | Critical network usage level.  
PerfSocketsMax | Integer | The maximum number of active sockets per day.  
PerfSocketsCritical | Integer | The critical number of active sockets.  
  
<a id="data"></a>
## Server Data (#data)

Parameter | Type | Description  
UpdateLastTime | Integer | Last update time in seconds elapsed since 01.01.1970.  
UpdateBuild | Integer | Last update version.  
UpdateAttempts | Integer | Number of update attempts.  
  
<a id="trade"></a>
## Trade Server Parameters (#trade)

Parameter | Type | Purpose  
DemoMode | Integer | Demo account allocation mode. Passed in a value of the [EnDemoMode (#endemomode)](../../../../Configuration-Interfaces/Network/IMTConServerTrade/Enumerations.md#endemomode) enumeration.  
DemoPeriod | Integer | Demo account period in days.  
OvernightMode | Integer | The overnight mode. Passed in a value of the [EnOvernightMode (#enovernightmode)](../../../../Configuration-Interfaces/Network/IMTConServerTrade/Enumerations.md#enovernightmode) enumeration.  
OvernightTime | Integer | Time of transition to the next day in minutes elapsed since 00:00.  
OvernightTimeLast | Integer | Date and time of the last transition to the next day in seconds elapsed since 01.01.1970.  
OvernightTimePrev | Integer | Date and time of the transition to the next day preceding the last transition, in seconds elapsed since 01.01.1970.  
OvernightDays | Integer | Schedule of operations related to the trading day closure.  
OvermonthMode | Integer | The mode of transition to the next month. Passed in a value of the [EnOvernightMode (#enovermonthmode)](../../../../Configuration-Interfaces/Network/IMTConServerTrade/Enumerations.md#enovermonthmode) enumeration.  
OvermonthTimeLast | Integer | Date and time of the last transition to the next month in seconds elapsed since 01.01.1970.  
OvermonthTimePrev | Integer | Date and time of the transition to the next month preceding the last transition, in seconds elapsed since 01.01.1970.  
LoginsRange | Array of integers | Array with the login range description.  
OrdersRange | Array of integers | Array with the order range description.  
DealsRange | Array of integers | Array with the deal range description.  
TotalUsers | Integer | Total number of accounts on the trade server.  
TotalUsersReal | Integer | Total number of real accounts on the trade server.  
TotalDeals | Integer | Total number of deals executed on the trade server.  
TotalOrders | Integer | Total number of active orders placed on the trade server.  
TotalOrdersHistory | Integer | Total number of orders in the history on the trade server.  
TotalPositions | Integer | Total number of positions on the trade server.  
  
<a id="history"></a>
## History Server Parameters (#history)

Parameter | Type | Description  
DatafeedsTimeout | Integer | Timeout of data feeds before switching to other ones. This is done in seconds.  
NewsMax | Integer | The maximum number of news that can be stored on the history server.  
  
<a id="access"></a>
## Access Server Parameters (#access)

Parameter | Type | Description  
Priority | Integer | Base priority of the access server. The main priority values ​​are available in the [EnServerPriority (#enserverpriority)](../../../../Configuration-Interfaces/Network/IMTConServerAccess/Enumerations.md#enserverpriority) enumeration.  
AntifloodEnabled | Integer | Antiflood control: 0 — disabled, 1 — enabled.  
AntifloodConnects | Integer | The maximum number of connections from one IP address for a certain period of time, after which the address is temporarily blocked.  
AntifloodErrors | Integer | The maximum number of incorrect connections, after which the IP address is temporarily blocked.  
NewsMax | Integer | The maximum number of news that can be stored on the access server.  
BalancingConnections | Integer | The current number of connections to the access server.  
BalancingPriority | Integer | Current priority of the access server.  
AccessMask | Integer | Allowed types of connection to the access server. The types are passed using the [EnAccessMask (#enaccessmask)](../../../../Configuration-Interfaces/Network/IMTConServerAccess/Enumerations.md#enaccessmask) enumeration.  
AccessFlags | Integer | Additional access server settings. Passed using the [EnAccessFlags (#enaccessflags)](../../../../Configuration-Interfaces/Network/IMTConServerAccess/Enumerations.md#enaccessflags) enumeration values.  
Servers | Array of integers | Array with IDs of trade servers, connection to which is established via this access server.  
  
<a id="backup"></a>
## Backup Server Parameters (#backup)

Parameter | Type | Description  
PairServer | Integer | ID of the server to backup.  
BackupFlags | Integer | Backup flags. Passed using the [EnBackupFlags (#enbackupflags)](../../../../Configuration-Interfaces/Network/IMTConServerBackup/Enumerations.md#enbackupflags) enumeration values.  
BackupPath | String | The path to save backups.  
BackupPeriod | Integer | Backup frequency in hours.  
BackupTTL | Integer | Period to keep backups in days.  
BackupFullTime | Integer | Full backup copy creation time in minutes elapsed since 00:00.  
SQLMode | Integer | Mode of data exporting to an SQL database. Database type for data export. Passed in a value of the [EnSQLExportMode (#ensqlexportmode)](../../../../Configuration-Interfaces/Network/IMTConServerBackup/Enumerations.md#ensqlexportmode) enumeration.  
SQLServer | String | The address of the server, on which the database is installed.  
SQLLogin | String | Login for connecting to an SQL database.  
SQLPassword | String | Password for connecting to an SQL database.  
SQLFolder | String | The name of the SQL database the data is exported to.  
SQLFlags | Integer | Additional SQL export settings. Passed using the [EnSQLExportFlags (#ensqlexportflags)](../../../../Configuration-Interfaces/Network/IMTConServerBackup/Enumerations.md#ensqlexportflags) enumeration values.  
SQLPeriod | Integer | The frequency of price and profit data export. Indicated in minutes.  
SQLExportLastSync | Integer | The time of the last full synchronization of databases and platform configurations with the SQL database. Specified in seconds since 01.01.1970. If data export is disabled or synchronization is in progress, the value is 0. The full synchronization is launched when a backup server is started or after connection to the SQL database or to the trading server is lost. After synchronization, the SQL database is updated in real time in accordance with the transactions of changes in the platform databases.  
  
<a id="antiddos"></a>
## AntiDDoS Server Parameters (#antiddos)

Parameter | Type | Description  
Priority | Integer | Basic priority of the Anti DDoS server. The main priority values ​​are available in the [EnServerPriority (#enserverpriority)](../../../../Configuration-Interfaces/Network/IMTConServerAntiDDoS/Enumerations.md#enserverpriority) enumeration.  
AccessMask | Integer | Allowed types of connection to the Anti DDoS server. The types are passed using the [EnAccessMask (#enaccessmask)](../../../../Configuration-Interfaces/Network/IMTConServerAntiDDoS/Enumerations.md#enaccessmask) enumeration.  
Servers | Array of integers | Array with IDs of trade servers, the connection to which is implemented through this Anti DDoS server.  
Sources | Array of strings | Range of IP addresses of Anti DDoS provider's proxy servers.  
  
<a id="certificate"></a>
## Certificate parameters (#certificate)

Parameter | Type | Description  
Timestamp | Integer | Certificate timestamp.  
Name | Integer | Certificate name. Here the "Common Name" certificate field is passed. In this field, the domain for which the certificate is issued, is indicated.  
Thumbprint | Array of integers | Certificate thumbprint — the "Thumbprint" field.
