[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerBackup](../IMTConServerBackup.md) / Enumerations

[Previous](../IMTConServerBackup.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConServerBackup](../IMTConServerBackup.md) class contains the following enumerations:

  * [IMTConServerBackup::EnBackupFlags (#enbackupflags)](Enumerations.md#enbackupflags)
  * [IMTConServerBackup::EnBackupPeriod (#enbackupperiod)](Enumerations.md#enbackupperiod)
  * [IMTConServerBackup::EnBackupTTL (#enbackupttl)](Enumerations.md#enbackupttl)
  * [IMTConServerBackup::EnSQLExportMode (#ensqlexportmode)](Enumerations.md#ensqlexportmode)
  * [IMTConServerBackup::EnSQLExportFlags (#ensqlexportflags)](Enumerations.md#ensqlexportflags)



<a id="enbackupflags"></a>
## IMTConServerBackup::EnBackupFlags (#enbackupflags)

Backup flags are enumerated in IMTConServerBackup::EnBackupFlags.

ID | Value | Description  
FLAG_ENABLE_BACKUPS | 0x00000001 | The flag of enabling backup on the server. If a server does not have this flag, no backups will be created on this server. This may be necessary if the backup server is only used to export data to an SQL database.  
FLAG_ENABLE_TICKS | 0x00000002 | When working with the history server, the backup server can save copies of accumulated ticks. By default, this function is disabled since tick data occupy large amount of space. To enable it, set the FLAG_ENABLE_TICKS flag. Also, make sure to configure the [IMTConServer::BackupTTL](BackupTTL.md) parameter. In case of long storage periods, backup copies of ticks may quickly occupy all available disk space.  
FLAG_ENABLE_FAILOVER | 0x00000004 | The trading platform features the automatic failover system, with which it switches to a backup server. By default, the platform can switch to any of the existing backup servers. If a certain backup server should not be used by the automatic failover system, disable the FLAG_ENABLE_FAILOVER for that server. This may be needed if the backup server is used only for exporting data to an SQL database. You may also disable the flag FLAG_ENABLE_BACKUPS for such servers, to save resources required for the creation of backup copies in a disk. By removing the flag you only disable switching in automatic mode. If necessary, you can switch to this backup server manually.  
FLAG_ENABLE_LOG | 0x00000008 | The backup server is a copy of the backed up one since it stores the same data as the main server, including log files. If you only use the backup server for data export to SQL, you can disable log synchronization with the primary server to save disk space. This can be done by removing the FLAG_ENABLE_LOG.  
  
The enumeration is used in the [IMTConServerBackup::BackupFlags](BackupFlags.md) method.

<a id="enbackupperiod"></a>
## IMTConServerBackup::EnBackupPeriod (#enbackupperiod)

Possible backup period are specified in IMTConServerBackup::EnBackupPeriod.

ID | Value | Description  
BACKUP_DISABLED | 0 | Periodic backups are not created.  
BACKUP_15MINUTES | 1 | Every 15 minutes.  
BACKUP_30MINUTES | 2 | Every 30 minutes.  
BACKUP_1HOUR | 3 | Every hour.  
BACKUP_4HOURS | 4  | Every 4 hours.  
BACKUP_1DAY | 5 | Every day.  
BACKUP_FIRST |  | Beginning of enumeration. It corresponds to BACKUP_15MINUTES.  
BACKUP_LAST |  | End of enumeration. It corresponds to BACKUP_1DAY.  
  
This enumeration is used in the [IMTConServerBackup::BackupPeriod](BackupPeriod.md) method.

<a id="enbackupttl"></a>
## IMTConServerBackup::EnBackupTTL (#enbackupttl)

Possible periods of backup storing are listed in IMTConServerBackup::EnBackupTTL.

ID | Value | Description  
BACKUP_TTL_1DAY | 1 | One day.  
BACKUP_TTL_3DAYS | 2 | Three days.  
BACKUP_TTL_1WEEK | 3 | One week.  
BACKUP_TTL_1MONTH | 4  | One month.  
BACKUP_TTL_3MONTHS | 5 | Three months.  
BACKUP_TTL_6MONTHS | 6 | Six months.  
BACKUP_TTL_FIRST |  | Beginning of enumeration. It corresponds to BACKUP_TTL_1DAY.  
BACKUP_TTL_LAST |  | End of enumeration. It corresponds to BACKUP_TTL_6MONTHS.  
  
This enumeration is used in the [IMTConServerBackup::BackupTTL](BackupTTL.md) method.

<a id="ensqlexportmode"></a>
## IMTConServerBackup::EnSQLExportMode (#ensqlexportmode)

Modes of data export to an SQL database are enumerate in IMTConServerBackup::EnSQLExportMode.

ID | Value | Description  
SQL_MODE_NONE | 0 | Export is disabled.  
SQL_MODE_MSSQL | 1 | Export to Microsoft SQL Server.  
SQL_MODE_FIREBIRD | 2 | Export to FireBird.  
SQL_MODE_MYSQL | 3  | Export to MySQL.  
SQL_MODE_ORACLE | 4 | Export to Oracle.  
SQL_MODE_POSTGRESQL | 5 | Export to PostgreSQL.  
SQL_MODE_FIRST |  | Beginning of enumeration. Corresponds to SQL_MODE_NONE.  
SQL_MODE_LAST |  | End of enumeration. Corresponds to SQL_MODE_POSTGRESQL.  
  
This enumeration is used in the [IMTConServerBackup::SQLExportMode](SQLExportMode.md) method.

<a id="ensqlexportflags"></a>
## IMTConServerBackup::EnSQLExportFlags (#ensqlexportflags)

Additional flags of data export to an SQL database are enumerate in IMTConServerBackup::EnSQLExportFlags.

ID | Value | Description  
SQL_FLAG_NONE | 0x00000000 | No flags.  
SQL_FLAG_PARTITIONS | 0x00000001 | History orders and deals are exported to two separate tables by default. But as time goes by, order and deal bases may grow significantly leading to larger tables in SQL base. When this flag is enabled, history of orders and deals for each year will be exported to a separate table.  
SQL_FLAG_SKIP_DEMO | 0x00000002 | When this flag is enabled, accounts from demo groups, as well as trade operations (orders, deals and positions) of these accounts will not be exported to an SQL base.</t2>  
SQL_FLAG_ALL |  | End of enumeration. All flags are enabled.  
  
This enumeration is used in the [IMTConServerBackup::SQLExportFlags](SQLExportFlags.md) method.
