[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerBackup](../IMTConServerBackup.md) / BackupLastFull

[Previous](BackupLastStartup.md) | [Next](BackupLastArchive.md)

# IMTConServerBackup::BackupLastFull

Get the creation time of the last [file copy (#file)](https://support.metaquotes.net/ru/docs/mt5/platform/components/backup_server/backup_server_features#file) of all databases.

C++
    
    
    INT64  IMTConServerBackup::BackupLastFull()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConServerBackup.BackupLastFull()

### Return Value

The creation time of the last full copy of the databases in seconds since 01.01.1970.
