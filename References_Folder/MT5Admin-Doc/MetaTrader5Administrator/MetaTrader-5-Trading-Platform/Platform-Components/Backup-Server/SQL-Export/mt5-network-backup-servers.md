[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_network_backup_servers

[Previous](mt5-network-trade-servers.md) | [Next](mt5-network-backup-folders.md)

# mt5_network_backup_servers

Data on the [backup servers settings](../../../Platform-Setup/Network-cluster/Configuring-Servers/Backup-Server.md) is exported to this table. The table contains the following fields:

Name | Type | Description  
Login | Integer | Server ID.  
PairrServer | Integer | ID of the server to backup.  
BackupFlags | Integer | [Backup settings (#backup)](../../../Platform-Setup/Network-cluster/Configuring-Servers/Backup-Server.md#backup). The settings are specified as a sum of flags:

  * 1 — enables backup.
  * 2 — enables the backup of tick data.
  * 4 — enables the possibility to use the server for the automatic Failover, with which the system switches to this backup server.
  * 8 — enables synchronization of logs with the primary server.

  
BackupPath | String | The path to save backups.  
BackupPeriod | Integer | Backup frequency:

  * 0 — no periodic backups
  * 1 — every 15 minutes
  * 2 — every 30 minutes
  * 3 — every hour
  * 4 — every 4 hours
  * 5 — every day

  
BackupTtl | Integer | Period to keep backups:

  * 1 — one day
  * 2 — three days
  * 3 — one week
  * 4 — one month
  * 5 — three months
  * 6 — six months

  
BackupTimeFull | Integer | Time of creating full backup copies in minutes since 00:00.  
BackupLastStartup | DateTime | The last backup copy creation time when launching the server in the YYYY-MM-DD HH:MM:SS.MSC format.  
BackupLastFull | DateTime | The last full backup copy creation time in the YYYY-MM-DD HH:MM:SS.MSC format.  
BackupLastArchive | DateTime | The last increment backup copy creation time in the YYYY-MM-DD HH:MM:SS.MSC format.  
BackupLastSync | DateTime | The time of the last successful synchronization with the backed up server in the YYYY-MM-DD HH:MM:SS.MSC format.  
SqlMode | Integer | Mode of exporting data to an SQL database:

  * 0 — export disabled
  * 1 — export to Microsoft SQL Server
  * 2 — export to FireBird
  * 3 — export to MySQL
  * 4 — export to Oracle

  
SqlServer | String | The address of the server the database is installed on.  
SqlFolder | String | The name of the SQL database the data is exported to.  
SqlFlags | Integer | Additional settings of data export to an SQL database. Defined by the sum of flags: 1 — export trade history to separate tables. 2 — do not export accounts and trade operations of demo groups For example, the value of 3 means that both settings are enabled.  
SqlPeriod | Integer | The frequency of price and profit data export.  
SQLExportLastSync | Integer | The time of the last full synchronization of databases and platform configurations with the SQL database. Specified in seconds since 01.01.1970. If data export is disabled or synchronization is in progress, the value is 0. The full synchronization is launched when a backup server is started or after connection to the SQL database or to the trading server is lost. After synchronization, the SQL database is updated in real time in accordance with the transactions of changes in the platform databases.
