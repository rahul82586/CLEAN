[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerBackup](../IMTConServerBackup.md) / BackupLastStartup

[Previous](BackupLastSync.md) | [Next](BackupLastFull.md)

# IMTConServerBackup::BackupLastStartup

Get the creation time of the last database startup copy.

C++
    
    
    INT64  IMTConServerBackup::BackupLastStartup()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConServerBackup.BackupLastStartup()

### Return Value

The creation time of the last database startup copy in seconds since 01.01.1970.

### Note

When started, the backup server creates a [file copy (#file)](https://support.metaquotes.net/ru/docs/mt5/platform/components/backup_server/backup_server_features#file) of its databases which were synchronized with the main server in real time. This happens before synchronization with the main server in case its databases are already damaged. This enables the rollback to a previous state from the file copy if necessary.
