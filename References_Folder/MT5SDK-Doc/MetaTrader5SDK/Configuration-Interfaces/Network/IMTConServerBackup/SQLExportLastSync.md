[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerBackup](../IMTConServerBackup.md) / SQLExportLastSync

[Previous](SQLExportFolder.md) | [Next](FoldersAdd.md)

# IMTConServerBackup::SQLExportLastSync

Get the time of the last full synchronization of databases and platform configurations with the SQL database.

C++
    
    
    INT64  IMTConServerBackup::SQLExportLastSync()  const

.NET (Gateway/Manager API)
    
    
    long  IMTConServerBackup::SQLExportLastSync()

### Return Value

The time of the last full synchronization in seconds since 01.01.1970. If data export is disabled or synchronization is in progress, the method will return 0.

### Note

The full synchronization is launched when a backup server is started or after connection to the SQL database or to the trading server is lost. After synchronization, the SQL database is updated in real time in accordance with the transactions of changes in the platform databases.
