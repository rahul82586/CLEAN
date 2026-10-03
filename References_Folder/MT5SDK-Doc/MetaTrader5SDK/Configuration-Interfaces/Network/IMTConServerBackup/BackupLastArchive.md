[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerBackup](../IMTConServerBackup.md) / BackupLastArchive

[Previous](BackupLastFull.md) | [Next](SQLExportMode.md)

# IMTConServerBackup::BackupLastArchive

Get the creation time of the last [additional file copy (#archive-backup-period)](https://support.metaquotes.net/ru/docs/mt5/platform/administration/admin_network/network_add_edit/network_backup_server#archive-backup-period).

C++
    
    
    INT64  IMTConServerBackup::BackupLastArchive()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConServerBackup.BackupLastArchive()

### Return Value

The creation time of the last additional file copy in seconds since 01.01.1970.
